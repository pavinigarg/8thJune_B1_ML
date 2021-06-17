Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #ques 2
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a = 20; a+= 30; a%=3; print(a)
2
>>> True*False
0
>>> True&False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True==False)or(False>True))and(False<=True)
False
>>> #####################
>>> #ques 3
>>> 
>>> s1="Nice to have it"
>>> s2="here"
>>> s=s1+" "+s2
>>> print(s)
Nice to have it here
>>> #####################
>>> #ques 4
>>> 
>>> a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][-1]
['hello']
>>> a[3][1][-1][0]
'hello'
>>> #####################
>>> #ques 5
>>> a.insert(0,s1)
>>> a.append(s2)
>>> print(a)
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> #####################
>>> #ques 6
>>> 
>>> color_list_1 = set(["White", "Black", "Red"])
>>> color_list_2 = set(["Red", "Green"])
>>> print(color_list_1.difference(color_list_2))
{'Black', 'White'}
>>> #####################
>>> #ques 7
>>> 
>>> strr=input("Enter the string:")
Enter the string:The five boxing wizards jump quickly
>>> strr.lower()
'the five boxing wizards jump quickly'
>>> sett=set(strr)
>>> sett.remove(' ')
>>> if len(sett)==26:
	print("String is pangram")
    else:
        print("String is not pangram")

String is pangram
>>> #####################
>>> #ques 8
>>> num=eval(input('enter a no:'))
enter a no:5
>>> t='{0}+{0}{0}+{0}{0}{0}'.format(num)
>>> print(t)
5+55+555
>>> #####################
>>> #ques 9
>>> S=input("enter some words: ")
enter some words: without,hello,bag,world
>>> T=S.split(',')
>>> T.sort()
>>> T
['bag', 'hello', 'without', 'world']
>>> #####################
>>> #ques 10
>>> d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 
'Marks': [57,87,67,79]}
>>> print(d['Student'][d['Marks'].index(max(d['Marks']))])
Kishore
>>> 