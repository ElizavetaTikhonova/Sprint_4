class TestBooksCollectorInterfase:

    def test_add_new_book_valid_len_name(self, collector):
        
        book_name = "Война и мир"
        collector.add_new_book(book_name)
        lst_book = collector.get_books_genre().keys() 
        assert book_name in lst_book
        
    def test_set_book_genre_with_valid_genre(self, collector):
        book_name = 'Война и Мир'
        genre = 'Ужасы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        dict_book = collector.get_books_genre()
        assert dict_book[book_name] == genre

    def test_get_book_genre_get_by_name(self, collector):
        book_name = 'Гарри Поттер'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        genre_book = collector.get_book_genre(book_name)
        assert genre_book == genre

    def test_get_books_with_specific_genre_empty_collector(self, collector):
        assert collector.get_books_with_specific_genre('Фантастика') == []

    def test_get_books_with_specific_genre_one_book(self, collector):   
        book_name = 'Гарри Поттер'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер'] 
        
    def test_get_books_genre_with_multiple_books(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Детективы')

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        collector.add_new_book('Холодное сердце')
        collector.set_book_genre('Холодное сердце', 'Мультфильмы')
        
        assert collector.get_books_genre() == {
                'Война и мир': 'Детективы',
                'Гарри Поттер': 'Фантастика',
                'Холодное сердце': 'Мультфильмы'} 

    def test_get_books_for_children_all_books_for_children(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Незнайка")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.set_book_genre("Незнайка", "Комедии")
        assert collector.get_books_for_children() == ["Гарри Поттер", "Незнайка"]            

    def test_add_book_in_favorites_new_book(self, collector):
        
        book_name = 'Шерлок Холмс'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        lst_favorites = collector.get_list_of_favorites_books()
        assert book_name in lst_favorites

    def test_delete_existing_book_from_favorites(self, collector):
        
        book_name = 'Шерлок Холмс'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_add_unknown_book(self, collector):
        book_name = 'Шерлок Холмс'
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == []
        
    def test_get_books_for_children_no_children_books(self, collector):
        collector.add_new_book('Звонок')
        collector.set_book_genre('Звонок', 'Ужасы')   

        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы') 
        
        assert collector.get_books_for_children() == [] 