def check_sum(num1, num2):
    if num1 <= 0 and num2 <= 0:
        return "Числа негативные или равны нулю"
    elif num1 == num2:
        return "Числа равны друг другу"
    else:
        sum_result = num1 + num2
        if sum_result >= 10:
            return str(sum_result)
        else:
            return "Сумма чисел слишком мала"

print(check_sum(5, 6))    # Выведет: "11"
print(check_sum(3, 2))    # Выведет: "Сумма чисел слишком мала"
print(check_sum(1, 1))    # Выведет: "Числа равны друг другу"
print(check_sum(0, 0))    # Выведет: "Числа негативные или равны нулю"
print(check_sum(-1, -2))  # Выведет: "Числа негативные или равны нулю"
print(check_sum(-3, 3))   # Выведет: "Сумма чисел слишком мала"
