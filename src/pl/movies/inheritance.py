class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor called.")
        self.last_name= last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print ("Child Constructor called.")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

GM_LAI = Parent("LAI", "black")
print(GM_LAI.last_name)

GM_LI = Child("LI", "blue", 5)
print (GM_LI.last_name)
print (GM_LI.eye_color)
print (GM_LI.number_of_toys)