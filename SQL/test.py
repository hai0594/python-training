class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name  = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        Pokemon.attack += self.attack_boost

    def defense_up(self):
        Pokemon.defense += self.defense_boost

    def health_up(self):
        Pokemon.health += self.health_boost

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}\r\nAttack: {}, Defense: {}, Health: {}".format(self.name, self.p_type, self.level, self.attack, self.defense, self.health)
    
pokemon = Pokemon('Alomomola', 9)
print(pokemon)
print('------')
print('Traning: ', pokemon.train())
print('------')
print(pokemon)

class Grass_Pokemon(Pokemon):
    attack = 15 
    defense = 14 
    health = 12 
    p_type = "Grass"

    def attack_up(self):
        Pokemon.attack += self.attack_boost

    def defense_up(self):
        Pokemon.defense += self.defense_boost

    def health_up(self):
        Pokemon.health += self.health_boost

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def __init__(self, name,level = 5):
        [...]
        self.weak = "Dark"
        self.strong = "Psychic"

    def train(self):
        [...]

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return self.name + " knows a lot of different moves!"
    

class Ghost_Pokemon(Pokemon):
    p_type = "Ghost" 
    weak = "Dark" 
    strong = "Psychic"

class Fire_Pokemon(Pokemon):
    p_type = "Fire"
    weak = "Water"
    strong = "Grass"  

class Flying_Pokemon(Pokemon):
    p_type = "Flying"
    weak = "Electric"
    strong = "Fighting"

print(Ghost_Pokemon('Cofagrigus', 10))
print(Fire_Pokemon('Reshiram', 12))
print(Ghost_Pokemon('Zapdos', 9))