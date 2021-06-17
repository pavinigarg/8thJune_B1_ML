#ques 2
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a=20
a+=30
a%=3
print(a)
print(True * False)
print(True & False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
#print(False in 'False')    gives error
print(((True == False) or (False > True)) and (False <= True))

#ques 3
s1="Nice to have it"
s2="here"
s=s1+" "+s2
print(s)

#ques 4
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a[3][1][-1][0]

#ques 5
a.insert(0,s1)
a.append(s2)
print(a)

#ques 6
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

#ques 7
strr=input("Enter the string:")
strr.lower()
sett=set(strr)
sett.remove(' ')
if len(sett)==26:
  print("String is pangram")
else:
  print("String is not pangram")

#ques 8
num=eval(input('enter a no:'))
t='{0}+{0}{0}+{0}{0}{0}'.format(num)
print(t)

#ques 9
S=input("enter some words: ")
T=S.split(',')
T.sort()
T

#ques 10
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 
'Marks': [57,87,67,79]}
print(d['Student'][d['Marks'].index(max(d['Marks']))])
