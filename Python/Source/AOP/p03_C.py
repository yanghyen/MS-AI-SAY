# Controller 
#   상황 판단해서 M 필요하면 M 소환, V 필요하면 V 소환

from p03_M import Calculator
from p03_V import ConsoleScreen

if __name__ == "__main__":
    x, y = ConsoleScreen.getXY()
    z = Calculator.getSum(x, y)
    ConsoleScreen.printResult(z)