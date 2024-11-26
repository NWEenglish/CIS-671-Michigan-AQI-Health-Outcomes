class Visualization:
    def __init__(self, id = None, name = None, visual = None, data = None):
        self.id = id
        self.name = name 
        self.visual = visual
        self.data = data 

    def set_data(self, data):
        self.data = data  

    def get_id(self):
        return self.id 

    def get_name(self):
        return self.name 

    def get_visual(self):
        return self.visual 

  

    
