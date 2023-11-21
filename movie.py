#def say_hello(name):
    #return (f"Hello {name} !")

#name = "Eliott"
#print(say_hello(name))


#for i in range(501):
    #print(i)

#somme = 0

#for i in range(1001):
    #somme = somme + i
    #print(somme)

#nombre = int(input("Entrez n'importe quel nombre :"))
#if (nombre % 2) == 0:
    #print(nombre, "est paire")

#else:
    #print(nombre, "est impaire")


#liste = [3, 4, 5, 6]

#moy = sum(liste) / len(liste)
#print(moy)


#def afficher_nombres(nombre):
    #for i in range(1, nombre + 1):
     #   if i > 500:
    #        break  
   #     if i % 5 == 0:
  #          continue 
 #       print(i)

#nombre = 600

#afficher_nombres(nombre)

#def compter_voyelles(mot):
    #voyelles = "aeiouyAEIOUY"
    #nombre_voyelles = 0

    #for lettre in mot:
   #     if lettre in voyelles:
  #          nombre_voyelles = nombre_voyelles + 1

 #   return nombre_voyelles

#mot = input("Entrez un mot : ")
#resultat = compter_voyelles(mot)
#print(f"Le nombre de voyelles dans '{mot}' est : {resultat}")


from logger import log


films = {}

def create_movie(nom, genre, favori):
    """
    Crée un nouveau film avec les détails donnés.

    Parameters:
    nom (str): Le nom du film.
    genre (str): Le genre du film.
    favori (bool): True si le film est favori, False sinon.

    Returns:
    dict: Le film créé, ou None si le film existe déjà.
    """
    # Vérifier si le film existe déjà dans la liste
    if nom not in films:
        film = {'nom': nom, 'genre': genre, 'favori': favori}
        log(f"Création du film '{nom}' dans la liste.")
        add_movie(film)
        return film
    else:
        log(f"Echec, le film '{nom}' est déjà dans la liste.")
        return None

def add_movie(film):
    """
    Ajoute un film à la liste des films.

    Parameters:
    film (dict): Détails du film à ajouter à la liste.
    """
    nom = film['nom']
    # Vérifier si le film existe déjà dans la liste
    if nom not in films:
        films[nom] = film
        log(f"Ajout du film '{nom}' à la liste.")
    else:
        log(f"Echec, le film '{nom}' est déjà dans la liste.")

def delete_movie(nom):
    """
    Supprime un film de la liste des films.

    Parametre:
    nom (str): Le nom du film à supprimer.
    """
    try:
        del films[nom]
        log(f"Suppression du film '{nom}' de la liste.")
    except KeyError:
        log(f"Erreur: Le film '{nom}' n'est pas dans la liste.")


def get_names():
    """
    Renvoie une liste alphabétique des noms de films.

    Return:
    list: Liste alphabétique des noms de films.
    """
    log("Obtention de la liste alphabétique des noms de films.")
    return sorted(films.keys())

def display_all():
    """Affiche tous les films."""
    log("Affichage de tous les films.")
    for film in films.values():
        print(f"Nom: {film['nom']}, Genre: {film['genre']}, Favori: {film['favori']}")

def get_genres():
    """
    Renvoie un dictionnaire avec les genres en clé et le nombre de films correspondant au genre en valeur.

    Return:
    dict: Dictionnaire des genres et du nombre de films correspondant.
    """
    log("Obtention du nombre de films par genre.")
    genres_count = {}
    for film in films.values():
        genre = film['genre']
        genres_count[genre] = genres_count.get(genre, 0) + 1
    return genres_count

def get_favorites():
    """
    Renvoie une liste alphabétique des films favoris.

    Return:
    list: Liste alphabétique des noms des films favoris.
    """
    log("Obtention de la liste des films favoris.")
    favorites = [film['nom'] for film in films.values() if film['favori']]
    return sorted(favorites)

def get_names_by_genre(genre):
    """
    Renvoie une liste alphabétique des noms de films pour un genre donné.

    Parametre:
    genre (str): Le genre pour lequel récupérer les noms de films.

    Return:
    list: Liste alphabétique des noms de films pour le genre donné.
    """
    log(f"Obtention de la liste des films pour le genre '{genre}'.")
    genre_names = [film['nom'] for film in films.values() if film['genre'] == genre]
    return sorted(genre_names)

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



