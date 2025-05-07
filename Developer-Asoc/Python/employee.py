class Employee:
    employee_count = 0

    def __init__(self, name, email, hire_date):
        self.name = name
        self.email = email
        self.hire_date = hire_date
        Employee.employee_count += 1
        
        self.posts = [] #initiates list to hold user posts
        
    def post_message(self, message):
        new_post = Post(message, self.name)
        self.posts.append(new_post)

class Post:
    def __init__(self,message, author):
        self.message = message
        self.author = author
        self.comments = []
    
    def edit(self, message):
        self.message = message
    
    def __str__(self):
        return self.message
    
    def __repr__(self):
        return f"La representación del objeto es {self.message}"

post1 = Post("Hola", "Reynaldo")
print(post1)
print(post1.__repr__())

sandra =  Employee("Sandra", "sandra@gmail.com", "01/Jan/2000")
sandra.post_message("Hola")
sandra.post_message("y adios")

print(sandra.posts)

class Comment:
    def __init__(self, employee, post, comment):
        self.comment = comment
        self.employee = employee
        self.post = post