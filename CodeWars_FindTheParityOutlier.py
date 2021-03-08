def find_outlier(integers):
    isEvenNumbers = (((integers[0] % 2) == 0) and ((integers[1] % 2) == 0)) or (((integers[0] % 2) == 0) and ((integers[2] % 2) == 0)) or (((integers[1] % 2) == 0) and ((integers[2] % 2) == 0))

    for integer in integers:
        if (isEvenNumbers and ((integer % 2) == 1)):
            return integer
        
        if ((isEvenNumbers == False) and ((integer % 2) == 0)):
            return integer

    return 0

num1 = [2, 4, 0, 100, 4, 11, 2602, 36]
num2 = [160, 3, 1719, 19, 11, 13, -21]
print(find_outlier(num1))
print(find_outlier(num2))