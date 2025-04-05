def d():
    animal = "elephant"
    
    def e():
        nonlocal animal
        animal = "dog"
        print("Inside nested function: " + animal)
    
    print("Before nested function: " + animal)
    e()
    print("After nested function: " + animal)

animal = "cat"
d()
print("Global variable: " + animal)

    
    