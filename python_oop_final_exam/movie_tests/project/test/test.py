from project.movie import Movie
from unittest import TestCase, main


class MovieTests(TestCase):
    def setUp(self):
        self.movie = Movie("Test", 1990, 3.00)
        self.other_movie = Movie("NBH", 2000, 2.13)

    def test_movie_object_initialized_correctly(self):
        name = "Test"
        year = 1990
        rating = 3.00
        movie = Movie(name, year, rating)
        self.assertEqual(name, movie.name)
        self.assertEqual(year, movie.year)
        self.assertEqual(rating, movie.rating)
        self.assertEqual([], movie.actors)

    def test_initialize_with_empty_name_raises(self):
        name = ""
        year = 1990
        rating = 3.00
        with self.assertRaises(ValueError) as ex:
            movie = Movie(name, year, rating)
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_initialize_movie_older_than_1887(self):
        name = "Test"
        year = 1883
        rating = 3.00
        with self.assertRaises(ValueError) as ex:
            movie = Movie(name, year, rating)
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_new_actor(self):
        self.assertEqual([], self.movie.actors)
        name = "Ian"
        self.movie.add_actor(name)
        self.assertEqual([name], self.movie.actors)

    def test_try_add_existing_actor(self):
        name = "Ian"
        self.movie.actors = [name]
        self.assertEqual([name], self.movie.actors)
        result = self.movie.add_actor(name)
        self.assertEqual(f"{name} is already added in the list of actors!", result)
        self.assertEqual([name], self.movie.actors)

    def test_dunder_method_with_greater_value(self):
        result = self.movie > self.other_movie
        self.assertEqual(f'"{self.movie.name}" is better than "{self.other_movie.name}"', result)

    def test_dunder_method_with_lesser_value(self):
        self.other_movie.rating = 4.12
        result = self.movie > self.other_movie
        self.assertEqual(f'"{self.other_movie.name}" is better than "{self.movie.name}"', result)

    def test_repr_movie_without_actors(self):
        expected_result = f"Name: {self.movie.name}\n" \
               f"Year of Release: {self.movie.year}\n" \
               f"Rating: {self.movie.rating:.2f}\nCast: "
        self.assertEqual(expected_result, str(self.movie))

    def test_repr_returns_correctly(self):
        self.movie.actors = ["Ian", "Paul", "Robert"]
        expected_result = f"Name: {self.movie.name}\n" \
                          f"Year of Release: {self.movie.year}\n" \
                          f"Rating: {self.movie.rating:.2f}\n" \
                          f"Cast: {', '.join(self.movie.actors)}"
        self.assertEqual(expected_result, str(self.movie))


if __name__ == "__main__":
    main()
