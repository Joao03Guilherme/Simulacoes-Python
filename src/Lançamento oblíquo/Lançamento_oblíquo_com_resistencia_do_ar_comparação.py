from vpython import *

g = vector(0,-10,0) # Gravitational acceleration

class ground:
    def __init__(self, size):
        self.vpython_obj = box(pos=vector(0,0,0), size=vector(size,0.01,size/10))

class ball:
    def __init__(self, mass, radius, drag_coef, initial_position, initial_velocity, initial_acceleration):
        self.mass = mass
        self.radius = radius 
        self.drag_coef = drag_coef # Dummy units
        self.position : vector = initial_position
        self.velocity : vector = initial_velocity
        self.acceleration : vector = initial_acceleration
        
        self.vpython_obj = sphere(radius=radius, pos=initial_position, color=color.red, make_trail=True)
     
    def update_acceleration(self, dt):
        drag_force = - self.drag_coef * self.velocity.mag2 * self.velocity.norm() # Simple drag force
        gravitational_force = self.mass * g 
        net_force = drag_force + gravitational_force
        
        self.acceleration = net_force / self.mass
           
        
    def update_position(self, dt):
        self.position += self.velocity * dt 
        self.velocity += self.acceleration * dt 
        
        self.vpython_obj.pos = self.position
        self.update_acceleration(dt)
        
b1 = ball(1, 1, 0.002, vector(-250,0,0), vector(50,50,0), g)
b2 = ball(1, 1, 0, vector(-250,0,0), vector(50,50,0), g)      
ground(600)

dt = 0.001
while b1.position.y >= 0 or b2.position.y >= 0:
    rate(1/dt)
    if b1.position.y >= 0:
        b1.update_position(dt)
    if b2.position.y >= 0:
        b2.update_position(dt)