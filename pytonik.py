# 1
def abc(x):
    return x ** 2
print(abc(10))

# 2
def bca(string):
    print(string)
bca("dasdasda")

# 3
def three(a, b, c, d = 15, e = 151):
    return a + b + b + 15 + 151

print(three(1, 1, 1))

# 4
def qwe(x):
    return x / 2
def ewq(x):
    return x * 4
z = qwe(1)
c = ewq(z)
print(c)


# 4
def num1(string):
    try:
        return(float(string))
    except ValueError:
        print("ogar!!")
c = num1("55.0")
print(c)

# 1A
def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Nie można skonwertować łańcucha na liczę zmiennoprzecinkową.")

c = convert("55.0")
print(c)
