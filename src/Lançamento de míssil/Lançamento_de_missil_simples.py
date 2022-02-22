from vpython import * 
from math import sin, cos, sqrt
from scipy.optimize import newton

class airplane:
    speed = 10 # Sign sensitive!
    def __init__(self, initial_position):
        self.position = initial_position
        self.velocity = vector(airplane.speed,0,0)
        self.acceleration = vector(0,0,0)
        
        # Visualization
        self.vpython_obj = sphere(radius=2, pos=self.position) 
        
    def update_position(self, dt):
        self.position += self.velocity * dt 
        self.vpython_obj.pos = self.position
        
class missile:
    speed = 30 # Sign sensitive!
    def __init__(self, initial_position):
        self.position = initial_position
        self.velocity = vector(0,0,0) 
        self.launched = False
        
        # Visualization
        self.vpython_obj = sphere(radius=1, pos=self.position, make_trail=True)  
        
    def hit(self, target):
        epsilon = 1
        return (target.position - self.position).mag < epsilon
    
    @staticmethod
    def calculate_angle(alpha, x, y, airplane_speed, missile_speed):
        return cos(alpha) - x/y*sin(alpha) - airplane_speed/missile_speed
        
    def launch(self, target : airplane):
        # Calculate trajectory to target
        angle = newton(self.calculate_angle, pi/4, 
                       args=(target.position.x, target.position.y, airplane.speed, missile.speed)
                       )
        
        self.velocity = vector(missile.speed * cos(angle), missile.speed * sin(angle), 0)
        self.launched = True
        return angle
    
    def update_position(self, dt):
        self.position += self.velocity * dt 
        self.vpython_obj.pos = self.position 
        
class ground:
    def __init__(self, size):
        self.obj = box(pos=vector(0,0,0), width=size, height=0.1, length=size)
    
a = airplane(vector(0,40,0))
m = missile(vector(0,0,0))
ground(200)

dt = 0.01
while True:
    rate(1/dt)
    a.update_position(dt)
    m.update_position(dt)
    
    if abs(a.position.x) > 15 and not m.launched:
        m.launch(a)
        
    if m.hit(a):
        a.vpython_obj.color = color.red
        print(f"Intersection at: ({m.position.x}, {m.position.y})")
        break