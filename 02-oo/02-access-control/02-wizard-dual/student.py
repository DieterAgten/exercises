class Wizard:
    def __init__(self, name):
        self.__mana = 45
        self.__health = 65
        self.name = name

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health

    def get_fireballed(self):
        self.__health -= 30
        return(self.__health)

    def drink_mana_potion(self):
        self.__mana += 40
        return(self.__mana)