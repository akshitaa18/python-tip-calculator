print("welcome to the tip calculator!")
total=float(input("what was the total bill? $"))
tip=int(input("how much tip would you like to give? 10,12,15? "))
split=int(input("how many people to split the bill? "))
tip_percent=tip/100
total_tip=total*tip_percent
final_bill=total+total_tip
final_split=final_bill/split
print(f"Each person should pay: ${final_split:.2f}")