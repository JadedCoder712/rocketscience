from ggrocket import Rocket, Planet
from math import radians, sqrt
from ggmath import Slider

earth = Planet()

Re = 6.3761E6
Me = 5.972E24
G = 6.674E-11

Ve=sqrt(2*Me*G/Re)
print("Predicted escape velocity is ", Ve, " m/s")
tz = Slider((10,400), 0, 3, 0, positioning="physical")

rocket = Rocket(earth, heading=radians(90), directiond=90, velocity=Ve, timezoom=tz)
earth.run(rocket)
