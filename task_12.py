from task_11 import Dessert


class JellyBean(Dessert):

    def __init__(self, flavor=None):
        self.flavor = flavor
        super().__init__()

    @property
    def flavor(self):
        return self.flavor

    @flavor.setter
    def flavor(self, value):
        self.flavor = value

    def is_delicious(self):
        if self.flavor == "black licorice":
            return False
