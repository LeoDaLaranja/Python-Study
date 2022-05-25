print("Today's date ")
today = input()
print("Breakfast calories")
breakfast = float(input())
print("Lunch Calories")
lunch = float(input())
print("Dinner calories")
dinner = float(input())
print("Snack calories? ")
snack = float(input())
sum = breakfast+lunch+dinner+snack

print("Calorie content for "+ today + ": " +str(sum))