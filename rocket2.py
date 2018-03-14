from ggrocket import Rocket, Planet
from math import radians

earth = Planet()

Re = 6.3761E6
Me = 5.972E24
G = 6.674E-11

Ve=sqrt(2*Me*G/Re)
print("Predicted escape velocity is ", Ve, " m/s")

rocket = Rocket(earth, heading=radians(90), directiond=90, velocity=10)
earth.run(rocket)
