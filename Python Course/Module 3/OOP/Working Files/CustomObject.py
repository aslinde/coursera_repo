class NewClass():
    print("Who wrote this")
    index = "Author-Book"
    def hand_list(self, philosopher, book):
        print(NewClass.index)
        print(philosopher + " wrote the book: " + book)

whodunnit = NewClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")

#### With _init_ to avoid double Instantiation so that Who Wrote this isn't printed twice in some cases
class MyFirstClass:
    index = "Author-Book"

    def __init__(self):
        print("Who wrote this?")  # Move the print statement into the constructor

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)

# Instantiate the class
whodunnit = MyFirstClass()
# Call the method with parameters
whodunnit.hand_list("Sun Tzu", "The Art of War")


class MyFirstClass1:
    index = "Author-Book"

    def __init__(self, philosopher, book):
        print("Who wrote this?")  # Move the print statement into the constructor
        self.philosopher = philosopher
        self.book = book    #### You're defining variables that are apart of the class itself rather than temporary method variables 
                            #### they that's why they have to have the self key word to actually initialize them as class variables and object not temporary
    def hand_list(self):
        print(MyFirstClass1.index)
        print(self.philosopher + " wrote the book: " + self.book) 

# Instantiate the class
whodunnit = MyFirstClass1("Sun Tzu", "The Art of War")
# Call the method with parameters
whodunnit.hand_list()