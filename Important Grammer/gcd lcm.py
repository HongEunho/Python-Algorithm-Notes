import math

a = 21
b = 14
print(math.gcd(a, b))
# python 3.9부터는 lcm도 라이브러리로 제공 print(math.lcm(a, b))
print(a * b // math.gcd(a, b)) # 혹은 이렇게 lcm 표현해도 됨