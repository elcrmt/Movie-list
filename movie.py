


import logger

movie_list = {}

def create_movie(name, genre, favorite):
    """
    Creates a movie to be added in the movie list.
    :param name: the name of the movie
    :param is_favorite: True if the movie is favorite
    :return: A dictionary with all the contact data
    """
    movie = {
        'name': name,
        'genre': genre,
        'favorite': favorite,
    }
    logger.log(f'Create movie={movie}')
    return movie


def add_movie(movie):
    """
    Adds a movie to the movie list.
    If the movie already exists, the movie is not added.
    :param movie: the movie to be added
    """
    name = movie['name']

    if name in movie_list.keys():
        logger.log(f'Add movie failed. Movie already in movie list')
        return

    logger.log(f'Add movie={movie}')
    movie_list[name] = movie

def delete_movie(movie_name):
    """
    Deletes a movie from the given movie name.
    :param movie_name: name of the movie to be deleted
    :return: None, simply deletes the movie from the movie list
    """
    try:
        movie = movie_list[movie_name]
        logger.log(f'Delete movie={movie}')
        del movie_list[movie_name]
    except KeyError as e:
        logger.log(f'Film non trouve pour le nom {movie_name}')
        return 


def get_names():
    """
    Retrieves an alphabetically sorted list of all the movies names of the movie list.
    :return: the sorted list of movie names
    """
    logger.log('Display alphabetically sorted list of all the movies names')
    return sorted(movie_list.keys())


def display_all():
    """
    Display all the movies of the movie list
    """
    logger.log('Display all')
    for movie_name, movie in movie_list.items():
        print(f'{movie_name}={movie}')


def get_genres():
    """
    Returns a dictionnary of genres in the movie list
    """
    res = {}
    for name, movie in movie_list.items():
        genre = movie['genre']
        res[genre] = res.get(genre, 0) + 1
    return res

def get_favorites():
    """
    Returns an alphabetically sorted list of favorite movies
    """
    res = []
    for name, movie in movie_list.items():
        if movie['favorite']:
            res.append(name)
    res.sort()
    return res

def get_names_by_genre(genre):
    """
    Returns an alphabetically sorted list of movies for the given genre
    """
    res = []
    for name, movie in movie_list.items():
        if movie['genre'] == genre:
            res.append(name)
    return sorted(res)


nouveau_film = create_movie('Fight Club', 'Action, Suspense', True)
if nouveau_film:
    add_movie(nouveau_film)

nouveau_film = create_movie('Star Wars', 'Action', True)
if nouveau_film:
    add_movie(nouveau_film)

nouveau_film = create_movie('Ca', 'Horreur', False)
if nouveau_film:
    add_movie(nouveau_film)

nouveau_film = create_movie("Top Gun", "Science fiction", True)
if nouveau_film:
    add_movie(nouveau_film)

nouveau_film = create_movie("The Dark Knight", "Action", True)
if nouveau_film:
    add_movie(nouveau_film)

nouveau_film = create_movie("La La Land", "Musical", False)
if nouveau_film:
    add_movie(nouveau_film)

#delete_movie('Star Wars')

trie_nom_film = get_names()
print("\nListe alphabétique des noms de films :")
print(trie_nom_film)

display_film_all = display_all()
print("\nListe de tous les films :")
display_all()

get_genre_film = get_genres()
print("\nListe de films avec genre :")
for genre, count in get_genre_film.items():
    print(f"{genre}: {count} films")

get_fav_movies = get_favorites()
print("\nListe alphabétique des films favoris :")
print(get_fav_movies)

genre_to_search = 'Action'
names_by_genre = get_names_by_genre(genre_to_search)
print(f"\nListe alphabétique des noms de films pour le genre '{genre_to_search}':")
print(names_by_genre)

display_all()



