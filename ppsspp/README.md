# :video_game: PPSSPP Game Server

**Add-on oficial de [Hiapp](https://github.com/Triplex3x-cyver/hiapp) para servir ISOs de PSP a [PPSSPP](https://www.ppsspp.org/).**

Añade a Hiapp un servidor de disco remoto compatible con el emulador PPSSPP. Los juegos se leen directamente del servidor  
a medida que PPSSPP necesita algún **rango**, sin descargarlos completos.

Si alguien necesita descargar un juego completo, puede hacerlo desde un navegador:  
abre `IP-del-servidor:puerto/game`, verás el nombre de cada juego. Copia el nombre,  
pégalo en la barra de direcciones precedido por `/` y ejecuta. La descarga comenzará.

> [!WARNING]
> **Aviso legal**: no recomiendo ni sugiero vender archivos de juego.  
> Pero **no está prohibido compartir tus propios juegos**, adquiridos legalmente.  
> Los compraste; son tuyos; tú decides que hacer.
>
> **NO ME HAGO RESPONSABLE DEL USO QUE SE LES DÉ**.

---

## :sparkles: Características

- **Streaming por rangos** (`Range Requests`): PPSSPP lee solo los fragmentos que necesita.
- **Compatible con PPSSPP 1.20.4+**, puede que también con versiones anteriores.
- **Sin copia local**: los juegos viven en el servidor, no en cada dispositivo.
- **Navegación en el emulador**: PPSSPP muestra la lista de juegos; eliges uno y comienza el streaming.
- **Compatible con nombres con espacios** (codificación automática a %20 y otros).

---

## :file_folder: Estructura del add-on

```
ppsspp/
├── README.md          # Este archivo
├── README_EN.md       # English version
├── addon.json         # Metadatos del add-on
└── core/
    ├── __init__.py    # Punto de entrada: register(context)
    ├── routes.py      # Blueprint Flask (/game, /game/<file>)
    └── paths.py       # Utilidades de rutas
```

---

## :gear: Configuración

### Directorio de juegos

Por defecto, Hiapp busca los juegos en el **HOME** de tu equipo `~/PSP/`. Puedes cambiarlo con:

```bash
hiapp-config set games_dir /ruta/a/tus/ISOs
```

Formatos soportados: **`.iso`** normal y **`.cso`** comprimido.

### Configurar PPSSPP

En base a la versión 1.20.4

1. Conecta el dispositivo cliente a la **misma red** que el servidor.
2. Busca en los **Ajustes de juegos** o **Preferencias** la sección **Streaming de disco remoto**.
3. Entra en **Opciones** y añade cada opción:
   - Servidor remoto:
       **192.168.10.1 (la que muestre tu Hiapp)**
   - Puerto remoto:
     **5000 (o el que hayas definido antes)**
   - Subdirectorio remoto
     **/game**
4. Navega por los juegos disponibles y selecciona uno. PPSSPP solicitará los datos que necesite.

> [!NOTE]
> Los nombres de menús en PPSSPP varían según la versión y traducción.  
> Busca la sección equivalente en tu emulador.
>
> **Servidor y puerto**: los ves en el mensaje de arranque de Hiapp.
>
> **Subdirectorio remoto**: `/game`, **sin barra al final**.

---

## :brain: Detalles técnicos

- **Endpoint `/game`**: devuelve el catálogo en formato `index.txt`.
- **Endpoint `/game/<filename>`**: sirve el archivo con soporte `206 Partial Content`.
- **Codificación**: los nombres con espacios se codifican como `%20` en el catálogo.
- **Seguridad**: protección contra *path traversal* en el endpoint de streaming.

---

## :hammer_and_wrench: Solución de problemas

### El servidor no responde a PPSSPP

1. Verifica que ambos dispositivos estén en la **misma red WiFi**.
2. Comprueba que el puerto (por defecto `5000`) no esté bloqueado por el firewall.
3. Prueba `http://<IP-del-servidor>:5000/game` desde el navegador del cliente.
   Deberías ver una lista de nombres de archivos.

### Error 400 en el log del servidor

```
code 400, message Bad request version ('\x00\x12...')
```

Significa que alguna aplicación intentó conectar por HTTPS a un puerto HTTP. No es
un problema del add-on. Ignorar.

### Error 404 al seleccionar un juego

Verifica que:
- Su extensión es `.iso` o `.cso`, son las admitidas.

### El juego se ve entrecortado o lento

El servidor de desarrollo de Flask no es óptimo para streaming de archivos
grandes. En versiones futuras se usará un servidor más potente
(`waitress`). Aparte, puedes tener una mala configuración en el emulador, y la ROM puede ser pesada de emular.

Mientras tanto, verifica:
- Que el cliente y el servidor estén en la **misma red WiFi** (no por internet).
- Que la señal WiFi sea estable.
- Que no haya otros dispositivos consumiendo demasiado ancho de banda en la misma red.

> [!WARNING]
> Si tienes cortafuegos o VPN activo, Hiapp puede darte una ip inútil para hotspot,
> como `10.0.8.1` o `127.0.0.1`, busca y prueba hasta lograrlo, si has llegado hasta aquí, es porque eres inteligente, tú puedes hacerlo.

---

## :scroll: Licencia

Este add-on se distribuye bajo la licencia **Apache 2.0**, igual que el
proyecto Hiapp. Consulta el archivo [LICENSE](../../LICENSE) para detalles.

---

## :pray: Agradecimientos

Al equipo de [PPSSPP](https://www.ppsspp.org/), por un emulador
extraordinario y su soporte de servidores de red.

---

*Última actualización: 15 de Octubre de 2026*

[Ir a arriba](#-ppsspp-game-server) • [Volver al repositorio](../../README.md)