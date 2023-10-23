import loader


class Font:
    def __init__(self, name):
        self.name = name
        self.cache = {}

    def retrieve(self, variant, size):
        if (variant, size) not in self.cache.keys():
            self.cache[(variant, size)] = (loader.load_font(f"{self.name}-{variant.capitalize()}", size), size)

        return self.cache[(variant, size)]

RobotoSlab = Font("RobotoSlab")