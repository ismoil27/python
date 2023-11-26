print('How many kilometres did you run today?')
kms = input()
miles = float(kms) / 1.60934
miles = round(miles, 2)
print(f"Your {kms}km ride was {miles}miles ")

# round(thing to round, how many decimal points)
