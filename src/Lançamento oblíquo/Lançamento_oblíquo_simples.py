from vpython import *

class ground:
    def __init__(self, size):
        self.vpython_obj = box(pos=vector(0,0,0), size=vector(size,0.01,size/10))

class ball:
    def __init__(self, mass, radius, initial_position, initial_velocity, initial_acceleration):
        self.mass = mass
        self.radius = radius 
        self.position : vector = initial_position
        self.velocity : vector = initial_velocity
        self.acceleration : vector = initial_acceleration
        
        self.vpython_obj = sphere(radius=radius, pos=initial_position, color=color.red, make_trail=True)
        
    def update_position(self, dt):
        self.position += self.velocity * dt 
        self.velocity += self.acceleration * dt 
        
        self.vpython_obj.pos = self.position

g = vector(0,-10,0) # Gravitational acceleration
b = ball(1, 1, vector(-250,0,0), vector(50,50,0), g)    
ground(600)

dt = 0.001
while b.position.y >= 0:
    rate(1/dt)
    b.update_position(dt)