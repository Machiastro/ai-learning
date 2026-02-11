def get_grade(score):
	if score >= 80:
		return "A"
	elif score >= 70:
		return "B"
	elif score >= 60:
		return "C"
	else:
		return "D"

def main():
	scores = [85, 72, 61, 40]
		
	for s in scores:
		grade = get_grade (s)
		print(f"Score {s} → Grade {grade}")

main()