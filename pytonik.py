# 1
def firstt(x):

    return x ** 2
print(firstt(8))

# 2
def second():
    print("asdsa", "adsasda", "asdasgffg")
second()

#3
def hihihi(z, x, c, a = 100, s = 250):
    return z + x + c + a + s
result = hihihi(1, 1, 1)
print(result)


# 4 
def fourth(x):
    return x / 2
def multi(x):
    return x * 4
y = fourth(1)
z = multi(y)
print(z)

# 5
def conv(string):
    try: 
       return float(string)
    except ValueError:
        print("nain")
c = conv("55.0")
print(c)



