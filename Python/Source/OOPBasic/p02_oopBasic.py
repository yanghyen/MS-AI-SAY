class Capybara:
    name = None
    age = None

    def nap(self, cnt):
        print("ᶻ z 𐰁 .ᐟ " * cnt)

    def showInfo(self):
        print(self.name)
        print(self.age)

c1 = Capybara()
c1.name = "차누바라"
c1.age = 7
c1.nap(3)
c1.showInfo()