
ale = 71
age = int(input('How old are you?'))

print('ale == age :', ale == age)
print('ale != age :', ale != age)
print('ale < age :', ale < age)
print('ale > age :', ale > age)
print('ale >= age :', ale >= age)
print('ale <= age :', ale <= age)


print('age % 5 == 0  : ', age % 5 == 0)

 # not and or
print('age % 5 != 0', age % 5 != 0)
print('not age % 5 == 0', not age % 5 == 0)

# and
print('age % 5 == 0 and age<ale: ',age % 5 == 0 and age < ale)

# or
print('age % 5 == 0 or age<ale: ',age % 5 == 0 or age < ale)

# priority
print((1 > 2 and (0 < 5 or 0 < 2)) and 0 == 0)