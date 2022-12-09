x = 100

def f():
    global x
    x += 1
    print(x)

f()




a = input("wpisz liczbę: ")
b = input("wpisz drugą liczbę: ")
a = int(a)
b = int(b)
try:
    print(a/b)
except ZeroDivisionError:
    print("Drugą liczba nie może byc 0.")

    