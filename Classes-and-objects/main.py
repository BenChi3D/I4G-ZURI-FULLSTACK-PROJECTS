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
        self.name = change_name
        pass

    def change_age(self, change_age):
        self.age = change_age
        pass

    def add_track(self, add_track):
        self.tracks.append(add_track)
        pass

    def get_score(self):
        return self.score



Bob = Student("Bob", 26, ["FE", "BE"], 20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()  # returning the score

print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.get_score())
