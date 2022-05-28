class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score =score

    def change_name(self, name):
        self.change_name = name

    def change_age(self, age):
        self.change_age = age

        pass



Bob = Student("Bob", 26, ["FE","BE"],20.90)
Bob = Student("Peter", 34, "UI/UX", ())
# Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()

print(Bob.change_name)
print(Bob.age)
print(Bob.change_name)