from socket import AI_PASSIVE
from BmiView import ConsoleScreen


class Calculator:
    def heightToMeter(height):
        if height >10:
            height = height / 100
            return height
        else:
            return height
        
    def calculator(weight, height):
        bmi = weight / height * height
        return bmi