class Student:
    def __init__(self, prenom, nom, num, credits=0):
        self.__prenom = prenom
        self.__nom = nom
        self.__num = num
        self.__credits = credits
        self.__level = self.__studentEval()

    def enter_name(self):
        return self.__prenom

    def enter_lastname(self):
        return self.__nom

    def enter_credits(self):
        return self.__credits

    # retourne le niveau de l'étudiant
    def __studentEval(self):
        message = "Insuffisant"
        if self.enter_credits() >= 90:
            message = "Excellent"
        elif self.enter_credits() >= 80:
            message = "Très bien"
        elif self.enter_credits() >= 70:
            message = "Bien"
        elif self.enter_credits() >= 60:
            message = "Passable"
        return message

    # affiche les infos de l'étudiant
    def studentInfo(self):
        print("nom =", self.__prenom)
        print("prénom =", self.__nom)
        print("id =", self.__num)
        self.__level = self.__studentEval()
        print("niveau =", self.__level)

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits


John = Student("John", "Doe", 158)
John.add_credits(29)
John.add_credits(-12)
John.add_credits(1)

print("Le nombre de credits de", John.enter_name(), John.enter_lastname(), "est de", John.enter_credits(), "points")

John.studentInfo()