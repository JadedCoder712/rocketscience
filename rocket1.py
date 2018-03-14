from ggrocket import Rocket, Planet

earth = Planet(viewscale=5)
rocket = Rocket(earth, altitude=5)
earth.run(rocket)
