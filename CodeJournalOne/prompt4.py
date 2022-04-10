class Cat:
    def __init__(self, armLength, legLength, numEyes, hasTail, isFurry):
        self.armLength = armLength
        self.legLength = legLength
        self.numEyes = numEyes
        self.hasTail = hasTail
        self.isFurry = isFurry

    def printAtttributes(self):
        print(f'The cat has arms of {self.armLength} length and legs of {self.legLength} length. It has {self.numEyes} eyes, {"a tail" if self.hasTail else "doesn not have a tail"}, and {"is furry" if self.isFurry else "is not furry"}')

def main():
    cat = Cat(2, 2, 2, True, True)
    cat.printAtttributes()

main()
