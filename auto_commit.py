import os
from datetime import datetime

# Configuración de Git
repo_path = "."  # Directorio del repositorio
file_name = "commits.log"  # Archivo que se actualizará

# Cambia al directorio del repositorio
os.chdir(repo_path)

# Escribe la fecha actual en el archivo
with open(file_name, "a") as f:
    f.write(f"Auto commit at {datetime.now()}\n")

# Comandos Git
os.system("git config --global user.name 'Tu Nombre'")
os.system("git config --global user.email 'tu-email@example.com'")
os.system("git add .")
os.system(f"git commit -m 'Auto commit: {datetime.now()}'")
os.system("git push")
