def divide(dividend: int, divisor: int) -> int:
    quot = 0
    while dividend >= divisor:
        quot += 1
        dividend -= divisor
    return quot

def multiply(n1, n2):
    prod = 0
    while n2 > 0:
        prod += n1
        n2 -= 1
    return prod
