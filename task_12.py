from task_11 import Dessert


class JellyBean(Dessert):

    def __init__(self, flavor=None, name=None, calories=None):
        self._flavor = flavor
        super().__init__(name=name, calories=calories)

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def is_delicious(self):
        if str(self.flavor) == "black licorice":
            return False
        else:
            return True


