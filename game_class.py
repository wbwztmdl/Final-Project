'''
some game classes
1. skill
2. pokemon
3. player
'''


class Skill:
    def __init__(self, name, attack_type, consume_mp, attack_rate):
        self.name = name
        self.attack_type = attack_type
        self.consume_mp = consume_mp
        self.attack_rate = attack_rate

    def activate(self, pokemon, pokemon_attacked):
        if pokemon.current_mp != '∞':
            if pokemon.current_mp - self.consume_mp < 0:
                print("Don't have enough mp!")
                return False
            else:
                pokemon.current_mp -= self.consume_mp

        if self.attack_type == 'physic':
            damage = self.attack_rate * pokemon.attack - pokemon_attacked.defence
            if damage < 0:
                damage = 0

            pokemon_attacked.current_hp = pokemon_attacked.current_hp - damage
            if pokemon_attacked.current_hp < 0:
                pokemon_attacked.current_hp = 0
        elif self.attack_type == 'magic':
            damage = self.attack_rate * pokemon.attack * (1 - pokemon_attacked.spell_resistance)
            pokemon_attacked.current_hp = pokemon_attacked.current_hp - damage
            if pokemon_attacked.current_hp < 0:
                pokemon_attacked.current_hp = 0

        if pokemon_attacked.current_hp == 0:
            print(
                f"{pokemon.name} uses {self.name} to deal {damage} {self.attack_type} damage to {pokemon_attacked.name}, and {pokemon_attacked.name} has been defeated!")
        else:
            print(
                f"{pokemon.name} uses {self.name} to deal {damage} {self.attack_type} damage to {pokemon_attacked.name}, and {pokemon_attacked.name} has {pokemon_attacked.current_hp} HP left")
        return True

    def __str__(self):
        return f'''Skill name: {self.name}
Attack_type: {self.attack_type}
Consume_mp: {self.consume_mp}
Attack_rate: {self.attack_rate}'''


# initial skill: crash
crash = Skill('crash', 'physic', 0, 1)


class Pokemon:
    def __init__(self, name, pokemon_type, level, hp, mp, attack, defence, spell_resistance):
        self.name = name
        self.pokemon_type = pokemon_type
        self.level = level
        self.max_hp = hp
        self.current_hp = hp
        self.max_mp = mp
        self.current_mp = mp
        self.attack = attack
        self.defence = defence
        self.spell_resistance = spell_resistance
        self.skills = [crash]

    def level_up(self, attribute):
        self.level += 1

        if self.current_mp != '∞':
            self.max_mp += 1
            self.current_mp += 1

        if attribute == 'hp':
            self.max_hp += 15
            self.current_hp += 15
        elif attribute == 'attack':
            self.attack += 10
        elif attribute == 'defence':
            self.defence += 20
        elif attribute == 'spell_resistance':
            self.spell_resistance = round(self.spell_resistance * 0.9 + 0.1, 2)

    def min_consume_mp(self):
        min_consume_mp = self.skills[0].consume_mp
        for i in self.skills:
            if min_consume_mp > i.consume_mp:
                min_consume_mp = i.consume_mp

        return min_consume_mp

    def can_fight(self):
        if self.current_hp == 0:
            return False
        else:
            return True

    def __str__(self):
        str_print = f'''Name: {self.name}
Pokemon_type: {self.pokemon_type}
Level: {self.level}
HP: {self.current_hp}/{self.max_hp}
MP: {self.current_mp}/{self.max_mp}
Attack: {self.attack}
Defence: {self.defence}
Spell_resistance: {self.spell_resistance}\n'''
        str_print += ">>> SKILLS:\n"
        for i in range(len(self.skills)):
            str_print = str_print + f'{i + 1}: ' + self.skills[i].__str__() + '\n\n'
        return str_print[:-1]


class Player:
    def __init__(self, name):
        self.name = name
        self.money = 5000
        self.pokemons = []
        self.energy = 5

    def __str__(self):
        return f'Name: {self.name}  Money: {self.money}  Energy: {self.energy}'

    def add_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def is_energy_enough(self, reduce_energy):
        if self.energy - reduce_energy < 0:
            print("You are too tired!Go to sleep!")
            return False
        else:
            return True

    def reduce_energy(self, reduce_energy):
        if self.is_energy_enough(reduce_energy):
            self.energy -= reduce_energy
            return True
        else:
            return False

    def check_pokemons(self):
        for i in range(len(self.pokemons)):
            print(
                f"{i + 1}: {self.pokemons[i].name}  level: {self.pokemons[i].level}  HP: {self.pokemons[i].current_hp}  MP: {self.pokemons[i].current_mp}")
        while True:
            command = input('choose one for further information or exit <{index}|exit>: ').lower()
            if command == 'exit':
                break
            elif not command.isdecimal():
                print("Input Error!")
            elif int(command) - 1 in range(len(self.pokemons)):
                print(self.pokemons[int(command) - 1])
            else:
                print("Out of range")

    def can_fight(self):
        count = 0
        for i in self.pokemons:
            count += i.current_hp
        if count == 0:
            return False
        else:
            return True

