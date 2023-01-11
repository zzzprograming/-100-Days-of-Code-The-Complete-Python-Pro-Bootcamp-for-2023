#100 Days of Code, Day 2 project
#Tip Calculator
#Calcuate how much each person should pay


#program starts
print("Welcome to the tip calculator！\n")
#1. asking for the total bill
total_bill = input("What was the total bill?\n")
#2. asking what percentage tip would you like to give? 10, 12 or 15?
percentage_tip = input("What percentage tip would you like to give?\n")
#3. how many people to split the bill
number_of_people = input("How many people to split the bill\n")
#4. find the total that including the tip they picked
final_bill = float(total_bill) *(1+float(percentage_tip)/100)
#5. find the total that have been splited
after_split=final_bill/float(number_of_people)
#6. Rouding the total to two decimal place
rounded_split = round(after_split, 2)

print(f"your final bill per person:${rounded_split}0")


