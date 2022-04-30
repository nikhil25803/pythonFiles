l = ['a', 0, 2]

for ele in l:
	try:
   		print("The entry is", ele) 
   		r = 1/int(ele)
   		
	except Exception as e: #Using Exception class 
   		print("Oops!", e.__class__, "occurred.") 
   		print("Next entry.")
   		print()
   		
print("The reciprocal of", ele, "is", r)