from project.team import Team
from unittest import TestCase, main


class TeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team("Test")
        self.other_team = Team("TeamA")

    def test_object_initialized_correctly(self):
        name = "Test"
        team = Team(name)
        self.assertEqual(name, team.name)
        self.assertEqual({}, team.members)

    def test_name_setter_raises_numbers_only(self):
        with self.assertRaises(ValueError) as ex:
            team = Team("12")
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_name_setter_raises_numbers_and_letters(self):
        with self.assertRaises(ValueError) as ex:
            team = Team("12as")
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_remove_member_that_doesnt_exist(self):
        result = self.team.remove_member("Ivan")
        self.assertEqual(f"Member with name Ivan does not exist", result)
        self.assertEqual({}, self.team.members)

    def test_remove_member_that_exists(self):
        self.team.members = {
            "Ivan": 23,
            "Pavel": 15
        }
        result = self.team.remove_member("Ivan")
        self.assertEqual(f"Member Ivan removed", result)
        self.assertEqual({"Pavel": 15}, self.team.members)

    def test_team_str_returns_correct_string_empty_members(self):
        result = f"Team name: {self.team.name}"

        self.assertEqual(result, str(self.team))

    def test_team_str_returns_correct_string_with_members(self):
        self.team.members = {
            "Ivan": 23,
            "Pavel": 15
        }
        result = [f"Team name: {self.team.name}"]
        members = list(sorted(self.team.members.items(), key=lambda x: (-x[1], x[0])))
        result.extend([f"Member: {x[0]} - {x[1]}-years old" for x in members])
        result = "\n".join(result)
        self.assertEqual(result, str(self.team))

    def test_team_dunder_len_returns_correct(self):
        self.team.members = {
            "Ivan": 23,
            "Pavel": 15
        }
        result = len(self.team)
        self.assertEqual(2, result)

    def test_len_method_zero_length(self):
        result = len(self.team.members)
        self.assertEqual(0, result)

    def test_team_greater_method_equal_lengths(self):
        result = self.team > self.other_team
        self.assertEqual(False, result)

    def test_team_greater_method_self_longer_lengths(self):
        other_team = Team("TeamA")
        self.team.members = {
            "Ivan": 23,
            "Pavel": 15
        }

        result = self.team > other_team
        self.assertEqual(True, result)

    def test_team_greater_method_other_longer_lengths(self):
        self.other_team.members = {
            "Ivan": 23,
            "Pavel": 15
        }

        result = self.team > self.other_team
        self.assertEqual(False, result)

    def test_add_member_new_member_data(self):
        added_members_by_name = ["Ivan", "Pavel"]
        result = self.team.add_member(Ivan=14, Pavel=34)
        self.assertEqual(f"Successfully added: {', '.join(added_members_by_name)}", result)

        expected_members = {
            "Ivan": 14,
            "Pavel": 34
        }
        self.assertEqual(expected_members, self.team.members)

    def test_add_member_semi_new_member_data(self):
        self.team.members = {"Ivan": 14}

        added_members_by_name = ["Pavel"]
        result = self.team.add_member(Ivan=14, Pavel=34)
        self.assertEqual(f"Successfully added: {', '.join(added_members_by_name)}", result)

        expected_members = {
            "Ivan": 14,
            "Pavel": 34
        }
        self.assertEqual(expected_members, self.team.members)

    def test_add_member_with_no_new_data(self):
        expected_members = {
            "Ivan": 23,
            "Pavel": 15
        }
        self.team.members = expected_members
        result = self.team.add_member(Ivan=14, Pavel=34)
        self.assertEqual(f"Successfully added: ", result)
        self.assertEqual(expected_members, self.team.members)

    def test_add_dunder_method_with_empty_members(self):
        new_team = self.team + self.other_team
        self.assertEqual("TestTeamA", new_team.name)
        self.assertEqual({}, new_team.members)

    def test_add_dunder_method_with_repeating_members(self):
        expected_members = {
            "Ivan": 14,
            "Pavel": 34
        }
        self.team.members = expected_members
        self.other_team.members = expected_members
        new_team = self.team + self.other_team
        self.assertEqual("TestTeamA", new_team.name)
        self.assertEqual(expected_members, new_team.members)

    def test_add_method_empty_other_team(self):
        expected_members = {
            "Ivan": 14,
            "Pavel": 34
        }
        self.team.members = expected_members
        new_team = self.team + self.other_team
        self.assertEqual("TestTeamA", new_team.name)
        self.assertEqual(expected_members, new_team.members)

    def test_add_method_empty_self_team(self):
        expected_members = {
            "Ivan": 14,
            "Pavel": 34
        }
        self.other_team.members = expected_members
        new_team = self.team + self.other_team
        self.assertEqual("TestTeamA", new_team.name)
        self.assertEqual(expected_members, new_team.members)

    def test_add_method_with_different_data(self):
        team1_members = {"Berrin": 45, "Nelin": 18}
        self.team.members = team1_members

        team2_members = {"Melek": 16}
        self.other_team.members = team2_members
        new_team = self.team + self.other_team
        self.assertEqual("TestTeamA", new_team.name)

        expected_members = {"Berrin": 45, "Nelin": 18, "Melek": 16}
        self.assertEqual(expected_members, new_team.members)


if __name__ == '__main__':
    main()