class Barbell:
    def __init__(self, weight=20, type="men"):
        if type == "women":
            self.weight = 15
        else:
            self.weight = weight
        self.type = type


if __name__ == "__main__":
    barbell = Barbell() 
    print(barbell.type, barbell.weight)
    
    barbell_w = Barbell(type="women") 
    print(barbell_w.type, barbell_w.weight)
