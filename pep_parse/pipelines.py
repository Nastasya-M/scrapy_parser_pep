import csv
from datetime import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = {}
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        status = item['status']
        if self.results.get(status):
            self.results[status] += 1
        else:
            self.results[status] = 1
        return item

    def close_spider(self, spider):
        results = [('Статус', 'Количество')]
        datetime = dt.now().strftime('%Y_%m_%d_%H_%M_%S')
        file_path = self.results_dir / f'status_summary_{datetime}.csv'
        with open(file_path, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow((results))
            for key, value in self.results.items():
                writer.writerow([key, value])
            writer.writerow(['Total', sum(self.results.values())])
