from Movie import *
from movie_catalog import MovieCatalog as mc

option = None
while option !=4:
    try:
        print('Options: ')
        print('1. Add movie: ')
        print('2. List movie: ')
        print('3. Delete movie catalog ')
        print('4. Exit ')
        option = int(input('Enter your option (1-4): '))

        if option == 1:
            movie_name = input('Enter the name of the movie: ')
            movie_year = int(input('Enter the year of the movie: '))
            movie = Movie(movie_name, movie_year)
            mc.add_movie(movie)
        elif option == 2:
            mc.list_movies()
        elif option == 3:
            mc.delete_movies()

    except Exception as e:
        print(f'An error occurred. {e}')
        option = None
else:
    print('Exit program...')

# The Shawshank Redemption 1994
# The Godfather 1972
# The Lord of the Rings: Return of the King 2003
# Saving Private Ryan 1998
# The Green Mile 1999