def get_status(avg):
    if avg > 100000:
        return "LAVISH"
    elif avg > 50000:
        return "NORMAL"
    else:
        return "FRUGAL"
 
def get_average(expenses):
     return sum(expenses) / len(expenses)
     
def get_expenses():
     expenses = []
     
     while True:
            user_input = input("Enter Expense(q to exit):")
            
            if user_input.lower() == "q":
                break
             
            try:
                expense = float(user_input)
                
                expenses.append(expense)
                
            except ValueError:
                print("Invalid input. Please enter expense")
      
     return expenses
      
def main():
     expenses=get_expenses()
     
     if not expenses:
         print("No expenses entered.")
         return
         
     avg = get_average(expenses)
     status = get_status(avg)
     
     print("\n--- report ---")
     print("Expense:", expenses)
     print("Average:", round(avg,2))
     print("Status:", status)
     
if __name__ == "__main__":
    main()
     