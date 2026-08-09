def greatest(num1, num2, num3):
    if (num1>num2):
        greater=num1
    else:
        greater=num2
    if(num3>greater):
        greater=num3
    return greater
a=greatest(33, 56, 26)
print(a)