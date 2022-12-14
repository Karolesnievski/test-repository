
#first
def squared(x):
    return x ** 2
print(squared(2))

#second
def print_string(string):
    print(string)

print_string("testujemy: 1, 2, 3.")

#third
def add_mult(a,b,c,x=100,z=1000):
    return a + b + b * x * z
result = add_mult(10, 15, 25)
print(result)