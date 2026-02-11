def check_score(score):
	if score >= 60:
		return "PASS"
	else:
		return "FAIL"

result = check_score(40)

print("Result is: ", result)