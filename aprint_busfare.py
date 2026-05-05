def busfare(distance):
    fare=0
    if distance <=10:
        fare= 80
    elif distance >10 and distance<20:
        fare = 80+ (distance - 10) * 6
    elif distance > 20 and distance<30:
        fare = 80+(10*6)+ (distance - 20)*5
    elif distance > 30:
        fare = 80 + (10*6)+(10*5)+(distance-30)*4
    return fare
distance1 = float(input("enter distance you're traveling"))
print(busfare(distance1))

