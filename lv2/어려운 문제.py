def factorial_digit_reduction(n):
    def factorial(num):
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))

    result = factorial(n)

    while result >= 10:
        result = sum_of_digits(result)

    return result

n = int(input())
print(factorial_digit_reduction(n))