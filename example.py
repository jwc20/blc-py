from blc import Blc, Barbell, Plates


if __name__ == "__main__":
    weight = 206

    blc = Blc(Plates(use_collar=False), Barbell(weight=20, type="men"))
    print(blc.calculate_plates(weight))

    plates2 = Plates(use_collar=True)
    plates2.remove_plate(25, 8)

    blc2 = Blc(plates2, Barbell(weight=20, type="men"))
    print(blc2.calculate_plates(weight), " + collars")

    plates3 = Plates(use_collar=True)
    plates3.remove_plate(25, 8)
    blc3 = Blc(plates3, Barbell(weight=20, type="men"))
    blc3.add_weight(1)
    print(f"{blc3.calculate_plates(weight)} + collars, new weight: {blc3.weight}")
    
    
    plates4 = Plates(use_collar=True)
    plates4.remove_plate(25, 8)
    blc4 = Blc(plates4, Barbell(weight=20, type="men"))
    blc4.calculate_plates(weight)
    blc4.remove_weight(20)
    print(f"{blc4.plates_to_use} + collars, new weight: {blc4.weight}")

    plates6 = Plates(use_collar=True)
    plates6.remove_plate(25, 8)
    blc6 = Blc(plates6, Barbell(weight=20, type="men"))
    blc6.calculate_plates(208)
    print(f"{blc6.plates_to_use} + collars, new weight: {blc6.weight}")
