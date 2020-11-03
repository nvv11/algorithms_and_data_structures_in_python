from collections import namedtuple


hero_1 = ('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_1[4])


class Person:

    def __init__(self, name, race, health, mana, strenght):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.strenght = strenght


hero_2 = Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_2.mana)


new_person = namedtuple('new_person', 'name, race, health, mana, strenght')
hero_3 = new_person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_3.race)

prop = ['name', 'race', 'health', 'mana', 'strenght']
new_person_1 = namedtuple('new_person_1', prop, rename=True)
hero_4 = new_person_1('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_4.race)

print('*' * 50)
Point = namedtuple('Point', 'x, y, z')
p1 = Point(2, z=3, y=4)
print(p1)

t = [5, 10, 15]
p2 = Point._make(t)
print(p2)

d2 = p2._asdict()
print(d2)

p3 = p2._replace(x=6)
print(p3)

print(p3._fields)

print('*' * 50)
new_point = namedtuple('new_point', 'x, y, z', defaults=[0, 0])
p4 = new_point(5)
print(p4)
print(p4._fields_defaults)

dct = {'x': 10, 'y': 20, 'z': 30}
p5 = new_point(**dct)
print(p5)
