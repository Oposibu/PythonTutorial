## Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm, and asks them how many hours into the future they want to go. Print out what the hour will be that many hours into the future, printing am or pm as appropriate.

hour = eval(input("Enter hour between 1 and 12: "))
while hour < 0 or hour > 12:
    hour = eval(input("Enter hour between 1 and 12: "))
mon_Eve = eval(input("AM(1) or PM(2): "))
while mon_Eve != 1 and mon_Eve != 2:
    mon_Eve = eval(input("AM(1) or PM(2): "))
else:
    futureTime = eval(input("How many hours ahead?: "))
    x = hour + futureTime
    y = x % 12
    if x == 12 and mon_Eve == 1:
        print("12pm afternoon")
    elif x == 12 and mon_Eve == 2:
        print("12 am morning")
    elif x > 12 and mon_Eve == 1:
        print("New hour: ", y, "pm", sep="")
    elif x < 12 and mon_Eve == 1:
        print("New hour: ", y, "am", sep="")
    elif x > 12 and mon_Eve == 2:
        print("New hour: ", y, "am", sep="")
    elif x < 12 and mon_Eve == 2:
        print("New hour: ", y, "pm", sep="")

