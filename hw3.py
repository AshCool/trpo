from abc import ABCMeta, abstractclassmethod

"""
Ресивер - герой

Команды - удар, защита, заклинание, отступление.

Клиент - игрок.

Инвокер -  ̶и̶м̶б̶а̶ инвокер.

"""


class Log:

    def __init__(self):

        self.attacksCount = 0
        self.defendsCount = 0
        self.spellsCount = 0
        self.retreatsCount = 0


# receiver


class Hero:

    def __init__(self, name, age):

        self.name = name
        self.age = age


# commands

class Command(metaclass=ABCMeta):

    def __init__(self, hero: Hero, log: Log):

        self.hero = hero
        self.log = log

    @abstractclassmethod
    def execute(self):

        raise NotImplementedError()

    @abstractclassmethod
    def undo(self):

        raise NotImplementedError()


class Attack(Command):

    def execute(self):

        if self.hero.age > 60:
            print("Aren't you a bit too old to swing that sword around here, granpa?\n")
        else:
            print("{0} aimlessly swings his sword.\n".format(self.hero.name))
        self.log.attacksCount += 1

    def undo(self):

        if self.log.attacksCount == 0:
            print("{0} hasn't attacked yet. Pathetic.\n".format(self.hero.name))
        else:
            print("{0} tried to unswing his sword resulting in more swings.\n".format(self.hero.name))
            self.log.attacksCount -= 1


class Defend(Command):

    def execute(self):

        print("{0} raised his shield. No one cares.\n".format(self.hero.name))
        self.log.defendsCount += 1

    def undo(self):

        if self.log.defendsCount == 0:
            print("{0} hasn't defend yet and probably should.\n".format(self.hero.name))
        else:
            print("{0} lowered his shield. Still, no one cares.\n".format(self.hero.name))
            self.log.defendsCount -= 1


class Spell(Command):

    def execute(self):

        print("{0} miserably failed, trying to show card focus.\n".format(self.hero.name))
        self.log.spellsCount += 1

    def undo(self):

        if self.log.spellsCount == 0:
            print("Maybe try to cast something first, huh?")
        else:
            print("Stop, {0}, you are making it worse.\n".format(self.hero.name))
            self.log.spellsCount -= 1


class Retreat(Command):

    def execute(self):

        if self.log.retreatsCount == 1:
            print("You can't retreat twice!")
        else:
            print("Yeah, There you go.\n")
            self.log.retreatsCount += 1

    def undo(self):

        if self.log.retreatsCount == 0:
            print("{0} never did that.\n".format(self.hero.name))
        else:
            print("Yeah, back to battle. Whatever.\n".format(self.hero.name))
            self.log.retreatsCount -= 1


# invoker

class Invoker:

    def invoke(self, command: Command):

        command.execute()

    def undo(self, command: Command):

        command.undo()


class SessionClosed(Exception):

    def __init__(self, value):

        self.value = value


# client

if __name__ == "__main__":

    invoker = Invoker()
    log = Log()

    name = input("Name yourself, hero. ")

    while True:

        age = input("Age yourself, hero. ")

        try:

            age = int(age)

        except ValueError:

            print("You do know what number are, right? Let's try again.\n")
            continue

        break

    hero = Hero(name, age)

    ACTIONS = {"attack": Attack(hero, log), "defend": Defend(hero, log), "spell": Spell(hero, log), "retreat": Retreat(hero, log)}

    print("Well, you can ATTACK, DEFEND, SPELL, and RETREAT. Also, you can UNDO all of it. Do your things now.\n")

    try:

        while True:

            action = input().lower().split(" ")

            try:

                if len(action) == 1:
                    command = ACTIONS[action[0]]
                    invoker.invoke(command)
                else:
                    if action[0] != "undo":
                        raise KeyError
                    command = ACTIONS[action[1]]
                    invoker.undo(command)

            except KeyError:

                print("What are you trying to do?")

    except SessionClosed as e:

        print(e.value)
        print(log.attacksCount)

# 98 lines of code
