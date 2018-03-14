from ggrocket import Rocket, Planet
viewscale = input("Viewscale:")
altitude = input("Altitude:")
velocity = input("Velocity:")
timezoom = input("Time zoom:")
planet = input("What planet?")


earth = Planet(viewscale=0.00014)
rocket = Rocket(earth, altitude=161000, velocity=7810, timezoom=3)
earth.run(rocket)
