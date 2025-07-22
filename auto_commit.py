import os
import random
from datetime import datetime

# Lista de frases aleatorias para los mensajes de commit
phrases = [
    "Keep going 💪",
    "Another step forward 🚀",
    "One more brick in the wall 🧱",
    "Persistence is key 🔑",
    "Making history, one commit at a time 🕒",
    "Tick tock, another commit 🕰️",
    "More green squares! 🟩",
    "Automated love ❤️",
    "Hello again, GitHub 👋",
    "Commit como si nadie mirara 🎭"
]

# Elegir una frase aleatoria
random_phrase = random.choice(phrases)

# Configuración del repo y archivo a modificar
repo_path = "."
file_name = "commits.log"

# Cambiar al directorio del repositorio
os.chdir(repo_path)

# Escribir algo nuevo en el archivo para forzar cambios reales
with open(file_name, "a") as f:
    f.write(f"{datetime.now()} - {random_phrase}\n")

# Configurar Git con tu nombre y correo
os.system("git config user.name 'majopan'")
os.system("git config user.email 'mariazzz2326@gmail.com'")

# Agregar cambios y hacer commit, incluso si no hay cambios (--allow-empty)
os.system("git add .")
os.system(f"git commit -m '{random_phrase}' --allow-empty")

# Hacer push (GitHub Actions ya tiene permisos para esto)
os.system("git push")
