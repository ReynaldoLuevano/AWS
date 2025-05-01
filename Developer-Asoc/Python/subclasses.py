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

class Engineer(Employee):
    def __init__(self, name, email, hire_date):
        self.department = "Engineering"
        super().__init__(name, email, hire_date)

reynaldo = Engineer("Reynaldo", "rey@gmail.com", "01/01/2000");
print(reynaldo.department)
print(Employee.employee_count)