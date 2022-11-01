
WeightInKilograms=int(input())
HeightInMeters=float(input())
BMI=WeightInKilograms/(HeightInMeters**2)
#BMI=round(BMI,2)
# the second way to solve disimal number problem .
#number_1=unkown
#printing 2 disimal number after int(number_1)
BMI2="{:.2f}".format(BMI)
if BMI <18.5:
    print(BMI2)
    print("Underweight")
if 18.5<=BMI<25:
    print(BMI2)
    print("Normal")
if 25<=BMI<30:
    print(BMI2)
    print("Overweight")
if BMI >= 30:
    print(BMI2)
    print("Obese")
