import os # os: operating system

class MovieCatalog:

    file_path = 'movie.txt'

    @classmethod
    def add_movie(cls, movie):
        with open(cls.file_path, 'a', encoding='utf8') as file:
            file.write(f'{movie._name}\n')

    @classmethod
    def list_movies(cls):
        with open(cls.file_path, 'r', encoding='utf8') as file:
            print(' Movie catalog '.center(50, '-'))
            print(file.read())

    @classmethod
    def delete_movies(cls):
        os.remove(cls.file_path)
        print(f'File deleted: {cls.file_path}')