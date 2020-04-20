class Gpa:
    def __init__(self, name = 'Nancy', score = 60):
        self.name = name
        self.score = score

    def setName(self, name):
        self.name = name

    def setScore(self, score):
        self.score = score    

    def getGpa(self):
        if self.score >= 80:
            print('%s\'s GPA is A.'%(self.name))
        elif self.score >= 70:
            print('%s\'s GPA is B.'%(self.name))
        elif self.score >= 60:
            print('%s\'s GPA is C.'%(self.name))
        elif self.score >= 50:
            print('%s\'s GPA is D.'%(self.name))
        else:
            print('%s\'sGPA is E.'%(self.name))