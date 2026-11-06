# Program to find the sum of the series: 1 + x + x^2 + ... + x^n
x = int(input("Enter the base value (x): "))
n = int(input("Enter the maximum power exponent (n): "))
series_sum = 0

for i in range(n + 1):
    series_sum += (x ** i)

print(f"The total sum of the series is: {series_sum}")
