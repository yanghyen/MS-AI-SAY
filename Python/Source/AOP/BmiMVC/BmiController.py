from BmiView import ConsoleScreen
from DoctorModel import Doctor


if __name__ == "__main__":
    guest = ConsoleScreen.getGuestInfo()
    Doctor.calculate(guest)
    ConsoleScreen.printFesult(guest)