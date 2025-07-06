from .plates import Plates
from .barbell import Barbell


class Blc:
    def __init__(self, weight, plates: Plates, barbell: Barbell) -> None:
        self._weight = weight
        self.plates = plates
        self.barbell = barbell

    def calculate_plates(self):
        target_weight = self._weight
        plates_to_use = []

        weight_to_load = (
            target_weight - self.barbell.weight
        ) / 2  # weights that need to be loaded for one side

        if self.plates.use_collar:
            weight_to_load -= 2.5

        if weight_to_load <= 0:  # or weight_to_load >= 275:
            raise ValueError("Invalid weight")

        for weight, quantity in self.plates:
            while weight_to_load >= weight and quantity >= 2:
                weight_to_load -= weight
                plates_to_use.append(weight)
                quantity -= 2

        return plates_to_use
