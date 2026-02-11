# print numbers 1-10
for i in range (1,11):
	print("Number:", i)

print("-----")

# Loop through list
scores = [85, 72, 61, 40]

for score in scores:
	if score >= 80:
		grade = "A"
	elif score >= 70:
		grade = "B"
	elif score >= 60:
		grade = "C"
	else:
		grade = "D"

	
	print(score, "->", grade)

print("-----")

#while loop
x = 5

while x > 0:
	print("Countdown:", x)
	x -= 1

print("Done!")