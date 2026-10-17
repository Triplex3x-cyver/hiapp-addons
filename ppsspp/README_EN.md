# :video_game: PPSSPP Game Server

**Official [Hiapp](https://github.com/Triplex3x-cyver/hiapp) add-on for serving PSP ISOs to [PPSSPP](https://www.ppsspp.org/).**

Adds a remote disc server to Hiapp, compatible with the PPSSPP emulator.
Games are read directly from the server as PPSSPP requests specific
**ranges**, without downloading them in full.

If someone needs to download a full game, they can do it from a browser:
open `server-IP:port/game` and you will see the name of each game. Copy
the name, paste it in the address bar preceded by a `/`, and press Enter.
The download will begin.

> [!WARNING]
> **Legal notice**: I do not recommend or suggest selling game files.  
> But **sharing your own legally acquired games is not prohibited**.  
> You bought them; they are yours; you decide what to do with them.
>
> **I AM NOT RESPONSIBLE FOR HOW THEY ARE USED**.

---

## :sparkles: Features

- **Range streaming** (`Range Requests`): PPSSPP reads only the fragments it needs.
- **Compatible with PPSSPP 1.20.4+**, and possibly earlier versions.
- **No local copy**: games live on the server, not on each device.
- **Navigation in the emulator**: PPSSPP shows the game list; pick one and streaming begins.
- **Supports filenames with spaces** (automatic encoding to %20 and others).

---

## :file_folder: Add-on structure

```
ppsspp/
├── README.md          # Spanish version
├── README_EN.md       # This file
├── addon.json         # Add-on metadata
└── core/
    ├── __init__.py    # Entry point: register(context)
    ├── routes.py      # Blueprint Flask (/game, /game/<file>)
    └── paths.py       # Route utilities
```

---

## :gear: Configuration

### Games directory

By default, Hiapp looks for games in the **HOME** folder `~/PSP/`. You can change it with:

```bash
hiapp-config set games_dir /path/to/your/ISOs
```

Supported formats: **`.iso`** (plain) and **`.cso`** (compressed).

### Configure PPSSPP

Based on version 1.20.4

1. Connect the client device to the **same network** as the server.
2. Look in **Game Settings** or **Preferences** for the **Remote disc streaming** section.
3. Enter **Options** and add each setting:
   - Remote server:
       **192.168.10.1 (the one Hiapp shows)**
   - Remote port:
       **5000 (or the one you configured)**
   - Remote subdirectory:
       **/game**
4. Browse the available games and pick one. PPSSPP will request the data it needs.

> [!NOTE]
> Menu names in PPSSPP vary by version and translation.  
> Look for the equivalent section in your emulator.
>
> **Server and port**: shown in the Hiapp startup message.
>
> **Remote subdirectory**: `/game`, **no trailing slash**.

---

## :brain: Technical details

- **Endpoint `/game`**: returns the catalog in `index.txt` format.
- **Endpoint `/game/<filename>`**: serves the file with `206 Partial Content` support.
- **Encoding**: filenames with spaces are encoded as `%20` in the catalog.
- **Security**: protection against *path traversal* in the streaming endpoint.

---

## :hammer_and_wrench: Troubleshooting

### The server does not respond to PPSSPP

1. Verify that both devices are on the **same WiFi network**.
2. Check that the port (default `5000`) is not blocked by a firewall.
3. Test `http://<server-IP>:5000/game` from the client's browser.
   You should see a list of filenames.

### Error 400 in the server log

```
code 400, message Bad request version ('\x00\x12...')
```

Means that some application tried to connect via HTTPS to an HTTP port. Not
an add-on issue. Ignore.

### Error 404 when selecting a game

Verify that:
- Its extension is `.iso` or `.cso` — those are the supported ones.

### The game looks choppy or slow

The Flask development server is not optimal for streaming large files.
Future versions will use a more powerful server (`waitress`). Separately,
you may have a wrong configuration in the emulator, and the ROM may be
heavy to emulate.

Meanwhile, verify:
- That the client and server are on the **same WiFi network** (not over the internet).
- That the WiFi signal is stable.
- That no other devices are consuming too much bandwidth on the same network.

> [!WARNING]
> If you have a firewall or VPN active, Hiapp may report an unusable IP for
> hotspot use, such as `10.0.8.1` or `127.0.0.1`. Keep trying until it works —
> if you got this far, you are smart, you can do it.

---

## :scroll: License

This add-on is distributed under the **Apache 2.0** license, same as the
Hiapp project. See the [LICENSE](../../LICENSE) file for details.

---

## :pray: Acknowledgements

To the [PPSSPP](https://www.ppsspp.org/) team, for an extraordinary
emulator and its network server support.

---

*Last updated: October 15, 2026*

[Back to top](#-ppsspp-game-server) • [Back to the repository](../../README.md)