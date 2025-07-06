from enum import Enum


class Plates(Enum):
    TWENTY_FIVE = 25
    TWENTY = 20
    FIFTEEN = 15
    TEN = 10
    FIVE = 5
    TWO_FIVE = 2.5
    TWO = 2
    ONE_FIVE = 1.5
    ONE = 1
    ZERO_FIVE = 0.5


class Equipment(Enum):
    COLLAR = 2.5

weights = [plate.value for plate in Plates]

bar_weight = 20
plate = []

class AvailablePlates:
    def __init__(self, twenty_five, twenty, fifteen, ten, five, two_five, two, one_five) -> None:
        self.twenty_five = twenty_five
        self.twenty = twenty
        self.fifteen = fifteen
        self.ten = ten
        self.five = five
        self.two_five = two_five
        self.two = two
        self.one_five = one_five

    @property
    def twenty_five(self):
        return self.twenty_five
    
    @property
    def twenty(self):
        return self.twenty
    
    @property
    def fifteen(self):
        return self.fifteen
    
    @property
    def ten(self):
        return self.ten
    
    @property
    def five(self):
        return self.five
    
    @property
    def two_five(self):
        return self.two_five
    
    @property
    def two(self):
        return self.two
    
    @property
    def one_five(self):
        return self.one_five
    
    @property.setter
    def twenty_five(self, value):
        self.twenty_five = value
    
    @property.setter
    def twenty(self, value):
        self.twenty = value
    
    @property.setter
    def fifteen(self, value):
        self.fifteen = value
    
    @property.setter
    def ten(self, value):
        self.ten = value
    
    @property.setter
    def five(self, value):
        self.five = value
    
    @property.setter
    def two_five(self, value):
        self.two_five = value
    
    @property.setter
    def two(self, value):
        self.two = value
    
    @property.setter
    def one_five(self, value):
        self.one_five = value



if __name__ == "__main__":
    twenty_five = Plates.TWENTY_FIVE.value
    collar = Equipment.COLLAR.value
    print(f"Available weights: {weights}")
    print(twenty_five)

    input = input("Enter the weight: ")
