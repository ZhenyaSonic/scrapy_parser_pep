from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BOT_NAME = 'pep_parse'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
RESULTS = 'results'
ROBOTSTXT_OBEY = True
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
FEEDS = {
    f'{RESULTS}/pep_%(time)s.csv': {
        'format': 'csv',
        'encoding': 'utf-8',
        'overwrite': True,
        'fields': ['number', 'name', 'status'],
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
