import logger

class Movie:
    def __init__(self, name, genre, favorite):
        self.name = name
        self.genre = genre
        self.favorite = favorite

    def __str__(self):
        return f"{self.name} - Genre: {self.genre}, Favorite: {self.favorite}"

class MovieList:
    def __init__(self):
        self.movie_list = {}

    def add_movie(self, movie):
        name = movie.name

        if name in self.movie_list.keys():
            logger.log(f'Add movie failed. Movie already in movie list')
            return

        logger.log(f'Add movie={movie}')
        self.movie_list[name] = movie

    def delete_movie(self, movie_name):
        try:
            movie = self.movie_list[movie_name]
            logger.log(f'Delete movie={movie}')
            del self.movie_list[movie_name]
        except KeyError as e:
            logger.log(f'Film non trouve pour le nom {movie_name}')
            return

    def get_names(self):
        logger.log('Display alphabetically sorted list of all the movies names')
        return sorted(self.movie_list.keys())

    def display_all(self):
        logger.log('Display all')
        for movie_name, movie in self.movie_list.items():
            print(f'{movie_name}={movie}')

    def get_genres(self):
        res = {}
        for name, movie in self.movie_list.items():
            genre = movie.genre
            res[genre] = res.get(genre, 0) + 1
        return res

    def get_favorites(self):
        res = []
        for name, movie in self.movie_list.items():
            if movie.favorite:
                res.append(name)
        res.sort()
        return res

    def get_names_by_genre(self, genre):
        res = []
        for name, movie in self.movie_list.items():
            if movie.genre == genre:
                res.append(name)
        return sorted(res)

# Utilisation des classes Movie et MovieList
movie_list_instance = MovieList()

nouveau_film = Movie('Fight Club', 'Action, Suspense', True)
if nouveau_film:
    movie_list_instance.add_movie(nouveau_film)

nouveau_film = Movie('Star Wars', 'Action', True)
if nouveau_film:
    movie_list_instance.add_movie(nouveau_film)

nouveau_film = Movie('Ca', 'Horreur', False)
if nouveau_film:
    movie_list_instance.add_movie(nouveau_film)

nouveau_film = Movie("Top Gun", "Science fiction", True)
if nouveau_film:
    movie_list_instance.add_movie(nouveau_film)

nouveau_film = Movie("The Dark Knight", "Action", True)
if nouveau_film:
    movie_list_instance.add_movie(nouveau_film)

nouveau_film = Movie("La La Land", "Musical", False)
if nouveau_film:
    movie_list_instance.add_movie(nouveau_film)

# Supprimer un film
# movie_list_instance.delete_movie('Star Wars')

# Récupérer et afficher les données
trie_nom_film = movie_list_instance.get_names()
print("\nListe alphabétique des noms de films :")
print(trie_nom_film)

print("\nListe de tous les films :")
movie_list_instance.display_all()

get_genre_film = movie_list_instance.get_genres()
print("\nListe de films avec genre :")
for genre, count in get_genre_film.items():
    print(f"{genre}: {count} films")

get_fav_movies = movie_list_instance.get_favorites()
print("\nListe alphabétique des films favoris :")
print(get_fav_movies)

genre_to_search = 'Action'
names_by_genre = movie_list_instance.get_names_by_genre(genre_to_search)
print(f"\nListe alphabétique des noms de films pour le genre '{genre_to_search}':")
print(names_by_genre)

# Afficher tous les films
movie_list_instance.display_all()
