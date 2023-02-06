#Jason Galvao
#CS 175-01L
#restaurants V2
keepGoing = "yes"
while keepGoing == "yes":
    vegetarian=False
    vegan=False
    glutenFree=False

    vegetarianInput = input("Is anyone in your party a vegetarian(yes/no)?")
    if vegetarianInput == "yes":
        vegetarian=True
    
    veganInput = input("Is anyone in your party a vegan(yes/no)?")
    if veganInput == "yes":
        vegan=True

    glutenFreeInput = input("Is anyone in your party gluten free(yes/no)?")
    if glutenFreeInput == "yes":
        glutenFree=True
            

    if vegetarian==False and vegan==False and glutenFree==False:
        print("Joe's Gourmet Burgers")
    elif vegetarian==True and vegan==False and glutenFree==False:
        print("Mama's Fine Italian")
    elif vegetarian==True and vegan==False and glutenFree==True:
        print("Main Street Pizza")

    print("Corner Cafe")
    print("Chef's Kitchen")

    keepGoing = input("Do you want to keep going(yes/no)?")
