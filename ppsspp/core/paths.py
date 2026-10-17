"""
Utilidades de rutas para el add-on PPSSPP.

Toda la información necesaria viene desde el context de Hiapp.
Este módulo no importa nada del paquete hiapp.
"""
# import sys
# sys.path.insert(0, str(Path.home() / ".hiapp" / addons / ppsspp / core))
from pathlib import Path

from . import get_context


def get_games_directory() -> str:
    """
    Devuelve el directorio de juegos configurado, creándolo si no existe.

    Lee la config fresca en cada llamada, por si el usuario la cambió
    con `hiapp-config` mientras Hiapp está corriendo.
    """
    context = get_context()

    # Preferir la función load_config si está disponible (config fresca)
    load_config = context.get("load_config")
    if load_config:
        config = load_config()
    else:
        # Fallback: usar la config snapshot
        config = context.get("config", {})

    games_dir = config.get("games_dir", str(Path.home() / "PSP"))
    Path(games_dir).mkdir(parents=True, exist_ok=True)
    return games_dir
