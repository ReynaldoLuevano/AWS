class Post:
    def __init__(self,message, author):
        self.message = message
        self.author = author
        self.comments = []
    
    def edit(self, message):
        self.message = message
