print("Welcome to tip calculator")
bill=float(input("What was the total bill : $"))
tip_percent=int(input("What percentage tip would you like to give? 10, 12, or 15 ? "))
persons=int(input("How many people to split the bill? : "))

total_bill=bill+(bill*tip_percent)/100
share=round(total_bill/persons,2)

print(f"Each person should pay ${share}")

