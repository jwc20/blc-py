from blc import Blc, Barbell, Plates


if __name__ == "__main__":
    weight = 206

    blc = Blc(weight, Plates(use_collar=False), Barbell(weight=20, type="men"))
    print(blc.calculate_plates())

    plates2 = Plates(use_collar=True)
    plates2.remove_plate(25, 8)

    blc2 = Blc(weight, plates2, Barbell(weight=20, type="men"))
    print(blc2.calculate_plates(), " + collars")

    plates3 = Plates(use_collar=True)
    plates3.remove_plate(25, 8)
    blc3 = Blc(weight, plates3, Barbell(weight=20, type="men"))
    blc3.add_weight(1)
    print(f"{blc3.calculate_plates()} + collars, new weight: {blc3.weight}")
    
    
    plates4 = Plates(use_collar=True)
    plates4.remove_plate(25, 8)
    blc4 = Blc(weight, plates4, Barbell(weight=20, type="men"))
    blc4.calculate_plates()
    blc4.remove_weight(20)
    print(f"{blc4.plates_to_use} + collars, new weight: {blc4.weight}")
