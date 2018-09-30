# Netology, assignment 5 


class Animal:
    animals = dict()
    all_animals = list()

    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
        self.fed = False
        self.voice = 'Hmm'
        self.subclass = 'Mammal'
        self.collect = False
        self.animals[self.name] = self.weight
        self.all_animals.append(self)

    def __str__(self):
        return self.name

    def feed(self):
        self.fed = True
        print(f'{self.name} is now fed.')

    def speak(self):
        print(f'{self.name} says: {self.voice}')

    def collect_from(self):
        self.collect = True


class Mammal(Animal):

    def collect_from(self):
        self.collect = True
        print(f'{self.name} is now milked.')


class Bird(Animal):

    def __init__(self, name, color, weight):
        super().__init__(name, color, weight)
        self.subclass = 'Bird'

    def collect_from(self):
        self.collect = True
        print(f'Eggs are collected from {self.name}.')


class Goose(Bird):

    def __init__(self, name, color, weight):
        super().__init__(name, color, weight)
        self.voice = "Honk-honk"


class Duck(Bird):

    def __init__(self, name, color, weight):
        super().__init__(name, color, weight)
        self.voice = 'Quack-quack'


class Chicken(Bird):

    def __init__(self, name, color, weight):
        super().__init__(name, color, weight)
        self.voice = 'Cluck-cluck'


class Cow(Mammal):

    def __init__(self, name, color, weight):
        super().__init__(name, color, weight)
        self.voice = 'Moo-moo'


class Sheep(Mammal):

    def __init__(self, name, color, weight):
        super().__init__(name, color, weight)
        self.voice = 'Baa-baa'

    def collect_from(self):
        self.collect = True
        print(f'{self.name} is now milked.')
        print(f'{self.name} is now fleeced.')


class Goat(Mammal):

    def __init__(self, name, color, weight):
        super().__init__(name, color, weight)
        self.voice = 'Maa-maa'

    def collect_from(self):
        self.collect = True
        print(f'{self.name} is now milked.')
        print(f'{self.name} is now fleeced.')


goose_1 = Goose('Grey', 'grey', 3)
goose_2 = Goose('White', 'white', 4)
chicken_1 = Chicken('Co-Co', 'white', 2)
chicken_2 = Chicken('Coo-Ka-Re-Coo', 'brownish', 3)
duck_1 = Duck('Quryackwa', 'grey', 2)
cow_1 = Cow('Manka', 'brown', 450)
sheep_1 = Sheep('Barashek', 'milky', 100)
sheep_2 = Sheep('Quodryawy', 'milky', 87)
goat_1 = Goat('Horn', 'black', 64)
goat_2 = Goat('Hoof', 'grey', 77)

for animal in Animal.all_animals:
    animal.feed()
    animal.speak()
    animal.collect_from()

winner = None
sum_weight = 0
max_weight = 0

for name, weight in Animal.animals.items():
    sum_weight += weight
    if weight > max_weight:
        max_weight = weight
        winner = name

print(f'Total weight of all farm animals: {sum_weight}')
print(f'The heaviest animal on the farm is {winner}')
