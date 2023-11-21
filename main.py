import art
import sys
from movie import *

print(art.text2art("MovieList"))

def say_hello(name: str):
    print(f'Hello {name} !')
    return

print(say_hello('Eliott'))

movie = create_movie('Star Wars', 'Science fiction', True)
add_movie(movie)

movie = create_movie('Star Trek', 'Science fiction', False)
add_movie(movie)

movie = create_movie('James Bond', 'Action', True)
add_movie(movie)

movie = create_movie('Cars', 'Animation', False)
add_movie(movie)

#delete_movie('Cars')

print(get_genres())

args = sys.argv[1:]
print(args)
if len(args) > 2:
    print('Invalid number of arguments')

if len(args) == 1:
    if args[0] == '-log':
        logger.show_log()
    elif args[0] == '-lm':
        print(get_names())
    elif args[0] == '-fv':
        favorites = get_favorites()
        print(favorites)
    else:
        print('Invalid argument !')

if len(args) == 2:
    if args[0] == '-g':
        res = get_names_by_genre(args[1])
        print(res)
    else:
        print('Invalid argument !')

{
    "workbench.colorCustomizations": {
    "editor.background": "#1c1920",
  }
}