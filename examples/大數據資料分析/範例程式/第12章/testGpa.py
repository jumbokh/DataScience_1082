from gpa import Gpa
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