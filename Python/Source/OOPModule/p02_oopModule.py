from p03_oopModule import Book

class BoardMarker:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def showww(self):
        print(self.name)
        print(self.color)
        
b = Book("Attack on Titan", 300000000)
b.show()

