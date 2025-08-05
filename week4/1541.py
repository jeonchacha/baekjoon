# 1541 잃어버린 괄호
import sys
input = sys.stdin.readline
expression = input().strip()

def min_calc(expression):
    removed_minus = list(expression.split("-"))
    result = 0
    is_first = True
    for exp in removed_minus:
        removed_plus = list(map(int, exp.split("+")))
        if is_first:
            result += sum(removed_plus)
            is_first = False
            continue
        result -= sum(removed_plus)
    return result

print(min_calc(expression))