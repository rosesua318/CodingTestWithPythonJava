a = int(input())
b = int(input())
c = b - a

if c <= 0:
    print("Congratulations, you are within the speed limit!")
elif c >= 1 and c <= 20:
    print("You are speeding and your fine is ${}.".format(100))
elif c >= 21 and c <= 30:
    print("You are speeding and your fine is ${}.".format(270))
elif c >= 31:
    print("You are speeding and your fine is ${}.".format(500))
