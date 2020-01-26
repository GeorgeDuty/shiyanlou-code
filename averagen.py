N = 10
sum = 0
count = 0
print("Please Input 10 numbers")
while count<N:
	number = float(input())
	sum += number
	count += 1
average = sum/N
print("N = {},Sum = {}".format(N,sum))
print("Average = {:.5f}".format(average))