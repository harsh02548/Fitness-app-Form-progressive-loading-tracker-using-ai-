import cv2
import mediapipe
import numpy

#print("AI libraries installed successfully!")

name = "Harsh"
age = 16
isLearningPython = True
money = 100.50

print(name)
print(age)
print(isLearningPython)
print(money)
age = 18
if age > 18:
    print("You are an adult.")
elif age == 18:
    print("You are exactly 18 years old.")
else:
    print("You are a minor.")

for i in range(3):
    print("hi", i)

while age < 20:
    print("You are still a minor.")
    age += 1