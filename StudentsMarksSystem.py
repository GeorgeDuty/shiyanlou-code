numberOfStudents = int(input("Please Input the Number Of Students: "))
data = {}
subject = ('Chinese','Maths','English')
for i in range(0,numberOfStudents):
	name = input("Please Input Student name: ")
	marks = []
	for j in subject:
		marks.append(int(input("Pleast Input The Marks Of {}: ".format(j))))
		data[name] = marks
for i,j in data.items():
	total = sum(j)
	print("The Total Marks Of Student {} is : {} ".format(i,total))
	avrage = total/3.0
	if avrage<60 :
		print("Studen {} avrage marks is {}, is failed".format(i,avrage))
	else :
		print("Studen {} avrage marks is {}, is passed".format(i,avrage))
print(len(subject))
