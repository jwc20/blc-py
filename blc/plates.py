class Plate:
    def __init__(self, weight, quantity) -> None:
        self.weight = weight
        self.quantity = quantity


class Plates:
    weights = [25, 20, 15, 10, 5, 2.5, 2, 1.5, 1, 0.5]

    def __init__(self, use_collar=True) -> None:
        self.plates = [Plate(weight, 4) for weight in self.weights]
        self.use_collar = use_collar

    def __iter__(self):
        return iter(self.plates)

    def __repr__(self):
        return str([(plate.weight, plate.quantity) for plate in self.plates])

    def add_plate(self, weight, quantity=1):
        for plate in self.plates:
            if plate.weight == weight:
                plate.quantity += quantity
                return
        raise ValueError(f"Plate {weight} not found")

    def remove_plate(self, weight, quantity=1):
        for plate in self.plates:
            if plate.weight == weight:
                plate.quantity -= quantity
                if plate.quantity == 0:
                    self.plates.remove(plate)
                return
        raise ValueError(f"Plate {weight} not found")

    def get_plate(self, weight):
        for plate in self.plates:
            if plate.weight == weight:
                return plate
        raise ValueError(f"Plate {weight} not found")


if __name__ == "__main__":
    plates = Plates()
    # print([(plate.name, plate.weight, plate.quantity) for plate in plates])

    plates.add_plate(25, 2)
    print(repr(plates))
