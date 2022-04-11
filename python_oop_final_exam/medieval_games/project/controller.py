from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player):
        players_added = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                players_added.append(player.name)
        return f"Successfully added: {', '.join(players_added)}"

    def add_supply(self, *supplies: Supply):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name, sustenance_type):
        player = self.find_player_by_name(player_name)

        if player is None:
            return
        if sustenance_type not in ["Food", "Drink"]:
            return
        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        sustenance_supply = self.find_supply_by_type(sustenance_type)
        if sustenance_supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if player.stamina + sustenance_supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += sustenance_supply.energy
        return f"{player_name} sustained successfully with {sustenance_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        # first_player = self.find_player_by_name(first_player_name)
        # second_player = self.find_player_by_name(second_player_name)
        #
        # if first_player.stamina == 0 and second_player.stamina == 0:
        #     return f"Player {first_player_name} does not have enough stamina.\n" \
        #            f"Player {second_player_name} does not have enough stamina."
        # if first_player.stamina == 0:
        #     return f"Player {first_player_name} does not have enough stamina."
        # if second_player.stamina == 0:
        #     return f"Player {second_player_name} does not have enough stamina."
        #
        # first_attack = self.attack_once(first_player, second_player)
        # if first_attack:
        #     return first_attack
        # second_attack = self.attack_once(first_player, second_player)
        # if second_attack:
        #     return second_attack
        #
        # if first_player.stamina > second_player.stamina:
        #     winner_name = first_player_name
        # else:
        #     winner_name = second_player_name
        # return f"Winner: {winner_name}"

        first_player = self.find_player_by_name(first_player_name)
        second_player = self.find_player_by_name(second_player_name)

        if first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\n" \
                   f"Player {second_player_name} does not have enough stamina."
        if first_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        if second_player.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        if first_player.stamina < second_player.stamina:
            second_player_stamina = self.attack(first_player)
            if second_player.stamina - second_player_stamina <= 0:
                second_player.stamina = 0
                winner_name = first_player
                return f"Winner: {winner_name}"
            second_player.stamina -= second_player_stamina
        else:
            first_player_stamina = self.attack(second_player)
            if first_player.stamina - first_player_stamina <= 0:
                first_player.stamina = 0
                winner_name = second_player_name
                return f"Winner: {winner_name}"
            second_player.stamina -= first_player_stamina

        if first_player.stamina > second_player.stamina:
            winner_name = first_player_name
        else:
            winner_name = second_player_name
        return f"Winner: {winner_name}"

    def next_day(self):
        for player in self.players:
            player_reduce = player.stamina - player.age * 2
            if player_reduce < 0:
                player.stamina = 0
            else:
                player.stamina = player_reduce
        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ""
        for player in self.players:
            result += f"{str(player)}\n"
        result.strip()
        for supply in self.supplies:
            result += supply.details() + "\n"
        return result.strip()

    def find_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
        return

    def find_supply_by_type(self, sustenance_type):
        supply = None
        index = 0
        for i in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[i].__class__.__name__ == sustenance_type:
                supply = self.supplies[i]
                index = i
                break

        if not supply:
            return
        del self.supplies[index]
        return supply

    @staticmethod
    def attack(player):
        return player.stamina / 2

    def attack_once(self, first_player, second_player):
        if first_player.stamina < second_player.stamina:
            second_player_stamina = self.attack(first_player)
            if second_player.stamina - second_player_stamina <= 0:
                second_player.stamina = 0
                winner_name = first_player.name
                return f"Winner: {winner_name}"
            second_player.stamina -= second_player_stamina
        else:
            first_player_stamina = self.attack(second_player)
            if first_player.stamina - first_player_stamina <= 0:
                first_player.stamina = 0
                winner_name = second_player.name
                return f"Winner: {winner_name}"
            first_player.stamina -= first_player_stamina
