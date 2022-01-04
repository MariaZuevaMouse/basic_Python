
age = int(input('How old are you?'))

# if - elif - else
if age < 18:
    print("access is denied")  # 4 space for the internal block
elif age == 18:
    print('you are 18')
else:
    print('access is allowed')
    if age % 5 == 0:
        print(' age % 5 == 0')  # 8 spaces



print('end')