#!/usr/bin/python3
class Person:
    def __init__(self, name):
        self.name = name

    
    def say_hi(self):
        print("Hello, my name is", self.name)

p = Person('Rachel')
p.say_hi()

class User:
    id = 1

User.id = 98
u = User()
u.id = 89
print(User.id)

class User:
    id = 1

u = User()
u.id = 89
User.id = 98
print(u.id)

def increment(n):
    n += 1

a = 1
increment(a)
print(a)

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)