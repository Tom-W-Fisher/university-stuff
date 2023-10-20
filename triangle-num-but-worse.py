def calc_triangle_num(num: int):
    return sum(i for i in range(num))

def triangle_input():
    num = int(input("Please input a number:\n"))
    print(calc_triangle_num(num))