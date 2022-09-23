from datetime import datetime
import math

current_date_and_time = datetime.now()

widthTire = int(input("Enter the width of the tire in mm (ex 205): "))
ratioTire = int(input("Enter the aspect ratio of the tire (ex 60): "))
wheelDiameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volumeCar = (math.pi * (widthTire ** 2) * ratioTire * (widthTire * ratioTire + (2540 * wheelDiameter))) / 10_000_000_000

print(f"The approximate volume is {volumeCar:.2f} liters")

with open("volumes.txt", mode="at") as volumesFile:
  firstQ = input("Do you want to buy tires with this dimensions? (Y/N) ")

  if firstQ.upper() == "Y":
    phoneNumber = int(input("What is your phone number? (Just Numbers) "))

    print(f"{current_date_and_time:%Y-%m-%d}, {widthTire}, {ratioTire}, {wheelDiameter}, {volumeCar:.2f}, {phoneNumber}", file=volumesFile)

    print()
    print("Saved information successfully!")
  else:
   print(f"{current_date_and_time:%Y-%m-%d}, {widthTire}, {ratioTire}, {wheelDiameter}, {volumeCar:.2f}", file=volumesFile)

   print()
   print("Saved information successfully!")

    
      
    




# print(f"{current_date_and_time:%Y-%m-%d}, {widthTire}, {ratioTire}, {wheelDiameter}, {volumeCar:.2f}", file=volumesFile)