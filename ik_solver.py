import math

print("ROBOTIC ARM KINEMATICS")

x = 0.4
y = 0.2

theta = math.degrees(math.atan2(y, x))

print("Target Coordinate:")
print("X =", x)
print("Y =", y)

print("Joint Angle:")
print(theta)