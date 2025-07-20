📅 Daily Auto-Commit Bot
Automatiza tus contribuciones en GitHub con commits programados cada hora usando Python y GitHub Actions.

Este repositorio contiene un script en Python y una configuración de GitHub Actions para hacer commits automáticos periódicos, simulando actividad en tu perfil de GitHub.

🚀 Características
✅ Commits automáticos cada hora (personalizable).
✅ Fácil configuración (solo clona y activa GitHub Actions).
✅ Funciona sin necesidad de tener tu PC encendida (usa servidores de GitHub).
✅ Personalizable (puedes modificar la frecuencia y el mensaje de commit).


❓ ¿Cómo funciona?
El script (auto_commit.py) hace lo siguiente:

Añade la fecha actual a un archivo commits.log.

Ejecuta los comandos Git (add, commit, push) para registrar el cambio.

GitHub Actions ejecuta este script automáticamente según el cronograma definido.
