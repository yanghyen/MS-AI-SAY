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
    sDAO = SnackDAO()
    mDAO = ManufacturerDAO()

    while True:
        menu = ConsoleScreen.showMainMenu()
        if menu == "10":
            break

        elif menu == '1':
            m = ConsoleScreen.showRegManufacturerMenu()
            result = mDAO.reg(m)
            ConsoleScreen.printResult(result)

        elif menu == '2':
            s = ConsoleScreen.showRegSnackMenu()
            result = sDAO.reg(s)
            result = ConsoleScreen.printResult(result)

        elif menu == '3':
            manufacturers = mDAO.getAll()
            ConsoleScreen.printManufacturers(manufacturers)
        
        elif menu == '4':
            snacks = sDAO.getAll()
            ConsoleScreen.printSnacks(snacks)
        
        elif menu == '5':
            pageCount = mDAO.getAllPageCount("")
            pageNo = ConsoleScreen.showSelectPageMenu(pageCount)
            manufacturers = mDAO.get(pageNo)
            ConsoleScreen.printManufacturers(manufacturers)
        
        elif menu == '6':
            pageCount = sDAO.getPageCount("")
            pageNo = ConsoleScreen.showSelectPageMenu(pageCount)
            snacks = sDAO.get(pageNo, "")
            ConsoleScreen.printSnacks(snacks)

        elif menu == '7':
            pass
       
        elif menu == '8':
            searchTxt = ConsoleScreen.searchMenu()
            pageCount = sDAO.getSearchSnackCount(searchTxt)
            pageNo = ConsoleScreen.showSelectPageMenu(pageCount)
            snacks = sDAO.get(pageNo, searchTxt)
            ConsoleScreen.printSnacks(snacks)

        elif menu == '9':
            pass