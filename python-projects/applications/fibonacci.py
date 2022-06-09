# fibonacci.py

# method 1
# display the first 15 digits of the fibonacci sequence
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
num1 = 0
num2 = 1
num3 = num1 + num2
for i in range(5):
    print(num1)
    print(num2)
    print(num3)
    num1 = num2 + num3
    num2 = num3 + num1
    num3 = num1 + num2

