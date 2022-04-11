from unittest import TestCase, main

from project.student_report_card import StudentReportCard


class StudentReportCardTests(TestCase):
    def setUp(self):
        self.student_report_card = StudentReportCard("Test", 1)

    def test_student_report_card_initialized_correctly(self):
        student_name = "Test"
        school_year = 1
        student_report_card = StudentReportCard(student_name, school_year)
        self.assertEqual(student_name, student_report_card.student_name)
        self.assertEqual(school_year, student_report_card.school_year)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_initialize_student_report_card_with_empty_string_for_name_raises(self):
        student_name = ""
        school_year = 1
        with self.assertRaises(ValueError) as ex:
            student_report_card = StudentReportCard(student_name, school_year)
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_initialize_student_report_card_year_lesser_than_1(self):
        student_name = "Test"
        school_year = 0
        with self.assertRaises(ValueError) as ex:
            student_report_card = StudentReportCard(student_name, school_year)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_initialize_student_report_card_year_greater_than_12(self):
        student_name = "Test"
        school_year = 13
        with self.assertRaises(ValueError) as ex:
            student_report_card = StudentReportCard(student_name, school_year)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_initialize_school_year_12(self):
        student_report_card = StudentReportCard("Test", 12)
        self.assertEqual(12, student_report_card.school_year)

    def test_initialize_school_year_between_1_and_12(self):
        student_report_card = StudentReportCard("Test", 3)
        self.assertEqual(3, student_report_card.school_year)

    def test_add_grade_to_new_subject(self):
        self.assertEqual({}, self.student_report_card.grades_by_subject)
        subject = "Math"
        grade = 6
        self.student_report_card.add_grade(subject, grade)
        self.assertEqual({subject: [grade]}, self.student_report_card.grades_by_subject)

    def test_add_grade_to_existing_subject(self):
        subject = "Math"
        grade = 6
        self.student_report_card.grades_by_subject = {subject: [grade]}
        self.assertEqual({subject: [grade]}, self.student_report_card.grades_by_subject)
        self.student_report_card.add_grade(subject, grade)
        self.assertEqual({subject: [grade, grade]}, self.student_report_card.grades_by_subject)

    def test_average_grade_by_subject_no_grades(self):
        result = self.student_report_card.average_grade_by_subject()
        self.assertEqual({}, self.student_report_card.grades_by_subject)
        self.assertEqual("", result)

    def test_average_grade_by_subject_with_one_subject(self):
        subject = "Math"
        self.student_report_card.grades_by_subject = {subject: [4, 6]}
        result = self.student_report_card.average_grade_by_subject()
        self.assertEqual("Math: 5.00", result)

    def test_average_grade_by_subject_with_grades(self):
        self.student_report_card.grades_by_subject = {"Math": [4, 6], "English": [5]}
        expected_result = "Math: 5.00\nEnglish: 5.00"
        result = self.student_report_card.average_grade_by_subject()
        self.assertEqual(expected_result, result)

    def test_average_grade_for_all_subjects_returns(self):
        self.student_report_card.grades_by_subject = {"Math": [4, 6], "English": [5]}
        result = self.student_report_card.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 5.00", result)

    def test_average_grade_for_all_subjects_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            self.student_report_card.average_grade_for_all_subjects()

    def test_repr_method_returns_correctly(self):
        self.student_report_card.grades_by_subject = {"Math": [4, 6], "English": [5]}
        expected_result = f"Name: Test\nYear: 1\n"
        expected_result += f"----------\n" \
                           f"{self.student_report_card.average_grade_by_subject()}\n" \
                           f"----------\n" \
                           f"{self.student_report_card.average_grade_for_all_subjects()}"

        result = repr(self.student_report_card)
        self.assertEqual(expected_result, result)

    def test_repr_method_zero_division_error_raises(self):
        with self.assertRaises(ZeroDivisionError):
            repr(self.student_report_card)


if __name__ == '__main__':
    main()