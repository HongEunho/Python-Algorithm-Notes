roma1 = input()
roma2 = input()
roma_dict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}


def roma_to_num(roma):
    i = 0
    sum = 0
    while i < len(roma):
        # 끝자리 일 경우는 예외사항 체크 X
        if i == len(roma) - 1:
            sum += roma_dict[roma[i]]
            break
        else:
            if roma[i:i + 2] == "IV":
                sum += 4
                i += 2
            elif roma[i:i + 2] == "IX":
                sum += 9
                i += 2
            elif roma[i:i + 2] == "XL":
                sum += 40
                i += 2
            elif roma[i:i + 2] == "XC":
                sum += 90
                i += 2
            elif roma[i:i + 2] == "CD":
                sum += 400
                i += 2
            elif roma[i:i + 2] == "CM":
                sum += 900
                i += 2
            else:
                sum += roma_dict[roma[i]]
                i += 1
    return sum

num1 = roma_to_num(roma1)
num2 = roma_to_num(roma2)


sum_num = num1+num2
roma_stack = []

while sum_num > 0:
    if sum_num >= 1000:
        roma_stack.append("M")
        sum_num -= 1000
    elif sum_num >= 900:
        roma_stack.append("CM")
        sum_num -= 900
    elif sum_num >= 500:
        roma_stack.append("D")
        sum_num -= 500
    elif sum_num >= 400:
        roma_stack.append("CD")
        sum_num -= 400
    elif sum_num >= 100:
        roma_stack.append("C")
        sum_num -= 100
    elif sum_num >= 90:
        roma_stack.append("XC")
        sum_num -= 90
    elif sum_num >= 50:
        roma_stack.append("L")
        sum_num -= 50
    elif sum_num >= 40:
        roma_stack.append("XL")
        sum_num -= 40
    elif sum_num >= 10:
        roma_stack.append("X")
        sum_num -= 10
    elif sum_num >= 9:
        roma_stack.append("IX")
        sum_num -= 9
    elif sum_num >= 5:
        roma_stack.append("V")
        sum_num -= 5
    elif sum_num >= 4:
        roma_stack.append("IV")
        sum_num -= 4
    else:
        roma_stack.append("I")
        sum_num -= 1

print(num1+num2)
print("".join(roma_stack))
