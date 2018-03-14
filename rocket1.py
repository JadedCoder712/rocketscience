from ggrocket import Rocket, Planet

earth = Planet(viewscale=0.00014, planetmass=73420000000000000000000)
rocket = Rocket(earth, altitude=100, velocity=1000, timezoom=3)
earth.run(rocket)
