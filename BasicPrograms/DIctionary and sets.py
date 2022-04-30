myDict={
"Fast": "Ina aquick manner",
"Nikhil": "A good Coder",
"Marks":[1,8,9],
1:2
    }

print(myDict['Nikhil'])
print(myDict['Marks'])

print(myDict.keys())

print(myDict.values())

print(myDict.items())

# To add an updated

print(myDict)
updateDict={
 "Rohan": "Friend"
    }
myDict.update(updateDict)
print(myDict)

print(myDict.get("Nikhil2")) # will return none if key is not present in dictionary 
