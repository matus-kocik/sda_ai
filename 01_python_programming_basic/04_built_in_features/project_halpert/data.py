def even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"


print(even_or_odd(2))
print(50 * "-")


def basic_operation(operation, val1, val2):
    if operation == "add":
        return val1 + val2
    elif operation == "sub":
        return val1 - val2
    elif operation == "mul":
        return val1 * val2
    elif operation == "div":
        if val2 == 0:
            return "Division by zero is not allowed"
        return val1 / val2


print(basic_operation("add", 2, 3))
print(basic_operation("sub", 2, 3))
print(basic_operation("mul", 2, 3))
print(basic_operation("div", 2, 3))
print(basic_operation("div", 2, 0))
print(50 * "-")


def total_points(total_score):
    home_score = total_score.split(":")[0]
    away_score = total_score.split(":")[1]
    if home_score > away_score:
        return 3
    elif home_score == away_score:
        return 1
    else:
        return 0


print(total_points("0:5"))
print(type(total_points("0:5")))
print(50 * "-")

def largest_number(a,b,c):
    result = [
        a+b+c,
        a*b*c,
        (a+b)*c,
        a*(b+c),
        (a+c)*b
    ]
    return max(result)

print(largest_number(1,2,3))
print(50 * "-")

def index(array, number):
    if number in range(0, len(array)):
        return array[number]**number
    else:
        return -1


print(index([1,2,3,4,5], 2))
print(50 * "-")
