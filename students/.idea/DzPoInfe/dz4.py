from abc import ABC, abstractmethod
import random
class Pavuki(ABC):
    def move(self):
        print(f'Run away {self.__class__.__name__} come closer')

    def bite(self, colgl, choice):
        if colgl != 4 and choice != 2:
            dmg = random.randint(1, 1000)
            if dmg >500:
                print(f'{self.__class__.__name__} spider bite you with the poison')
            elif dmg < 500:
                print(f'{self.__class__.__name__} spider bite you')
            elif dmg == 500:
                print(f'{self.__class__.__name__} spider bite you. And now you become a Spiderman!!!!')
        elif colgl == 4 and choice == 2:
            dmg = random.randint(1, 10)
            if dmg > 5:
                print(f'{self.__class__.__name__} spider bite you with the poison')
            elif dmg < 5:
                print(f'{self.__class__.__name__} spider bite you')
            elif dmg == 5:
                print(f'{self.__class__.__name__} spider bite you. And now you become a Spiderman!!!!')
        elif colgl == 4 or choice == 2:
            dmg = random.randint(1, 100)
            if dmg > 50:
                print(f'{self.__class__.__name__} spider bite you with the poison')
            elif dmg < 50:
                print(f'{self.__class__.__name__} spider bite you')
            elif dmg == 50:
                print(f'{self.__class__.__name__} spider bite you. And now you become a Spiderman!!!!')


    def __init__(self, colgl):
        self.colgl = colgl
        if colgl != 1 and colgl != 2 and colgl != 3 and colgl != 4:
            quit()

    def glaza(self):
        print(f'{self.__class__.__name__} has {self.colgl} eyes')

    @abstractmethod
    def web(self):
        raise Exception

    @abstractmethod
    def racion(self):
        raise Exception


class WaterPavuk(Pavuki):
    def _dive(self):
        d = random.randint(1,3)
        if d == 1:
            print(f'{self.__class__.__name__} swimming')
        elif d == 2:
            print(f'{self.__class__.__name__} dive deep')
        elif d == 3:
            print(f'{self.__class__.__name__} utonul game over :^(')
            quit()
    def racion(self):
        print(f'{self.__class__.__name__} love to eat mini-heads')
    def web(self):
        print(f'Intresting fact, {self.__class__.__name__} use web to catch mini-heads')


class Bespavutinnie(Pavuki, ABC):
    def jump(self):
        d = random.randint(1, 3)
        if d == 1:
            print(f'{self.__class__.__name__} jump and land succesfully')
        elif d == 2:
            print(f'{self.__class__.__name__} jump high and ele ele survive')
        elif d == 3:
            print(f'{self.__class__.__name__} razbilsa game over :^(')
            quit()


class Small(Bespavutinnie):
    def racion(self):
        print(f'{self.__class__.__name__} love to eat insects')

    def web(self):
        print(f'Intresting fact, {self.__class__.__name__} spiders jump on victim and suffocating it')


class Big(Bespavutinnie):
    def racion(self):
        print(f'{self.__class__.__name__} pavuk love to eat birds')

    def web(self):
        print(f'Intresting fact, {self.__class__.__name__} spiders jump on victim with a ready - made web and kill it')
class Kochevnik(Bespavutinnie):
    def racion(self):
        print(f'spider {self.__class__.__name__} eats everything that crawls on the ground')

    def web(self):
        print(f'Intresting fact, spider {self.__class__.__name__} says "reznya", jumps out of hiding and attacks the victim  ')
class Masking(Bespavutinnie):
    def masq(self):
        d = random.randint(1, 3)
        if d == 1:
            print(f'{self.__class__.__name__} disguised succesfully')
        elif d == 2:
            print(f'{self.__class__.__name__}  disguised very good, it is almost invisible')
        elif d == 3:
            print(f'{self.__class__.__name__} disquised so good that we poteryali ego.\nGame over :^(')
            quit()
    def racion(self):
        print(f'spider {self.__class__.__name__} eats insects')

    def web(self):
        print(f'Intresting fact, {self.__class__.__name__} spider dont use web he masquerades as ants. Kruto!')


print('choose your pavuk:\n1.Water Pavuk\n2.Small Pavuk\n3.Big Pavuk\n4.Pavuk Kochevnik\n5.Masking Pavuk')
choice = int(input())
print('choose nuber of eyes:\n1. 2 eyes\n2. 4 eyes\n3. 6 eyes\n4. 8 eyes')
colgl = int(input())
if choice == 1:
    print('Now you have a Water Pavuk')
    wpavuk = WaterPavuk(colgl)
    wpavuk.move()
    wpavuk.web()
    print('what you will do?\n1.bite\n2.move\n3.get info about racion\n4.Dive in water')
elif choice == 2:
    print('Now you have a Small Pavuk')
    spavuk = Small(colgl)
    spavuk.move()
    spavuk.web()
    print('what your spider will do?\n1.bite\n2.move\n3.get info about racion\n4.Jump')
elif choice == 3:
    print('Now you have a Big Pavuk')
    bipavuk = Big(colgl)
    bipavuk.move()
    bipavuk.web()
    print('what your spider will do?\n1.bite\n2.move\n3.get info about racion\n4.Jump')
elif choice == 4:
    print('Now you have a Pavuk Kochevnik')
    kpavuk = Kochevnik(colgl)
    kpavuk.move()
    kpavuk.web()
    print('what your spider will do?\n1.bite\n2.move\n3.get info about racion\n4.Jump')
elif choice == 5:
    print('Now your have a Masking Pavuk')
    mpavuk = Masking(colgl)
    mpavuk.move()
    mpavuk.web()
    print('what your spider will do?\n1.bite\n2.move\n3.get info about racion\n4.disguise')
v = int(input())
if v == 1 and choice == 1:
    wpavuk.bite(colgl, choice)
elif v == 2 and choice == 1:
    wpavuk.move()
elif v == 3 and choice == 1:
    wpavuk.racion()
elif v == 4 and choice == 1:
    wpavuk._dive()
elif v == 1 and choice == 2:
    spavuk.bite(colgl, choice)
elif v == 2 and choice == 2:
    spavuk.move()
elif v == 3 and choice == 2:
    spavuk.racion()
elif v == 4 and choice == 2:
    spavuk.jump()
elif v == 1 and choice == 3:
    bipavuk.bite(colgl, choice)
elif v == 2 and choice == 3:
    bipavuk.move()
elif v == 3 and choice == 3:
    bipavuk.racion()
elif v == 4 and choice == 3:
    bipavuk.jump()
elif v == 1 and choice == 4:
    kpavuk.bite(colgl, choice)
elif v == 2 and choice == 4:
    kpavuk.move()
elif v == 3 and choice == 4:
    kpavuk.racion()
elif v == 4 and choice == 4:
    kpavuk.jump()
elif v == 1 and choice == 5:
    mpavuk.bite(colgl, choice)
elif v == 2 and choice == 5:
    mpavuk.move()
elif v == 3 and choice == 5:
    mpavuk.racion()
elif v == 4 and choice == 5:
    mpavuk.masq()