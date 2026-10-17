"""
PPSSPP Game Server — Add-on de Hiapp.

Punto de entrada: register(context).

Hiapp llama a register() al cargar el add-on, pasando un diccionario
con las herramientas que el add-on necesita:

    context = {
        "app":           Flask app,
        "config":        dict con la configuración actual (snapshot),
        "load_config":   función para obtener config fresca,
        "save_config":   función para guardar cambios,
        "logger":        logging.Logger (opcional),
        "hiapp_dir":     Path a ~/.hiapp/,
        "hiapp_version": versión de Hiapp que cargó el add-on,
    }

Reglas de este add-on:
    - No importa nada de `hiapp`. Todo llega por el context.
    - Todo el código vive dentro de `core/`.
"""

_context = {}


def register(context):
    """
    Punto de entrada del add-on.

    Args:
        context: diccionario con las herramientas de Hiapp.
    """
    global _context
    _context = context

    # Registrar el blueprint
    from .routes import bp
    context["app"].register_blueprint(bp)

    # Log opcional
    logger = context.get("logger")
    if logger:
        logger.info("Add-on PPSSPP cargado.")


def get_context():
    """
    Devuelve el context inyectado por Hiapp al cargar el add-on.
    Usado por otros módulos internos (paths, etc.).
    """
    return _context
