Versión de Hiapp [![PyPI version](https://img.shields.io/pypi/v/hiapp.svg)](https://pypi.org/project/hiapp)

Descargas  
[![PyPI Weekly Downloads](https://static.pepy.tech/personalized-badge/hiapp?period=weekly&units=NONE&left_color=BLACK&right_color=GREEN&left_text=Descargas%2Fsemana)](https://pepy.tech/projects/hiapp)
[![PyPI Monthly Downloads](https://static.pepy.tech/personalized-badge/hiapp?period=monthly&units=NONE&left_color=BLACK&right_color=GREEN&left_text=Descargas%2Fmes)](https://pepy.tech/projects/hiapp)
[![PyPI Total Downloads](https://static.pepy.tech/personalized-badge/hiapp?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=Total)](https://pepy.tech/projects/hiapp)

**🌐 Idiomas:** **Español** | [English](README_EN.md)

---

# Hiapp Addons

**Add-ons oficiales para [Hiapp](https://github.com/Triplex3x-cyver/hiapp).**

Este repositorio contiene el código fuente, la documentación y el catálogo
de todos los add-ons gratuitos oficiales de Hiapp. Cada add-on añade funcionalidades
al núcleo sin aumentar el tamaño de la instalación base.

---

## :jigsaw: ¿Qué es un add-on?

Un add-on es un módulo dependiente que extiende Hiapp. Algunos son
**gratuitos** (incluidos con el proyecto) y otros son **PRO** (requieren
licencia). Los usuarios instalan solo los que necesitan.

Cada add-on:

- Tiene su propio `addon.json` con metadatos y permisos.
- Vive en su propia carpeta dentro de este repositorio.
- Se distribuye como archivo `.zip` desde las [Releases](https://github.com/Triplex3x-cyver/hiapp-addons/releases).
- Se instala en `~/.hiapp/addons/` cuando el usuario lo activa.

### Modelo de carga

Hiapp carga los add-ons mediante un **modelo pasivo**:

- El add-on **no se ejecuta por separado** (no es un proceso independiente).
- Hiapp lo importa y llama a su función de entrada: `register(context)`.
- El add-on **no importa nada de `hiapp`**. Todo lo que necesita (app Flask, configuración, logger) llega a través del diccionario `context`.

Esto garantiza que los add-ons sean **autocontenidos**, fáciles de verificar (por hash) y seguros de cargar.

---

## :package: Add-ons disponibles

| Add-on | Estado | Licencia | Descripción |
|--------|--------|----------|-------------|
| [**PPSSPP**](ppsspp/) | ✅ Estable | Gratuito | Servidor de streaming HTTP para PPSSPP. |

*(Esta tabla crecerá conforme se añadan nuevos add-ons.)*

---

## :inbox_tray: Instalación

Los add-ons se instalan **a través de Hiapp**, no manualmente:

```bash
hiapp addon install <nombre>
```

Por ahora, el sistema de instalación de add-ons está en desarrollo. En las
próximas versiones podrás instalar, actualizar y eliminar add-ons desde la
propia aplicación o desde el panel web.

**Estado actual**: los add-ons gratuitos vienen incluidos en Hiapp. Esta
separación en repositorio se está preparando para la versión `0.0.4`.

---

## :book: Catálogo

El archivo [`addons.json`](addons.json) contiene el catálogo de add-ons
disponibles, con sus metadatos mínimos. Hiapp lo consulta para saber qué
existe antes de descargar cada uno.

---

## :handshake: Contribuir

Las contribuciones son bienvenidas. Si quieres crear un add-on:

1. Lee la [guía de contribución](https://github.com/Triplex3x-cyver/hiapp/blob/main/docs/CONTRIBUTING.md) del proyecto principal.
2. Sigue la estructura de un add-on existente (ver `ppsspp/`).
3. Abre un Pull Request con tu propuesta.

Para reportar errores o proponer ideas:

- **Issues**: https://github.com/Triplex3x-cyver/hiapp-addons/issues
- **Discussions**: https://github.com/Triplex3x-cyver/hiapp/discussions

---

## :speech_balloon: Comunidad

- 🌐 **Sitio web**: http://hiapp.mywebcommunity.org/
- **Telegram (anuncios)**: https://t.me/hiapp_project
- **Telegram (chat y soporte)**: https://t.me/hiapp_chat
- **WhatsApp (canal)**: https://whatsapp.com/channel/0029VbEIkYy1Hsq3oyhkth2Y

---

## :scroll: Licencia

Este proyecto se distribuye bajo la licencia **Apache 2.0**.
Consulta el archivo [LICENSE](LICENSE) para más detalles.

> Traducción no oficial al español: [LICENSE_ES](LICENSE_ES).

---

## :pray: Agradecimientos

A la comunidad de [Termux](https://termux.dev/) y a los desarrolladores
de [Vosk](https://github.com/alphacep/vosk-api) (**Alpha Cephei Inc**),
cuyo trabajo hace posible Hiapp.

---

*Última actualización: 15 de Octubre de 2026*

[Ir a arriba](#hiapp-addons)
