from collections import defaultdict


class Plates:
    weights = [25, 20, 15, 10, 5, 2.5, 2, 1.5, 1, 0.5]

    def __init__(self, use_collar: bool = True):
        self.plates = defaultdict(int)
        for weight in self.weights:
            self.plates[weight] = 4
        self.use_collar = use_collar

    def add_plate(self, weight: float, quantity: int = 1) -> None:
        self.plates[weight] += quantity

    def remove_plate(self, weight: float, quantity: int = 1) -> None:
        if self.plates[weight] < quantity:
            raise ValueError(f"Not enough plates of weight {weight}")
        self.plates[weight] -= quantity
        if self.plates[weight] == 0:
            del self.plates[weight]

    def get_quantity(self, weight: float) -> int:
        return self.plates[weight]

    def __repr__(self) -> str:
        return str(list(self.plates.items()))

# if __name__ == "__main__":
#     plates = Plates()
#     # print([(plate.name, plate.weight, plate.quantity) for plate in plates])

#     plates.add_plate(25, 2)
#     print(repr(plates))

