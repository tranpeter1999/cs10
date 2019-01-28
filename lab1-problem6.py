#Peter Tran
#1104985

#constants
radius = 6378000;
massPlanet = 5.9742 * 10**24;
G = 6.67300 * 10**-11;

#input
massUser = float(input("Enter your weight (kg): "));

F = (G * massPlanet * massUser)/radius**2;
g = F/massUser;

print("The resulting value of g is {:.4f} which is close to the earth's gravitational force".format(g));

##Enter your weight (kg): 50
##The resulting value of g is 9.8001 which is close to the earth's gravitational force
