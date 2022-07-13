#Class
'''
class Rectangle:
    def __init__(self,width,height,color):
        self.width = width
        self.height = height
        self.color = color
        
rect = Rectangle(7,8,"red")
print(rect.color)
'''

#Inheritance
'''
class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

class cat(Animal):
    def pur(self):
        print("pur...")

class dog(Animal):
    def bark(self):
        print("woof!")

fido = dog("fido","brown")
print(fido.color)
fido.bark()
'''
'''
class A:
    def method(self):
        print("A")

class B(A):
    def anothermethod(self):
        print("B")

class C(B):
    def thirmethod(self):
        print("C")

c=C()
c.method()
c.anothermethod()
c.thirmethod()
'''

'''
class A:
    def spam(self):            ###super()
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()
'''

#Magic methods ***********
'''
class Vector2D:     #각 벡터의 x,y add
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector2D(self.x+other.x,self.y+other.y)

first = Vector2D(5,7)
second = Vector2D(3,9)
result = first + second
print(result.x)
print(result.y)
'''
'''
class specialstring:
    def __init__(self,cont):
        self.cont = cont

    def __truediv__(self,other):
        line = "="*len(other.cont)
        return "\n".join([self.cont,line,other.cont])

spam = specialstring("spam")
hello = specialstring("hello world")
print(spam/hello)
'''
'''
class specialstring:
    def __init__(self,cont):
        self.cont = cont
        
    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = specialstring("spam")
eggs = specialstring("eggs")
spam > eggs
'''
'''
import random as r

class vaguelist:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self,index):
        return self.cont[index+r.randint(-1,1)]

    def __len__(self):
        return r.randint(0,len(self.cont)*2)

vague_list = vaguelist(["A","B","C","D","E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
'''

#Object Lifecycle
'''
a=42
del a
'''

#Data Hiding
'''
class queue:
    def __init__(self,contents):
        self._hiddenlist = list(contents)

    def push(self,value):
        self._hiddenlist.insert(0,value)

    def pop(self):
        return self._hiddenlist.pop(-1)
    
    def __repr__(self):
        return "queue({})".format(self._hiddenlist) #####

queue = queue([1,2,3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
'''
'''
class spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s = spam()
s.print_egg()
print(s._spam__egg)
print(s._egg)        #error point
'''

#Class Methods
'''
class rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width*self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length,side_length)

square = rectangle.new_square(5)
print(square.calculate_area())
'''
'''
class pizza:
    def __init__(self,toppings):
        self.toppings = toppings

        @staticmethod
        def validate_topping(topping):
            if topping == "pineapple":
                raise ValueError("No pineapples!")
            else:
                return True

ingredients = ["cheese","onions","spam"]
if all(pizza.validate_topping(i)):
    for i in (ingredients):                  #????error
        pizza = pizza(ingredients)   
'''

#Properties
'''
class pizza:
    def __init__(self,toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False

pizza = pizza(["cheese","tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True      #읽기 속성이라 변경에서 오류나는 듯
'''
'''
class pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self,value):
        if value:
            password = input("enter the password: ")
            if password == "aaa":
                self._pineapple_allowed = value

            else:
                raise ValueError("Alert! Intruder")

pizza = pizza(["cheese","tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)
'''

#A Simple Game
'''
def get_input():                    #명령어와 같음 say 할말
    command = input(": ").split()   #.split() 
    verb = command[0]
    if verb in verb_dict:
        verbb = verb_dict[verb]
    else:
        print("unknown verb {}".format(verb))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verbb(noun_word))
    else:
        print(verbb("nothing"))

def say(noun):
    return 'you said"{}"'.format(noun)

verb_dict = {"say":say,"examine":examine,}

while True:
    get_input()


class Gameobject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name

Gameobject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc

class Goblin(gameobject):
    class_name = "goblin"
    desc = "a foul creature"

goblin = Goblin("gobbly")

def examine(noun):
    if noun in Gameobject.objects:
        return

Gameobject.objects[noun].get_desc()
    else:
        return "this is no {} here".format(noun)
'''
'''
class Goblin(Gameobject):
    def __init__(self, name):
        self.class_name = 'goblin'
        self.health = 3
        self._desc = "a foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "it has a wound on its knee."
        elif self.health ==1:
            health_line = "its left arm has been cut off"
        elif self.health <= 0:
            health_line = "it is dead"
        return self._desc +"\n"+health_line

    @desc.setter
    def desc(self,value):
        self._desc = value

def hit(noun):
    if noun in Gmaeobject.objects:
        thing = Gameobject.objects[noun]
        if type(thing) == Goblin:
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = "you killed the gonlin"
            else:
                msg = "you hit the {}".format(thing.class_name)
        else:
            msg = "there is no {} here".format(noun)
        return msg
'''
