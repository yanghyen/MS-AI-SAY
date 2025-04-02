# x : 
# y : 
# --------------
# 

# def calculation():
#     x = int(input("x : "))
#     y = int(input("y : "))
#     print(x + y, x - y, x * y, x/y)

# calculation()

x = int(input("x : "))
y = int(input("y : "))

try:
    d = x / y
    print("----------")
    print(d)

    e = [43, 23, 23]
    print(e[y])
except Exception as e:
    print("쨌든 잘못됨")
    print(e)

finally:
    print("쨌든 실행됨")