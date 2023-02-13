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
            movie = Movie(movie_name)
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

# The Shawshank Redemption
# The Godfather
# The Lord of the Rings: Return of the King
# Saving Private Ryan
# The Green Mile
