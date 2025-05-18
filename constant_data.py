import game_class

command_dict = {'exit game': 'exit the game',
                'check player': 'check the information of player',
                'check pokemons': 'check the information of pokemons that the player owned',
                'hang out': 'hanging out to enounter wild pokemons',
                'work': 'work to earn money',
                'treat pokemons': 'go to pokemon centre to threat your pokemons',
                'sleep': 'sleep until next day and recover all energy',
                'check boss': 'check the information of boss',
                'challenge boss': 'challenge the boss in advance, cost 2 enegy',
                'show commands': 'show the command list'}

# pokemon Attributes that can be level_up
attributes = ['hp', 'attack', 'defence', 'spell_resistance']

# initial pokemons
pikachu = game_class.Pokemon('pikachu', 'pikachu', 1, 270, 5, 120, 60, 0.4)
squirtle = game_class.Pokemon('squirtle', 'squirtle', 1, 330, 5, 90, 80, 0.6)
bulbasaur = game_class.Pokemon('bulbasaur', 'bulbasaur', 1, 300, 5, 100, 80, 0.4)
charmander = game_class.Pokemon('charmander', 'charmander', 1, 300, 5, 100, 60, 0.6)
initial_pokemons = [pikachu, squirtle, bulbasaur, charmander]

# several skills for pikachu
thunder = game_class.Skill('thunder', 'magic', 1, 1.5)
zippy_zap = game_class.Skill('zippy_zap', 'physic', 1, 1.5)
volt_tackle = game_class.Skill('volt_tackle', 'physic', 2, 2.5)
electro_web = game_class.Skill('electro_web', 'magic', 2, 2.5)
thunderbolt = game_class.Skill('thunderbolt', 'magic', 3, 4)
floaty_fall = game_class.Skill('floaty_fall', 'physic', 3, 4)

pikachu_low = [thunder, zippy_zap]
pikachu_medium = [thunder, zippy_zap, volt_tackle, electro_web]
pikachu_high = [thunder, zippy_zap, volt_tackle, electro_web, thunderbolt, floaty_fall]

# several skills for squirtle
bubble = game_class.Skill('bubble', 'magic', 1, 1.5)
bite = game_class.Skill('bite', 'physic', 1, 1.5)
rapid_spin = game_class.Skill('rapid_spin', 'physic', 2, 2.5)
water_gun = game_class.Skill('water_gun', 'magic', 2, 2.5)
hydro_pump = game_class.Skill('hydro_pump', 'magic', 3, 4)
skull_bash = game_class.Skill('skull_bash', 'physic', 3, 4)

squirtle_low = [bubble, bite]
squirtle_medium = [bubble, bite, rapid_spin, water_gun]
squirtle_high = [bubble, bite, rapid_spin, water_gun, hydro_pump, skull_bash]

# several skills for bulbasaur
leech_seed = game_class.Skill('leech_seed', 'magic', 1, 1.5)
tackle = game_class.Skill('tackle', 'physic', 1, 1.5)
vine_whip = game_class.Skill('vine_whip', 'physic', 2, 2.5)
poison_powder = game_class.Skill('poison_powder', 'magic', 2, 2.5)
solar_beam = game_class.Skill('solar_beam', 'magic', 3, 4)
razor_leaf = game_class.Skill('razor_leaf', 'physic', 3, 4)

bulbasaur_low = [leech_seed, tackle]
bulbasaur_medium = [leech_seed, tackle, vine_whip, poison_powder]
bulbasaur_high = [leech_seed, tackle, vine_whip, poison_powder, solar_beam, razor_leaf]

# several skills for charmander
ember = game_class.Skill('ember', 'magic', 1, 1.5)
scratch = game_class.Skill('scratch', 'physic', 1, 1.5)
metal_claw = game_class.Skill('metal_claw', 'physic', 2, 2.5)
flamethrower = game_class.Skill('flamethrower', 'magic', 2, 2.5)
fire_blast = game_class.Skill('fire_blast', 'magic', 3, 4)
swords_dance = game_class.Skill('swords_dance', 'physic', 3, 4)

charmander_low = [ember, scratch]
charmander_medium = [ember, scratch, metal_claw, flamethrower]
charmander_high = [ember, scratch, metal_claw, flamethrower, fire_blast, swords_dance]

# define a dictionary to store skills
skill_dict = {'pikachu': [pikachu_low, pikachu_medium, pikachu_high],
              'squirtle': [squirtle_low, squirtle_medium, squirtle_high],
              'bulbasaur': [bulbasaur_low, bulbasaur_medium, bulbasaur_high],
              'charmander': [charmander_low, charmander_medium, charmander_high]}

# Boss mewtwo
mewtwo = game_class.Pokemon('mewtwo', 'mewtwo', 10, 400, '∞', 150, 100, 0.7)
mewtwo.skills.pop()
turbo_strike = game_class.Skill('turbo_strike', 'physic', 2, 2.5)
psystrike = game_class.Skill('psystrike', 'magic', 2, 2.5)
ice_beam = game_class.Skill('ice_beam', 'magic', 3, 4)
hyper_beam = game_class.Skill('hyper_beam', 'magic', 4, 5)
mewtwo.skills.append(turbo_strike)
mewtwo.skills.append(psystrike)
mewtwo.skills.append(ice_beam)
mewtwo.skills.append(hyper_beam)

# Boss onix
onix = game_class.Pokemon('onix', 'onix', 10, 500, '∞', 120, 250, 0.3)
onix.skills.pop()
dragon_pulse = game_class.Skill('dragon_pulse', 'magic', 2, 2.5)
rock_throw = game_class.Skill('rock_throw', 'physic', 2, 2.5)
iron_tail = game_class.Skill('iron_tail', 'physic', 3, 4)
earthquake = game_class.Skill('earthquake', 'physic', 3, 5)
onix.skills.append(dragon_pulse)
onix.skills.append(rock_throw)
onix.skills.append(iron_tail)
onix.skills.append(earthquake)
