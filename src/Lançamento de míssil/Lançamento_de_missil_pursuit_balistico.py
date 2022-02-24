from vpython import * 

# NOT FINISHED
"""
class balistic_missile:
    speed = 20 # Sign sensitive!
    def __init__(self, initial_position):
        self.position = initial_position
        self.velocity = vector(balistic_missile.speed,0,0)
        self.acceleration = vector(2,1.7,0)
        
        # Visualization
        self.vpython_obj = sphere(radius=2, pos=self.position) 
        
    def update_position(self, dt):
        self.position += self.velocity * dt 
        self.velocity += self.acceleration * dt
        self.vpython_obj.pos = self.position
        
class missile:
    speed = 45 # Sign sensitive!
    def __init__(self, initial_position):
        self.position = initial_position
        self.velocity = vector(0,0,0) 
        self.launched = False
        
        # Visualization
        self.vpython_obj = sphere(radius=1, pos=self.position, make_trail=True)  
        
    def hit(self, target):
        epsilon = 1
        return (target.position - self.position).mag < epsilon
        
    def launch(self):
        self.launched = True
    
    def update_position(self, target : airplane, dt):
        self.position += self.velocity * dt 
        self.vpython_obj.pos = self.position 
        
        if self.launched:
            self.velocity = missile.speed * (target.position - self.position).hat
            
class ground:
    def __init__(self, size):
        self.obj = box(pos=vector(0,0,0), width=size, height=0.1, length=size)
    
a = airplane(vector(0,80,0))
m = missile(vector(0,0,0))
ground(400)

dt = 0.01
while True:
    rate(1/dt)
    a.update_position(dt)
    m.update_position(a, dt)
    
    if abs(a.position.x) > 50 and not m.launched:
        m.launch()
        
    if m.hit(a):
        a.vpython_obj.color = color.red
        print(f"Intersection at: ({m.position.x}, {m.position.y})")
        break
"""