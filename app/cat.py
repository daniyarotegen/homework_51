import random


class Cat:
    name = ""
    age = 0
    satiety = 100
    happiness = 100
    is_sleeping = False
    avatar = ""

    SLEEPING_AVATAR = "/static/images/sleeping.png"
    HAPPY_AVATAR = "/static/images/happy.png"
    SAD_AVATAR = "/static/images/sad.png"
    ANGRY_AVATAR = "/static/images/angry.png"

    @classmethod
    def feed(cls):
        if cls.is_sleeping:
            return
        cls.satiety += 15
        cls.happiness += 5
        if cls.satiety > 100:
            cls.satiety = 100
            cls.happiness -= 30
        if cls.happiness < 0:
            cls.happiness = 0

    @classmethod
    def play(cls):
        if cls.is_sleeping:
            cls.is_sleeping = False
            cls.happiness -= 5
            return
        cls.happiness += 15
        cls.satiety -= 10
        if random.randint(0, 2) == 0:
            cls.happiness = 0
        if cls.happiness < 0:
            cls.happiness = 0

    @classmethod
    def sleep(cls):
        cls.is_sleeping = True

    @classmethod
    def update_avatar(cls):
        if cls.is_sleeping:
            cls.avatar = cls.SLEEPING_AVATAR
        elif cls.happiness > 60:
            cls.avatar = cls.HAPPY_AVATAR
        elif cls.happiness > 20:
            cls.avatar = cls.SAD_AVATAR
        else:
            cls.avatar = cls.ANGRY_AVATAR
