import random
#Параметры для генерации паролей
countPassword = input('Количество паролей: ')
countSymvol = input('Количество символов в пароле: ')
# 1
# checkNumber = input('Использовать цифры в пароле (True - да, False - нет): ')
checkNumber = True #По умолчанию верно, так как цифры в пароле обязательны
# checkLowerLetter = input('Использовать маленькие буквы в пароле (True - да, False - нет): ')
checkLowerLetter = True #По умолчанию верно, так как букбы нижнего регистра обязательны
checkUpperLetter = input('Использовать большие буквы в пароле (1 - да, 0 - нет): ')
checkSpecSymvol = input('Использовать спец символы в пароле (1 - да, 0 - нет): ')
checkMySpecSymvol = input('Хотите ли вы использовать спец символы выбранные вами? (1 - да, 0 - нет): ')
if (checkMySpecSymvol == '1'):
    inputSymvol = input('Введите слитно спец символы, которые будут использовать в пароле: ')
else:
    inputSymvol = ''
    
alphabetEnLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetEnUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
arrayNumber = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
alphabetSpecSymvol = ['@', '№', '$', '%', '^', '&', '\\', '*', '(', ')']

def generatePassword(countPassword, countSymvol, checkUpperLetter, checkSpecSymvol, inputSymvol2):
    
    if (checkSpecSymvol):
        arraySymvol = [char for char in inputSymvol2]
    print(arraySymvol)
    
    k = round(int(countSymvol)*0.45) #кол-во букв нижнего регистра в пароле
    l = round(int(countSymvol)*0.2)   #кол-во букв верхнего регистра в пароле
    d = round(int(countSymvol)*0.15) #кол-во спец символов в пароле
    j = int(countSymvol)-k-l-d   #кол-во цифр в пароле
    
    for i in range(int(countPassword)):
        if (checkUpperLetter == '0' and checkSpecSymvol == '0'): #Генерация пароля из цифр и букв нижнего регистра
            temp_array = [] #пустой массив для символов генерации пароля
            for i in range(k):
                temp_array.append(random.choice(alphabetEnLower))
            for i in range(j):
                temp_array.append(random.choice(arrayNumber))
            print(temp_array)      
            random.shuffle(temp_array)
            print(temp_array)
        
        if (checkUpperLetter == '1' and checkSpecSymvol == '0'):
            temp_array = [] #пустой массив для символов генерации пароля
            for i in range(k):
                temp_array.append(random.choice(alphabetEnLower))
            for i in range(j):
                temp_array.append(random.choice(arrayNumber))
            for i in range(l):
                temp_array.append(random.choice(alphabetEnUpper))   
            print(temp_array)      
            random.shuffle(temp_array)
            print(temp_array)
        
        if (checkUpperLetter == '0' and checkSpecSymvol == '1' and checkMySpecSymvol == '0'):
            temp_array = [] #пустой массив для символов генерации пароля
            for i in range(k):
                temp_array.append(random.choice(alphabetEnLower))
            for i in range(j):
                temp_array.append(random.choice(arrayNumber))
            for i in range(d):
                temp_array.append(random.choice(alphabetSpecSymvol))   
            print(temp_array)      
            random.shuffle(temp_array)
            print(temp_array)
            
        if (checkUpperLetter == '0' and checkSpecSymvol == '1' and checkMySpecSymvol == '1'):
            temp_array = [] #пустой массив для символов генерации пароля
            for i in range(k):
                temp_array.append(random.choice(alphabetEnLower))
            for i in range(j):
                temp_array.append(random.choice(arrayNumber))
            for i in range(d):
                temp_array.append(random.choice(arraySymvol))   
            print(temp_array)      
            random.shuffle(temp_array)
            print(temp_array)
            
        if (checkUpperLetter == '1' and checkSpecSymvol == '1' and checkMySpecSymvol == '0'):
            temp_array = [] #пустой массив для символов генерации пароля
            for i in range(k):
                temp_array.append(random.choice(alphabetEnLower))
            for i in range(j):
                temp_array.append(random.choice(arrayNumber))
            for i in range(d):
                temp_array.append(random.choice(alphabetSpecSymvol))
            for i in range(l):
                temp_array.append(random.choice(alphabetEnUpper))  
            print(temp_array)      
            random.shuffle(temp_array)
            print(temp_array)
            
        if (checkUpperLetter == '1' and checkSpecSymvol == '1' and checkMySpecSymvol == '1'):
            temp_array = [] #пустой массив для символов генерации пароля
            for i in range(k):
                temp_array.append(random.choice(alphabetEnLower))
            for i in range(j):
                temp_array.append(random.choice(arrayNumber))
            for i in range(d):
                temp_array.append(random.choice(arraySymvol))
            for i in range(l):
                temp_array.append(random.choice(alphabetEnUpper))  
            print(temp_array)      
            random.shuffle(temp_array)
            print(temp_array)   
    
    
generatePassword(countPassword, countSymvol, checkNumber, checkLowerLetter, checkUpperLetter, checkSpecSymvol, inputSymvol)