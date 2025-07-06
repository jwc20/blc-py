from enum import Enum
from collections import namedtuple


Plate = namedtuple("Plate", ["name", "weight", "quantity"])


class PlateAvailable:
    plate_weights = [
        ("twenty_five", 25),
        ("twenty", 20),
        ("fifteen", 15),
        ("ten", 10),
        ("five", 5),
        ("two_five", 2.5),
        ("two", 2),
        ("one_five", 1.5),
        ("one", 1),
        ("zero_five", 0.5),
        ("collar", 2.5),
    ]

    def __init__(self) -> None:
        self.plates = [Plate(name, weight, 4) for name, weight in self.plate_weights]

    def __iter__(self):
        return iter(self.plates)

    def __repr__(self):
        return str(
            [(plate.name, plate.weight, plate.quantity) for plate in self.plates]
        )

    def add_plate(self, name, quantity):
        for plate in self.plates:
            if plate.name == name:
                plate.quantity += quantity
                return
        raise ValueError(f"Plate {name} not found")
        return

    def remove_plate(self, name, quantity):
        for plate in self.plates:
            if plate.name == name:
                plate.quantity -= quantity
                if plate.quantity == 0:
                    self.plates.remove(plate)
                return
        raise ValueError(f"Plate {name} not found")
        return

if __name__ == "__main__":
    plates = PlateAvailable()
    # print([(plate.name, plate.weight, plate.quantity) for plate in plates])
    print(repr(plates))
