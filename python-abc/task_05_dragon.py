#!/usr/bin/env python3

# Mixin class for swimming
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# Mixin class for flying
class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Dragon class that combines both behaviors
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

