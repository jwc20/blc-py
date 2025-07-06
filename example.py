from blc import Blc, Barbell, Plates


if __name__ == "__main__":
    weight = 206

    blc = Blc(weight, Plates(use_collar=False), Barbell(weight=20, type="men"))
    print(blc.calculate_plates())

    plates2 = Plates(use_collar=True)
    plates2.remove_plate(25, 8)

    blc2 = Blc(weight, plates2, Barbell(weight=20, type="men"))
    print(blc2.calculate_plates(), " + collars")
