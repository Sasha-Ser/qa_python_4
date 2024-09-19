import pytest
from main import BooksCollector


class TestBooksCollector:
    @pytest.fixture(autouse=True)
    def book_info(self):
        self.book = "Мастер и Маргарита"
        self.genre = "Фантастика"
        return self.book

    def test_add_new_book_add_book_true(self):  #добавление новой книги в словарь books_genre
        collector = BooksCollector()
        collector.add_new_book(self.book)

        assert self.book in collector.get_books_genre()

    def test_add_new_book_too_long_name_of_book_true(self):  # добавление новой книги в словарь books_genre с названием в 41 симвоо
        collector = BooksCollector()
        collector.add_new_book('Тайны Вселенной: путешествие в мир знаний')

        assert not 'Тайны Вселенной: путешествие в мир знаний' in collector.get_books_genre()

    def test_set_book_genre_set_fantastc_true(self):  #устанавливаем книге жанр
        collector = BooksCollector()
        collector.add_new_book(self.book)
        collector.set_book_genre(self.book, 'Фантастика')

        assert collector.get_book_genre(self.book) == 'Фантастика'

    def test_get_book_genre_master_and_margarita_true(self):  #получение жанра книги по названию
        collector = BooksCollector()
        collector.add_new_book(self.book)
        collector.set_book_genre(self.book, self.genre)

        assert collector.get_book_genre(self.book) == self.genre

    def test_get_books_with_specific_genre_fantastic_true(self):  #получение списка книг опредленного жанра
        collector = BooksCollector()
        collector.add_new_book(self.book)
        collector.set_book_genre(self.book, self.genre)

        assert collector.get_books_with_specific_genre(self.genre) == [self.book]

    def test_get_books_genre_true(self): #поолучение словаря books_genre
        collector = BooksCollector()
        collector.add_new_book(self.book)
        collector.set_book_genre(self.book, self.genre)

        assert collector.get_books_genre() == {self.book: self.genre}

    def test_get_books_for_children_add_azbuka_true(self): #получение списка книг, подходящие детям
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.set_book_genre('Азбука','Комедии')

        assert collector.get_books_for_children() == ['Азбука']

    def test_get_books_for_children_add_adult_genre_false(self):  # проверка не добавления книги со взрослым жанром
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1985', 'Ужасы')

        assert not collector.get_books_for_children() == ['1984']

    def test_add_book_in_favorites_add_master_and_margo_true(self): #добавляем книгу в избранное
        collector = BooksCollector()
        collector.add_new_book(self.book)
        collector.set_book_genre(self.book, self.genre)
        collector.add_book_in_favorites(self.book)

        assert self.book in collector.favorites

    def test_delete_book_from_favorites_delete_master_and_margo_true(self): #удаление книги из избранного
        collector = BooksCollector()
        collector.add_new_book(self.book)
        collector.set_book_genre(self.book, self.genre)
        collector.add_book_in_favorites(self.book)
        collector.delete_book_from_favorites(self.book)

        assert self.book not in collector.favorites

    def test_get_list_of_favorites_books_shows_master_and_margo_in_list_true(self): # получение списка избранного
        collector = BooksCollector()
        collector.add_new_book(self.book)
        collector.set_book_genre(self.book, self.genre)
        collector.add_book_in_favorites(self.book)

        assert collector.favorites == [self.book]
