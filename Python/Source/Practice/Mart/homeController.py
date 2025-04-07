# 1) 회사 등록
# ...
# 10) 종로
# ------------
# 뭐 : 1
# ------------
# 회사명 : 
# ...
# ------------
# 뭐 : 3
# ------------
# 1) 회사 등록
# ...
# 10) 종로
# ------------

# if __name__ == "__main__":
# 의미 : 

from calendar import c
from ManufacturerDAO import ManufacturerDAO
from SnackDAO import SnackDAO
from View import ConsoleScreen

if __name__ == "__main__":
    SnackDAO.getAllSnackCount()
    while True:
        menu = ConsoleScreen.showMainMenu()
        if menu == "10":
            break
        elif menu == '1':
            m = ConsoleScreen.showRegManufacturerMenu()
            result = ManufacturerDAO.reg(m)
            ConsoleScreen.printResult(result)
        elif menu == '2':
            s = ConsoleScreen.showRegSnackMenu()
            result = SnackDAO.reg(s)
            result = ConsoleScreen.printResult(result)
        elif menu == '3':
            manufacturers = ManufacturerDAO.getAll()
            ConsoleScreen.printManufacturers(manufacturers)
        elif menu == '4':
            snacks = SnackDAO.getAll()
            ConsoleScreen.printSnacks(snacks)
        elif menu == '6':
            pass


