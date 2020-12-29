# -*- coding: utf-8 -*-
"""week01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18igLAYaikXy1kNOmYzeAhdIyIq4toLaB

# week01 Python基础练习

# list
"""

nlist =[1,2,3]
nlist2=[7,8,9]
print(nlist)

nlist.append(4)#添加元素list#
print(nlist)

nlist.extend(nlist2)#合并两个list#
print(nlist)
nlist.insert(6,11)#在指定的位置添加元素，如果位置不存在，则添加到末尾#
print(nlist)

nlist.sort()
print(nlist)
nlist.reverse() #反转#
print(nlist)

"""# set"""

s={1,2,3,4}#不重复的集合#
s.add(4)
print(s)

s =set(('a', 'cc', 'f'))#2个括号#
print(s)
s.update('22','11','a')
print(s)

#s.remove('a')#没有元素在列表中就会报错#
print(s)
s.discard('a')#没有该元素也不会报错#
print(s)

s1 ={'2','aa','f','bb'}
print(s1|s) #求并集#
print(s&s1) #求交集#
print(s1-s) #求s1中不在s中的元素#
print(s.difference(s1))#求s中不存在s1中的元素
print(s1^s)#求s1和s中不重复元素的集合-对称差集

"""# dict"""

d = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
print(d)
d["v"]="vegatable" #增加#
print(d)
del(d["b"])#删除#
print(d)

#字典遍历#
d ={"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
for k in d:
  print(k,d[k])
print(d.items())
for (k, v) in d.items():
    print(k,v)

#使用列表、字典作为字典的值#
d = {"a" : ("apple",), "bo" : {"b" : "banana", "o" : "orange"}, "g" : ["grape","grapefruit"]}
print(d["a"])
print(d["a"][0])
print(d["bo"]["b"][0])
print(d["bo"]["o"])

"""# namedtuple

namedtuple是继承自tuple的子类。namedtuple创建一个和tuple类似的对象，而且对象拥有可访问的属性
类似C语言中的struct
"""

from collections import namedtuple
User = namedtuple("User",["name","age","sex"])
user1 = User(name="xiafeng",age=13,sex="male")
print(user1)
print(user1.name)
print(user1.age)
print(user1.sex)
user1 =user1._replace(age=23) #修改属性#
print(user1.age)

# 将User对象转换成字典，注意要使用"_asdict"
d =user1._asdict
print(d)