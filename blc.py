from enum import Enum


class WeightPlates(Enum):
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

weights = [plate.value for plate in WeightPlates]

bar_weight = 20
plate = []




if __name__ == "__main__":
    twenty_five = WeightPlates.TWENTY_FIVE.value
    collar = Equipment.COLLAR.value
    # print(f"25kg plate width: {WeightPlates.TWENTY_FIVE.value.width}")
    print(f"Available weights: {weights}")
    print(twenty_five)
