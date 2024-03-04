#question 1
num1=int(input("write a number: "))
num2=int(input("write a number: "))
if num1 %2 == 1 and num2 %2 == 1:
    result=(num1*num1)+(num2*num2)
    print(result)
else:
    print("calculation is not performed")




#question 2
def factorial(n):

  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers")
  if n == 0:
    return 1
  else:
    product = 1
    for i in range(1, n + 1):
      product *= i
    return product

# Example usage
number = int(input("Enter a number: "))
try:
  fact = factorial(number)
  print(f"The factorial of {number} is {fact}")
except ValueError as e:
  print(e)




#question 4
def main():
  # Get user input
  num_people = int(input("Enter the number of people: "))
  meal_cost = float(input("Enter the cost of each meal: "))
  sales_tax_percent = float(input("Enter the sales tax percentage (without %): "))
  tip_percent = float(input("Enter the tip percentage (without %): "))

  # Calculate bill details
  total_food_cost = num_people * meal_cost
  sales_tax = total_food_cost * sales_tax_percent / 100
  tip_amount = total_food_cost * tip_percent / 100
  total_bill = total_food_cost + sales_tax + tip_amount
  bill_per_person = total_bill / num_people

  # Print output
  print("\nRestaurant Bill Details:")
  print(f"- Total cost of food: ${total_food_cost:.2f}")
  print(f"- Sales tax: ${sales_tax:.2f}")
  print(f"- Tip amount: ${tip_amount:.2f}")
  print(f"- Total bill: ${total_bill:.2f}")
  print(f"- Bill per person: ${bill_per_person:.2f}")

if __name__ == "__main__":
  main()
