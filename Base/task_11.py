class Desert:
    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    def is_healthy(self):
        if self.calories < 200:
            return True
        else:
            return False

    def is_dilicious(self):
        return True

    @property
    def name(self):
        return self.name

    @property
    def calories(self):
        return self.calories

    @name.setter
    def name(self, value):
        self._name = value

    @calories.setter
    def calories(self, value):
        self.calories = value

