def function_name():
    print('Hello '+name)
name = 'Marcus'
function_name()

def calculeaza(num1,num2):
    return num1 + num2
result = calculeaza(1,2)
print(result)

def say_hello(nume='NUME'):
    return 'Hello '+nume
rezultat = say_hello('Julian')
print(rezultat)

def add(a1,a2):
    return a1+a2
result2 = add(20,30)
print(result2)

def truecheck(mystring):
    return 'true' in mystring.lower()
print(truecheck('alTrueism'))

def pig_latin(word):
    first_letter = word[0]

    # check if first letter is vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word
print(pig_latin('apple'))