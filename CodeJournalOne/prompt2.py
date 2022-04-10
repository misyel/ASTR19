def summation(x, y): 
    return x+y

def difference(x, y):
    return x-y

def product(x, y):
    return x*y

def main():
    floatX = 1.234
    floatY = 2.34
    intX = 1
    intY = 2

    sumOfTwoFloats = summation(floatX, floatY)
    diffOfTwoInts = difference(intX, intY)
    productOfFloatInt = product(floatX, intY)

    print(f'Sum of two floats: {floatX} and {floatY} is {sumOfTwoFloats} of {type(sumOfTwoFloats)}')
    print(f'Diff of two ints: {intX} and {intY} is {diffOfTwoInts} of {type(diffOfTwoInts)}')
    print(f'Product of float and int: {floatX} and {intY} is {productOfFloatInt} of {type(productOfFloatInt)}')

main()