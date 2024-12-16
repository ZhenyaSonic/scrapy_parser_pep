import csv
import os
from datetime import datetime
from collections import defaultdict

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT, RESULTS


class PepParsePipeline:

    def __init__(self):
        os.makedirs(BASE_DIR / RESULTS, exist_ok=True)

    def open_spider(self, spider):
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        current_time = datetime.now().strftime(DATETIME_FORMAT)
        filename = f'status_summary_{current_time}.csv'
        filepath = BASE_DIR / RESULTS / filename

        with open(filepath, 'w', newline='') as csvfile:
            csv.writer(
                csvfile,
                dialect=csv.excel,
                quoting=csv.QUOTE_NONE
            ).writerows((
                ('Статус', 'Количество'),
                *self.status_counts.items(),
                ('Всего', sum(self.status_counts.values()))
            ))
