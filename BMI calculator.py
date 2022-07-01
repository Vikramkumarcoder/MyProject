weight = float(input("Weight (kg):\n")) 
height = float (input("Height (m):\n") ) 

if (weight/((height)**2))<18.5:
    print(" You are:\"Underweight\"\n", "BMI =", (weight/((height)**2)))

elif 25>(weight/((height)**2))>=18.5:
    print(" You are:\"Normal\"", " BMI=",(weight/((height)**2)))

elif 25<=(weight/((height)**2))<30:
    print("You are:\"Overweight\"", "BMI=",(weight/((height)**2)))

elif (weight/((height)**2))>=30:
    print("You are:\"Obesity\"\n","BMI=",(weight/((height)**2)))