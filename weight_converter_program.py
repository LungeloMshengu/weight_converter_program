weight = float(input("Enter your weight: "))
units = input("kilograms or pounds (K or L): ").upper()

if units == "K":
	weight *= 2.205
	units = "Kgs"
	print(f"your weight is: {weight:.2f} {units}")
elif units == "L":
	weight /=2.205
	units = "Lbs"
	print(f"your weight is: {weight:.2f} {units}")
else:
	print(f"({units})is not valid units")	
