country = input("where do u need to drive?")
distantion = int(input("how long ur way (km)?"))
Vmid = int(input("What is the middle speed of a car?"))
benzine = int(input("How much gasoline does a car consume for 100 km?"))
benzine2 = int(input("how much 1 liter of gasoline cost?"))

benzinecost = (distantion/benzine)
tripcost = (benzinecost*benzine2)
triptime = (distantion/Vmid)

time = (round(triptime,2))
benzinecost2 = (round(benzinecost,2))
cost = (round(tripcost,2))

print("Time for trip:", time, "hours")
print("u need", benzinecost2, "liters of benzine")
print("you need", cost, "for ur trip" )