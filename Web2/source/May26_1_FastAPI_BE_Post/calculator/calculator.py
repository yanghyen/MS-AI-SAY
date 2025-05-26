class Calculator():
    def calculate(x, y):
        x = int(x)
        y = int(y)
        return {
            "hap" : x + y,
            "cha" : x - y,
            "gob" : x * y,
            "moks" : x / y
        }