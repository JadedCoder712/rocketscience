from ggrocket import Rocket, Planet

earth = Planet(viewscale=0.0011)
rocket = Rocket(earth, altitude=161000, velocity=7810)
earth.run(rocket)
