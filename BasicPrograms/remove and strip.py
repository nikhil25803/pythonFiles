'''

this="      Nikhil is"
print(this)
print(this.strip())
'''

#Using def function

def remove_strip(string,word):
    newStr=string.replace(word,"")
    return newStr.strip()

this="      nikhil is a good    "
n=remove_strip(this,"nikhil")
print(n)