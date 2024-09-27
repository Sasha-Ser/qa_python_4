# qa_python
Использовал фикстуру с парметром autouse, коазалось не надо было параметризацией.

1. test_add_new_book_add_book_true - проверяет добавление новой книги в словарь books_genre
2. test_add_new_book_too_long_name_of_book_true - проверяет, что не будет добавления новой книги в словарь books_genre с названием длинной в 41 символ
3. test_set_book_genre_set_fantastc_true - проверят устанавление книге жанра
4. test_get_book_genre_master_and_margarita_true - проверяет получение жанра по названию книги
5. test_get_books_with_specific_genre_fantastic_true - проверяет получение списка книг опредленного жанра
6. test_get_books_genre_true - проверяет получение словаря books_genre
7. test_get_books_for_children_add_azbuka_true - проверяет получение списка книг для детей
8. test_get_books_for_children_add_adult_genre_false - проверяет добавит в список книг для детей книгу со взрослым жанром
9. test_add_book_in_favorites_add_master_and_margo_true - проверяет добавление книгу в избранное
10. test_delete_book_from_favorites_delete_master_and_margo_true - проверяет удаление книги из избранного
11. test_get_list_of_favorites_books_shows_master_and_margo_in_list_true - проверяет получение списка избранного
