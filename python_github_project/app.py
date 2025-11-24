print("welcome to my Python program!") 

hours = input("How many hours did you study today?") # This will be where the userinserts their hours for their average daily hourly studying

try: 

    hours = float(hours) 

except ValueError: 

    print("Please enter a valid number") 

    exit() # This will ensure the the value inserted is correctly inputted 

weekly_hours = hours * 7 

print(f"You are on track to study {weekly_hours} hours this week.") 

 

 
