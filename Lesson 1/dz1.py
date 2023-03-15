import random
alphabetRu = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о",
            "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
alphabetEn = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Первый способ
for i in alphabetRu:
    print(i, end=' ')
print(end='\n')
for i in reversed(alphabetRu):
    print(i, sep=' ', end=' ')
print(end='\n')
for i in alphabetEn:
    print(i, end=' ')
print(end='\n')
for i in reversed(alphabetEn):
    print(i, sep=' ', end=' ')

