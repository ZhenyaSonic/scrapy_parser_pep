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
        filename = (
            f'status_summary_{datetime.now().strftime(DATETIME_FORMAT)}.csv'
        )
        filepath = BASE_DIR / RESULTS / filename
        with open(filepath, 'w') as csvfile:
            writer = csv.writer(
                csvfile,
                dialect=csv.excel,
                quoting=csv.QUOTE_NONE
            )
            writer.writerows((
                ('Статус', 'Количество'),
                *self.status_counts.items(),
                ('Всего', sum(self.status_counts.values()))
            ))
