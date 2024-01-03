date = input()
year=date.split("/")
year=int(date[2])
if (year% 4==0):
    print("%d is a leap year")
elif (year %100==0):
    print("%d is not a leap year")
elif (year% 400==0):
    print("%d is a leap year")
    if (year %4==0):
        printf("next leap year")
else:
    print("previous leap year")
