import random

def genDice(countDice = 1, countFace = 6, value_on_face = (1,2,3,4,5,6)) -> tuple:
    if (countFace == len(value_on_face)):
        all_dice = []
        for i in range(countDice):
            all_dice.append(random.choice(value_on_face))
        return tuple(all_dice)
    else:
        print("Количество граней должно совпадать с количеством значений на гранях")
        return tuple()

print(genDice())
print(genDice(3))
print(genDice(3,5,(1,2,3,4,5)))