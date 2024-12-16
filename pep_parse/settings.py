from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BOT_NAME = 'pep_parse'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
RESULTS = 'results'
NEWSPIDER_MODULE = 'pep_parse.spiders'
ROBOTSTXT_OBEY = True
SPIDER_MODULES = ['pep_parse.spiders']
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
