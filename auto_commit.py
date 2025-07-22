import os
import random
from datetime import datetime

# Lista de frases aleatorias
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

# Seleccionar una frase aleatoria
random_phrase = random.choice(phrases)

# Configuración
repo_path = "."
file_name = "commits.log"

# Cambiar al directorio del repositorio
os.chdir(repo_path)

# Agregar una línea al archivo (para forzar el cambio)
with open(file_name, "a") as f:
    f.write(f"{datetime.now()} - {random_phrase}\n")

# Configurar Git
os.system("git config --global user.name 'majopan'")
os.system("git config --global user.email 'mariazzz2326@gmail.com'")

# Agregar, commit y push (forzado con --allow-empty para que lo haga siempre)
os.system("git add .")
os.system(f"git commit -m '{random_phrase}' --allow-empty")
os.system("git push")
