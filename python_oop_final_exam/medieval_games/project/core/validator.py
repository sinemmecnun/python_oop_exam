class Validator:
    @staticmethod
    def raise_if_two_players_with_same_name(name, player_names, message):
        if name in player_names:
            raise Exception(message)