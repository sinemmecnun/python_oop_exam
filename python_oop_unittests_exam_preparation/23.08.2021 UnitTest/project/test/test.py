from project.library import Library
from unittest import TestCase, main


class LibraryTests(TestCase):
    def setUp(self) -> None:
        self.library = Library("Test")

    def test_object_correctly_initialized(self):
        name = "Test"
        library = Library(name)
        self.assertEqual(name, library.name)
        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

    def test_initialize_library_with_empty_string_raises(self):
        name = ""
        with self.assertRaises(ValueError) as ex:
            library = Library(name)
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_existing_book(self):
        self.library.books_by_authors = {"Holly Black": ["Cruel Prince"]}
        self.library.add_book("Holly Black", "Cruel Prince")

        self.assertEqual({"Holly Black": ["Cruel Prince"]}, self.library.books_by_authors)

    def test_add_new_author(self):
        self.assertEqual({}, self.library.books_by_authors)
        author_name = "Clare"
        book_title = "Shadowhunters"
        self.library.add_book(author_name, book_title)
        self.assertEqual({author_name: [book_title]}, self.library.books_by_authors)

    def test_add_new_book_to_existing_author(self):
        self.library.books_by_authors = {"Clare": []}
        author_name = "Clare"
        book_title = "Shadowhunters"
        self.library.add_book(author_name, book_title)
        self.assertEqual({author_name: [book_title]}, self.library.books_by_authors)

    def test_add_existing_reader(self):
        self.library.readers = {"Berrin": []}
        result = self.library.add_reader("Berrin")
        self.assertEqual(f"Berrin is already registered in the {self.library.name} library.", result)
        self.assertEqual({"Berrin": []}, self.library.readers)

    def test_add_new_reader(self):
        self.assertEqual({}, self.library.readers)
        self.library.add_reader("Berrin")
        self.assertEqual({"Berrin": []}, self.library.readers)

    def test_rent_book_to_not_registered_reader(self):
        reader_name = "Berrin"
        author_name = "Clare"
        book_title = "Shadowhunters"
        self.assertEqual({}, self.library.readers)
        result = self.library.rent_book(reader_name, author_name, book_title)
        self.assertEqual(f"{reader_name} is not registered in the {self.library.name} Library.", result)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_rent_book_by_non_existent_author(self):
        self.library.readers = {"Berrin": []}
        reader_name = "Berrin"
        author_name = "Clare"
        book_title = "Shadowhunters"
        self.assertEqual({}, self.library.books_by_authors)
        result = self.library.rent_book(reader_name, author_name, book_title)
        self.assertEqual(f"{self.library.name} Library does not have any {author_name}'s books.", result)
        self.assertEqual({"Berrin": []}, self.library.readers)

    def test_rent_book_not_in_library(self):
        self.library.readers = {"Berrin": []}
        self.library.books_by_authors = {"Clare": []}
        reader_name = "Berrin"
        author_name = "Clare"
        book_title = "Shadowhunters"
        result = self.library.rent_book(reader_name, author_name, book_title)
        self.assertEqual(f"""{self.library.name} Library does not have {author_name}'s "{book_title}".""", result)
        self.assertEqual({"Berrin": []}, self.library.readers)
        self.assertEqual({"Clare": []}, self.library.books_by_authors)

    def test_rent_book_makes_correct_changes(self):
        self.library.readers = {"Berrin": []}
        self.library.books_by_authors = {"Clare": ["Shadowhunters"]}
        reader_name = "Berrin"
        author_name = "Clare"
        book_title = "Shadowhunters"
        self.library.rent_book(reader_name, author_name, book_title)
        self.assertEqual({"Berrin": [{"Clare": "Shadowhunters"}]}, self.library.readers)
        self.assertEqual({"Clare": []}, self.library.books_by_authors)


if __name__ == '__main__':
    main()