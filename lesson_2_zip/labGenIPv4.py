import random

def getIPv4(min=(1,0,0,0), max=(255,255,255,255)):
    # генерируем четыре случайных числа от min до max
    numbers = [str(random.randint(min[i], max[i])) for i in range(4)]
    # объединяем в одну строку через точку
    return ".".join(numbers)

print(getIPv4())                 # 104.119.162.55
print(getIPv4(min=(192,168,0,0)))  # 192.168.11.87
print(getIPv4(min=(192,168,0,0), max=(192,168,255,255)))  # 192.168.102.214
