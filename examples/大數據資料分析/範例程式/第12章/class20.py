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
            print('%s\'sGPA is F.'%(self.name))

def main():
    gpa0 = Gpa()
    gpa0.getGpa()
    gpa1 = Gpa('John', 82)
    gpa1.getGpa()
    print()
    gpa2 = Gpa('mary', 74)
    gpa2.getGpa()
    gpa3 = Gpa()
    gpa3.setName('Jennifer')
    gpa3.setScore(99)
    gpa3.getGpa()

main()