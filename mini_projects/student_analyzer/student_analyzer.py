def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

def get_average(scores):
    return sum(scores) / len(scores)

def get_scores():
    scores = []
    
    while True:
            user_input = input("Enter score (q to quit): ")
            
            if user_input.lower() == "q":
                break
                
            try:
                score = float(user_input)
                
                if score < 0 or score > 100:
                    print("Score must be between 0 and 100")
                    continue
                    
                scores.append(score)
                
            except ValueError:
                print("Invalid input. Please enter a number.")
                
    return scores
 
 #test area
 
def main():
    scores = get_scores()
    
    if not scores:
        print("No scores entered.")
        return
        
    avg = get_average(scores)
    grade = get_grade(avg)
    
    print("\n--- Report ---")
    print("Scores:", scores)
    print("Average:", round(avg, 2))
    print("Final Grade:", grade)
    
if __name__ == "__main__":
    main()