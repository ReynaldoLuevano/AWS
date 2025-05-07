class Employee1:
    pass


class Bike:
    wheels = 2
   
    def __init__(self,frame_size, color):
        self.frame_size = frame_size
        self.color = color
    
    def ring_bell(self):
        print('ring!, ring!')

myBike = Bike(45,'red')
myBike.ring_bell()

#inspecting object attributes
#for i in dir(myBike): 
 #   print(i)

class Employee:
    employee_count = 0

    def __init__(self, name, email, hire_date):
        self.name = name
        self.email = email
        self.hire_date = hire_date
        Employee.employee_count += 1
        
        self.posts = [] #initiates list to hold user posts
        
    def post(self, content):
        new_post = content
        self.posts.append(new_post) 

e1 = Employee("Mary Major", "mary.major@example.com", "07/12/2021")

e1.post("I learned a new skill!")
e1.post("I'm having a great day!")
e1.post("Ask me about learning Python")

print (e1.posts)