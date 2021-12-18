import random
import json
from itertools import count
from faker import Faker
from typing import Iterator
from conf import MODEL


def main():
    """Основная функция

     запускает функцию генератор книг (book_generator())
     формирует список из 100 книг
     записывает полученный список в json-файл (books_generated.json)

     """

    python_object = []
    pk = get_pk()
    for _ in range(100):
        python_object.append(next(book_generator(pk)))
    print(python_object)

    with open("books_generated.json", "w", encoding="utf-8") as f_output:
        json.dump(python_object, f_output, indent=4, ensure_ascii=False)


def book_generator(pk) -> Iterator:
    """Функция генератор книг

    аргумент pk - автоинкремент, который увеличивается на 1 при генерации нового объекта
    формирует словарь книг в соответсвии с примером

    """
    pk = next(pk)
    keys = ["model", "pk", "fields"]
    values = [MODEL, pk, get_fields()]
    yield dict(zip(keys, values))


def get_pk() -> int:
    """Функция получения pk

    """
    for current_number in count(1):
        yield current_number


def get_fields() -> dict:
    """Функция формирования описания книги

    формируется словарь описания каждой книги, в котором указывается название книги (title), год выпуска (year),
    количество страниц (pages), код по isbn13 (isbn13), рейтинг (rating), цена (price) и авторы (author)

    """
    keys = ["title", "year", "pages", "isbn13", "rating", "price", "author"]
    values = [get_title(), get_year(), get_pages(), get_isbn13(), get_rating(), get_price(), get_author()]
    return dict(zip(keys, values))


def get_title() -> str:
    """Функция получения названия книги

    случайным образом из файла books.txt получаем название книги
    в функции учтена кодировка, на случай, если названия книг будут на русском языке

    """
    books = []
    with open("books.txt", "r", encoding='utf-8') as f_input:
        for line in f_input:
            books.append(line.rstrip())
    return random.choice(books)


def get_year() -> int:
    """Функция получения года

    в данной фунцкии случайным образом генерируется натуральное число, означающее год выспуска книги.
    Мной были установлены граничные значения для интервала 18800 и 2021, эти значения можно менять

    """
    return random.randint(1800, 2021)


def get_pages() -> int:
    """Функция получения количества страниц в книге

    в данной функции случайным образом генерируется натуральное число, означающее количество страниц в книге.
    Мной были установлены граничные значения для интервала 15 и 1000, эти значения можно менять

    """
    return random.randint(15, 1000)


def get_isbn13() -> str:
    """Функция получения isbn13

    в данной функции генерируется строка в соответствии с isbn13. Для генерации такого кода используется
    метод isbn13 модуля Faker

    """
    fake = Faker()
    return fake.isbn13()


def get_rating() -> float:
    """Функция получения рейтинга книги

    в данной функции случайным образом генерируется число с плавающей запятой в диапазоне от 0 до 5.
    Также было установлено округление до первого знака, т.к. привычный формат рейтинга, напрмер, 4.8

    """
    rating = random.uniform(0, 5)
    return round(rating, 1)


def get_price() -> float:
    """Функция получения цены книги

    в данной функции случайным образом генерируется число с плавающей запятой. Граничные значения диапазона 100 и 5000
    были установлены мнной и могут меняться.
    Также было устанослено округление до второго знака, т.к. привычный формат цен, напрмер, 350.60

    """
    price = random.uniform(100, 5000)
    return round(price, 2)


def get_author() -> list[str]:
    """Функция получения автора

    в данной функции с имользованием метода модуля Faker был случайным образом сгенерирован список авторв,
    при этом в соответсвии с заданием усановлена генерация списка авторов от 1 до 3
    в функции учтено написание ФИО авторов на русском языке

    """
    fake = Faker(locale='ru-RU')
    author_name_list = []
    for _ in range(5):
        author_name_list.append(fake.name())
    return random.sample(author_name_list, random.randint(1, 3))


if __name__ == "__main__":
    main()
