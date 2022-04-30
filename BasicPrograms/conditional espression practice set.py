#Find the maximum values among 4 enteries
'''
p1=int(input("Enter the value1 :"))
p2=int(input("Enter the value2 :"))
p3=int(input("Enter the value3 :"))
p4=int(input("Enter the value4 : "))

values=[p1, p2, p3,p4]
print(values)

c=max(values)
print(c)
'''

#using conditional statements methods
'''
p1=int(input("Enter the value1 :"))
p2=int(input("Enter the value2 :"))
p3=int(input("Enter the value3 :"))
p4=int(input("Enter the value4 : "))

if(p1>p4):
    f1=p1
else:
    f1=p4

if(p2>p3):
    f2=p2
else:
    f2=p3
if(f1>f2):
    print(str(f1)+ "is the greatest")
else:
    print(str(f2)+ "is the greatest")
'''

'''
Q.Write a program to find that a student is pass or fail depending on the 40%
total percentage and 33% subject wise percentage to pass the exam
'''
#Solution
'''

sub1=int(input("Enter your Marks: "))
sub2=int(input("Enter your Marks: "))
sub3=int(input("Enter your Marks: "))

    
if(sub1<33 or sub2<33 or sub3<33):
    print("Sorry! You are Failed")
elif((sub1+sub2+sub3)/3<40):
    print("Sorry! you are Failed")
else:
    print("Congratulations! You are Passed")

'''

#Write a program to detect spams which contains several words

'''
text=str(input("Enter the text "))

if("make a lot of money" in test):
    spam=True
elif("buy now" in text):
    spam=True
elif("click this" in text):
    spam=True
elif("subscribe this" in text):
    spam=True
else:
    spam=False

if(spam):
    print("This is spam")
else:
    print("This is not a spam")

'''

#Q. write a program to collect the grade of a student and grade the up as
#90-100=EX
#80-90=A
#70-80=B
#60-70=C
#50-60=D

'''Solution'''

sub1=int(input("Enter your marks: : "))

if(sub1>=90):
    grade="Ex"
elif sub1>=80:
    grade="A"
elif sub1>=70:
    grade="B"
elif sub1<=60:
    grade="C"
else:
    print("You are Failed")

print("Your grade is " + grade)
















































