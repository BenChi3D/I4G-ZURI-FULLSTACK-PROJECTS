class Student:
    """
    This is a Student class
    """
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        pass

    def change_name(self, change_name):
        self.change_name = change_name
        pass

    def change_age(self, change_age):
        self.change_age = change_age
        pass

    def add_track(self, add_track):
        self.add_track = add_track
        pass

    def get_score(self, get_score):
        self.get_score = get_score
        pass


Bob = Student("Bob", 26, ["FE", "BE"], 20.90)
Bob = Student("Peter", 34, "UI/UX", " ")

# Expected methods
Bob.change_name("John")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(75)  # inputting a score

print(Bob.change_name)
print(Bob.change_age)
print(Bob.add_track)
print(Bob.get_score)
