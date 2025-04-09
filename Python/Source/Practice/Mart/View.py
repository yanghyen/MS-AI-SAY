# def showMainMenu():의 self 여부 : 
#   저장할 게 없어서 멤버변수(객체) 없이 static메소드 기반으로 진행
#   근데 getAllSnackCount()하려면 필요함..
# PL 모르는 사람이 본다고 생각하고 짜기 -> 형변환 같은 개념 X

from Snack import Snack
from Manufacturer import Manufacturer

class ConsoleScreen:
    def showMainMenu():
        print("1) 회사등록")
        print("2) 과자등록")
        print('3) 회사전체조회')
        print('4) 과자전체조회')
        print('5) 회사조회')
        print('6) 과자조회')
        print('7) 회사검색')
        print('8) 과자검색')
        print('9) ')
        print("10) 종료")
        print('-----------')
        return input("뭐 : ")
    
    def showRegManufacturerMenu():
        name = input("회사 명 : ")
        addr = input("주소 : ")
        ceo = input("사장 : ")
        emp = input("인원수 : ")
        return Manufacturer(name, addr, ceo, emp)
    
    def showRegSnackMenu():
        name = input("과자 이름 : ")
        exp = input("유통기한(YYYYMMDD) : ")
        price = input("가격 : ")
        weight = input("중량 : ")
        c_name = input("제조사 : ")
        return Snack(name, exp, price, weight, c_name)
    
    def searchMenu():
        return input("검색어 : ")
    
    def showSelectPageMenu(pageCount):
        return input("페이지(1 ~ %d) : " % pageCount)
    
    def printResult(result):
        print(result)
        print("--------------")

    def printSnacks(snacks):
        for s in snacks:
            print(s.name, s.price, s.weight)
            print(s.c_name)
            print(s.exp)
            print('-----------')

    def printManufacturers(manufacturers):
        for m in manufacturers:
            print(m.name, m.addr, m.ceo, m.emp)
            print('------------')