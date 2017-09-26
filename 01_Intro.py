# Labo 01 - basis variabelen

#print("Hello World, \n hi Arthon")
#print("1+1")


Name = input("What's your name?")
Lastname = input("What's your lastname?")
Age = input("What's your age?") #is a string

Age = int(Age) + 1
print("\nName: {0} \nLastname: {1} \nAge: {2: 10.2f}".format(Name , Lastname, Age))
