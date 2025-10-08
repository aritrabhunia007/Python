#Name-Aritra Bhunia
#Course-Btech cse(fsd)
#Rollno-2501350034
print("Welcome to the Daily calorie CLI!")
print("Track your meals,calories, and compare against your daily limit")
#task-2
meal=[]
calories=[]
num_meals=int(input("Enter the number:-"))
#task-3
for i in range(num_meals):
    meal_name=input(f"Enter {i+1}th meal name:-")
    cal=float(input(f"Enter calories for {i+1}th meal:- "))
    meal.append(meal_name)
    calories.append(cal)
#task-4
total_calories=sum(calories)
avg_calories=total_calories/num_meals
daily_limit=float(input("Enter your daily calorie limit:-"))
print("\nSummary:")
for i in range(num_meals):
    print(f"{meal[i]}: {calories[i]} calories")

print(f"\nTotal Calories: {total_calories}")
print(f"Average Calories per Meal: {avg_calories}")
print(f"Daily Limit: {daily_limit}")

if total_calories > daily_limit:
    print(f"Warning: You've exceeded your daily calorie limit by {total_calories - daily_limit} calories.")
else:
    print(f"You've got {daily_limit - total_calories} calories left for the day.")
