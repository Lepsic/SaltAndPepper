class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

    def is_healthy(self):
        if self.calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
        return True

    @property
    def name(self):
        return self._name

    @property
    def calories(self):
        return self._calories

    @name.setter
    def name(self, name):
        self._name = name

    @calories.setter
    def calories(self, calories):
        self._calories = calories





