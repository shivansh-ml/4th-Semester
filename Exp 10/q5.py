class Movie:
    def __init__(self, title, actor, actress):
        self.title = title
        self.actor = actor
        self.actress = actress
    
    def display(self):
        print(f"Title: {self.title}, Actor: {self.actor}, Actress: {self.actress}")

movies = []
while True:
    title = input("Enter movie title: ")
    actor = input("Enter actor name: ")
    actress = input("Enter actress name: ")
    movies.append(Movie(title, actor, actress))
    cont = input("Do you want to add another movie? (Yes/No): ")
    if cont.lower() == "no":
        break

for movie in movies:
    movie.display()