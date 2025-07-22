import os
from datetime import datetime

# Configuración
repo_path = "."
file_name = "commits.log"

# Cambiar al directorio del repositorio
os.chdir(repo_path)

# Escribir la fecha en el archivo de log
with open(file_name, "a") as f:
    f.write(f"Auto commit at {datetime.now()}\n")

# Configurar Git
os.system("git config --global user.name 'majopan'")
os.system("git config --global user.email 'mariazzz2326@gmail.com'")

# Verificar si hay cambios antes de hacer commit
os.system("git add .")
status = os.popen("git status --porcelain").read()

if status.strip():
    os.system(f"git commit -m 'Auto commit: {datetime.now()}'")
    os.system("git push")
else:
    print("No hay cambios para commitear.")
