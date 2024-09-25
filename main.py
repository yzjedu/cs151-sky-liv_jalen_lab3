#This program will determine the distance traveled and total points earned for a ski jump given the speed and hill type.

#
hill_type = input("Is your hill type normal or large?")

#After determining the hill type, the constants for height, points per meter, and par,
#will be set (46, 2, 90 and 70, 1.8, 120 respectively for normal and large)

if hill_type == "normal":
    height = 46
    points_per_meter = 2
    par = 90
elif hill_type == "large":
    height = 70
    points_per_meter = 1.8
    par = 120
else:
    print("Invalid hill type, try again.")
