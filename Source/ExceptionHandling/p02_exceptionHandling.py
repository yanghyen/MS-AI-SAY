def getShare(a, b):
    try:
        c = a / b
        return c
    except Exception as e:
        return -2
    finally:
        print("앙 집에 가고 싶당")
a = 10
b = int(input())
c = getShare(a, b)
print(c)