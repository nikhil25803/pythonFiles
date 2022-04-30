course={
    'php':{'duration':'2 months','fees':"10000"},
    'python':{'duration':'1 months','fees':"1000"},
    'Java':{'duration':'3 months','fees':"50000"},
}
# print(course)
print(course['php']['fees'])

for k,v in course.items():
    print(k,v['duration'],v['fees'])