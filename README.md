# scrapy_parser_pep

## Асинхронный парсинг документации Python

### Описание проекта
Проект представляет собой консольное приложение для асинхронного парсинга документации с сайта Python.org с помощью библиотеки Scrapy.

### Возможности проекта
- Получение номера, названия и статуса каждого документа PEP.
- Подсчет количества документов PEP в разных статусах и формирование сводной таблицы.
- Полученные данные выводятся в файлы .CSV с указанием даты и времени в названии.

### Установка
Клонируйте репозиторий локально:

```bash
git clone git@github.com:ZhenyaSonic/scrapy_parser_pep.git
```

Перейдите в директорию проекта:
```bash
cd scrapy_parser_pep

python -m venv venv
```
Запустите виртуальное окружение
```bash
source venv/Scripts/activate
```
Обновите pip
```bash
pip install --upgrade pip
```
Установите зависимости
```bash
pip install -r requirements.txt
```
Работа с приложением
Запуск приложения

```bash
scrapy crawl pep
```
Файлы с результатами парсинга доступны в папке results:
```bash
cd results
```
Основные технологии
Python 3.9.13, Scrapy 2.5.1

Автор
Братанов Евгений https://github.com/ZhenyaSonic/