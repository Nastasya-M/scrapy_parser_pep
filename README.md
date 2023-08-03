# scrapy_parser_pep

### Описание 
```
Асинхронный парсер на базе фреймворка Scrapy - собирает актуальную иформацию о документах PEP с сайта https://peps.python.org/ и выводит собранную информацию в два файла .csv:

- Список PEP: номер, название и статус;
- Сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество).

### Технологи проекта:
```
Python
Scrapy
```

### Подготовка к запуску:
Клонировать репозиторий:
```
git clone https://github.com/Nastasya-M/scrapy_parser_pep
```
Создать виртуальное окружение:
```
python -m venv venv
```
Активировать виртуальное окружение и установить зависимости:
```
source venv/Scripts/activate
pip install -r requirements.txt
```
### Запуск парсера:
```
scrapy crawl pep

Автор: [Настасья Мартынова](https://github.com/Nastasya-M)