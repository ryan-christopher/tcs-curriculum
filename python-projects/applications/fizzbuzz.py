# fizzbuzz.py by Ryan Christopher
nums = []
def fizzbuzz(n):
    for i in range(1,n+1):
        if i % 3 != 0 and i % 5 != 0:
            nums.append(str(i))
        elif i % 3 == 0 and i % 5 != 0:
            nums.append("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            nums.append("Buzz")
        else:
            nums.append("FizzBuzz")
    return nums
    
print(fizzbuzz(100))