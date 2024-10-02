#This program will determine the distance traveled and total points earned
# for a ski jump given the speed and hill type.
import math

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
    print("Invalid hill type, start over.")

#This line prompts the user for their speed
jumper_speed = float(input("What was your speed at the end of the ramp?"))

#These 3 lines of code do the necessary calculations to find the users distance and earned points
air_time = math.sqrt((2 * height)/9.8)
distance_traveled = jumper_speed * air_time
earned_points = 60 + (distance_traveled - par) * points_per_meter

#Lastly, these lines output the distance, points, and a different message
# depending on how many points the user scored
print("Distance:", distance_traveled)
print("Earned points:", earned_points)
if earned_points >= 61:
    print("Great job for doing better than par!")
elif earned_points < 10:
    print("What happened?")
else:
    print("Sorry you didn't go very far.")
