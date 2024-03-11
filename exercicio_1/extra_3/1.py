def calculate(x, y, z):
    w = x * y < z / x or x / y < z * x and z * y < x
    print(w)

calculate(5, 10, 15)
calculate(40, 10, 3)
calculate(20, 2, 13)
