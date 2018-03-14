from ggrocket import Rocket, Planet

earth = Planet(viewscale=0.00014)
rocket = Rocket(earth, altitude=161000, velocity=7810, timezoom=3)
earth.run(rocket)
