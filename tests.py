import pytest
from main import BooksCollector


class TestBooksCollector:


    @pytest.mark.parametrize('name_book', ["Мастер и Маргарита"])
    def test_add_new_book_add_book_true(self, name_book):  #добавление новой книги в словарь books_genre
        collector = BooksCollector()
        collector.add_new_book(name_book)

        assert name_book in collector.get_books_genre()

    def test_add_new_book_too_long_name_of_book_true(self):  # добавление новой книги в словарь books_genre с названием в 41 симвоо
        collector = BooksCollector()
        collector.add_new_book('Тайны Вселенной: путешествие в мир знаний')

        assert not 'Тайны Вселенной: путешествие в мир знаний' in collector.get_books_genre()


    def test_set_book_genre_set_fantastc_true(self):  #устанавливаем книге жанр
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")

        assert collector.get_book_genre("Мастер и Маргарита") == "Фантастика"

    @pytest.mark.parametrize('name_book, gener', [("Колобок", "Ужасы")])
    def test_get_book_genre_master_and_margarita_true(self, name_book, gener):  #получение жанра книги по названию
        collector = BooksCollector()
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, gener)

        assert collector.get_book_genre(name_book) == gener

    @pytest.mark.parametrize('name_book, gener', [("Колобок", "Ужасы")])
    def test_get_books_with_specific_genre_fantastic_true(self, name_book, gener):  #получение списка книг опредленного жанра
        collector = BooksCollector()
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, gener)

        assert collector.get_books_with_specific_genre(gener) == [name_book]

    @pytest.mark.parametrize('name_book, gener', [("Мастер и Маргарита", "Фантастика")])
    def test_get_books_genre_true(self, name_book, gener): #поолучение словаря books_genre
        collector = BooksCollector()
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, gener)

        assert collector.get_books_genre() == {name_book: gener}

    def test_get_books_for_children_add_azbuka_true(self): #получение списка книг, подходящие детям
        collector = BooksCollector()
        collector.add_new_book('Азбука')
        collector.set_book_genre('Азбука','Комедии')

        assert collector.get_books_for_children() == ['Азбука']

    @pytest.mark.parametrize('name_book, gener', [("1984", "Ужасы")])
    def test_get_books_for_children_add_adult_genre_false(self, name_book, gener):  # проверка не добавления книги со взрослым жанром
        collector = BooksCollector()
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, gener)

        assert not collector.get_books_for_children() == [name_book]

    @pytest.mark.parametrize('name_book', ["Мастер и Маргарита"])
    def test_add_book_in_favorites_add_master_and_margo_true(self, name_book): #добавляем книгу в избранное
        collector = BooksCollector()
        collector.add_new_book(name_book)
        collector.add_book_in_favorites(name_book)

        assert name_book in collector.favorites

    @pytest.mark.parametrize('name_book, gener', [("1984", "Ужасы")])
    def test_delete_book_from_favorites_delete_master_and_margo_true(self, name_book, gener): #удаление книги из избранного
        collector = BooksCollector()
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, gener)
        collector.add_book_in_favorites(name_book)
        collector.delete_book_from_favorites(name_book)

        assert name_book not in collector.favorites

    @pytest.mark.parametrize('name_book, gener', [("1984", "Ужасы")])
    def test_get_list_of_favorites_books_shows_master_and_margo_in_list_true(self, name_book, gener): # получение списка избранного
        collector = BooksCollector()
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, gener)
        collector.add_book_in_favorites(name_book)

        assert collector.get_list_of_favorites_books() == [name_book]
