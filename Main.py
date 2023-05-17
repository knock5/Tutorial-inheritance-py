# Inheritance (Pewarisan)

# Membuat super class hewan
# Dalam hal ini hirarki antara class hewan sebagai parent dengan class kucing dan elang sebagai child
class Hewan:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def profil(self):
        print("Hi! Saya", self.name, "umur saya", self.age, "dan saya berwarna", self.color)


# Membuat class
class Ability:
    def __init__(self, power, defend):
        self.power = power
        self.defend = defend

    def attack(self):
        print('Menyerang dengan power :', self.power)

    def defence(self):
        print('Bertahan dengan defend :', self.defend)


# Membuat class
class Behavior:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, 'sedang makan...')

    def drink(self):
        print(self.name, 'sedang minum...')


# Membuat child class dengan parent hewan (Pewarisan Tunggal)
class Kucing(Hewan):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    def suara(self):
        print("Meow!")

    def berlari(self):
        print(self.name, "sedang berlari...")


# Membuat child class dengan parent hewan
class Elang(Hewan):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    def terbang(self):
        print(self.name, "sedang terbang...")


# Membuat child class dengan parent behavior
class Kuda(Behavior):
    def __init__(self, name):
        super().__init__(name)


# Pewarisan multi level
class Macan(Kucing):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)


# Pewarisan multiple : langsung merujuk pada parent
class Singa(Hewan, Ability):
    def __init__(self, name, age, color, attack, defend):
        super().__init__(name, age, color)
        super(Hewan, self).__init__(attack, defend)


# Pewarisan multi-path
class Badak(Kucing, Kuda):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)


# Pewarisan hybrid : penggabungan dari fitur pewarisan single, multiple, atau multi-path
class Rusa(Hewan, Kuda):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    def jump(self):
        print(self.name, 'sedang melompat...')


