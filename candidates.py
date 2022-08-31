class Candidates:
    def __init__(self, name, pk, position, picture, skills):
        self.name = name
        self.pk = pk
        self.position = position
        self.picture = picture
        self.skills = skills

    def __repr__(self):
        return f"{self.name} \n {self.position} \n {self.skills}"

