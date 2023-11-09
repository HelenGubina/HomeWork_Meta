def sum_digits(num):
    if num > 0:
        sum_d = sum_digits(num // 10) + num % 10
        return sum_d
    else:
        return 0


print(sum_digits(5679))
