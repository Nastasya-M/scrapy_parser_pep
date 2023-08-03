import csv
from datetime import datetime as dt
from .settings import BASE_DIR, RESULTS_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = {}
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        status = item['status']
        if self.results.get(status):
            self.results[status] += 1
        else:
            self.results[status] = 1
        return item

    def close_spider(self, spider):
        datetime = dt.now().strftime('%Y_%m_%d_%H_%M_%S')
        with open(
            self.results_dir / f'status_summary_{datetime}.csv',
            mode='w',
            encoding='utf-8'
        ) as f:
            csv.writer(f, dialect=csv.unix_dialect).writerows(
                (
                    ('Статус', 'Количество'),
                    *(self.results.items()),
                    ['Total', sum(self.results.values())]
                )
            )
