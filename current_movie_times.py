current_movies = {
    "Godzilla vs Kong": "11pm",
    "Mortal Kombat": "6pm",
    "Raya and the Last Dragon": "11am",
    "Nomadland": "2pm"
}

print("We're currently showing the following movies: ")
for key in current_movies:
    print(key)

movie = input("What movie would you like the current show time for?\n")
showtime = current_movies.get(movie)
if showtime == None:
    print("Movie is not available")
else:
    print(movie, "is showing at", showtime)
