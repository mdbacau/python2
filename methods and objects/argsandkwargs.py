def myfunc(a,b,c=0,d=0,e=0):
    # Returns 5% of the sum of a and b
    return sum((a,b,c,d,e)) * 0.05

print(myfunc(60,40,100,22,223))

def myfunc2(*args):
    for item in args:
        print(item)
myfunc2('haha',30)

def kwargsex(**kwargs):
    if 'fruit' in kwargs:
        print('Fruits are here boss, I like {}'.format(kwargs['fruit']))
    else:
        print('N-avem fructe sefule')

kwargsex(fruit='para')

def functie(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))

functie(10,20,30,food='orange',test='oua',mata='craciun')