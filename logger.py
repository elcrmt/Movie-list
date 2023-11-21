from datetime import datetime  

def log(message):
    """
    Enregistre un message dans le fichier movie.log à la racine du projet.

    Parametre:
    message (str): Le message à enregistrer dans le fichier de journal.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("movie.log", "a") as log_file:
        log_file.write(f"{current_time} - {message}\n")

    print(f"{current_time} - {message}")