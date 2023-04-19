from task_11 import Desert


class JellyBean(Desert):
    @property
    def flavor(self):
        return self.flavor

    @flavor.setter
    def flavor(self, value):
        self.flavor = value

    def is_dilicious(self):
        if self.flavor == "black licorice":
            return False

