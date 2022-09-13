import math

widthTire = int(input("Enter the width of the tire in mm (ex 205): "))
ratioTire = int(input("Enter the aspect ratio of the tire (ex 60): "))
wheelDiameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volumeCar = (math.pi * (widthTire ** 2) * ratioTire * (widthTire * ratioTire + (2540 * wheelDiameter))) / 10_000_000_000

print(f"The approximate volume is {volumeCar:.2f} liters")