# user story
# add new movie to my collection to keep track of all movies
# list all the movies in my collection
# see what movies they already have
# find a movie by using the movie title

# implementation tasks:
# decide where to store movies in code
# what data we want to store for each movie
# create a menu
# implement each requirement each as a separate function
# stop running the program

# store in a python list for now beacuse we haven't looked at databases

menu = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

# what we store for each movie maybe dictionary or tuple
# we will create a dictionary for each movie
# in the dictionary it will store movie title, director and release year

def add_movie():

    title = input("enter movie name: ")
    director = input("enter movie director: ")
    year = input("enter year released: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })
def show_movie():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"title: {movie['title']}")
    print(f"director: {movie['director']}")
    print(f"year: {movie['year']}")


def find_movie():
    search_title = input("Enter movie title you are looking for: ")
    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)
# show the user menu
# get the users input
# then run a loop and get their input again at the end

user_options = {
    "a": add_movie,
    "l": show_movie,
    "f": find_movie
}




def menu():

    selection = input(menu)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()

        else:
            print("command unrecognised, try again")

        selection = input(menu)
menu()
