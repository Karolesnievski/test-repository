x = 100

def f():
    global x
    x += 1
    print(x)

f()



try:
    a = input("podaj liczbe: ")
    b = input("podaj liczbe drugą: ")
    a = int("a")
    b = int("b")
    print(a / b)
    print("ok")
except(ValueError):
    print("nieprawidoe")


