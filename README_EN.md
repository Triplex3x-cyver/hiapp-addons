Hiapp version [![PyPI version](https://img.shields.io/pypi/v/hiapp.svg)](https://pypi.org/project/hiapp)

Downloads
[![PyPI Weekly Downloads](https://static.pepy.tech/personalized-badge/hiapp?period=weekly&units=NONE&left_color=BLACK&right_color=GREEN&left_text=Downloads%2Fweek)](https://pepy.tech/projects/hiapp)
[![PyPI Monthly Downloads](https://static.pepy.tech/personalized-badge/hiapp?period=monthly&units=NONE&left_color=BLACK&right_color=GREEN&left_text=Downloads%2Fmonth)](https://pepy.tech/projects/hiapp)
[![PyPI Total Downloads](https://static.pepy.tech/personalized-badge/hiapp?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=Total)](https://pepy.tech/projects/hiapp)

**🌐 Languages:** [Español](README.md) | **English**

---

# Hiapp Addons

**Official add-ons for [Hiapp](https://github.com/Triplex3x-cyver/hiapp).**

This repository contains the source code, documentation, and catalog
of all official Hiapp free add-ons. Each add-on adds functionality to the
core without increasing the base installation size.

---

## :jigsaw: What is an add-on?

An add-on is an dependent module that extends Hiapp. Some are **free**
(included with the project) and others are **PRO** (require a license).
Users install only the ones they need.

Each add-on:

- Has its own `addon.json` with metadata and permissions.
- Lives in its own folder inside this repository.
- Is distributed as a `.zip` file from [Releases](https://github.com/Triplex3x-cyver/hiapp-addons/releases).
- Is installed in `~/.hiapp/addons/` when the user activates it.

### Loading model

Hiapp loads add-ons through a **passive model**:

- The add-on **does not run on its own** (it is not a separate process).
- Hiapp imports it and calls its entry function: `register(context)`.
- The add-on **does not import anything from `hiapp`**. Everything it needs (Flask app, configuration, logger) is passed through the `context` dictionary.

This ensures that add-ons are **self-contained**, easy to verify (by hash), and safe to load.

---

## :package: Available add-ons

| Add-on | Status | License | Description |
|--------|--------|---------|-------------|
| [**PPSSPP**](ppsspp/) | ✅ Stable | Free | HTTP streaming server for PPSSPP. |

*(This table will grow as new add-ons are added.)*

---

## :inbox_tray: Installation

Add-ons are installed **through Hiapp**, not manually:

```bash
hiapp addon install <name>
```

For now, the add-on installation system is under development. In
upcoming versions you will be able to install, update, and remove
add-ons from the application itself or from the web panel.

**Current status**: free add-ons come bundled with Hiapp. This
repository separation is being prepared for version `0.0.4`.

---

## :book: Catalog

The [`addons.json`](addons.json) file contains the catalog of available
add-ons with their minimal metadata. Hiapp queries it to know what
exists before downloading each one.

---

## :handshake: Contributing

Contributions are welcome. If you want to create an add-on:

1. Read the [contributing guide](https://github.com/Triplex3x-cyver/hiapp/blob/main/docs/CONTRIBUTING.md) of the main project.
2. Follow the structure of an existing add-on (see `ppsspp/`).
3. Open a Pull Request with your proposal.

To report bugs or suggest ideas:

- **Issues**: https://github.com/Triplex3x-cyver/hiapp-addons/issues
- **Discussions**: https://github.com/Triplex3x-cyver/hiapp/discussions

---

## :speech_balloon: Community

- 🌐 **Website**: http://hiapp.mywebcommunity.org/
- **Telegram (announcements)**: https://t.me/hiapp_project
- **Telegram (chat & support)**: https://t.me/hiapp_chat
- **WhatsApp (channel)**: https://whatsapp.com/channel/0029VbEIkYy1Hsq3oyhkth2Y

---

## :scroll: License

This project is distributed under the **Apache 2.0** license.
See the [LICENSE](LICENSE) file for details.

> Unofficial Spanish translation: [LICENSE_ES](LICENSE_ES).

---

## :pray: Acknowledgements

To the [Termux](https://termux.dev/) community and to the developers
of [Vosk](https://github.com/alphacep/vosk-api) (**Alpha Cephei Inc**),
whose work makes Hiapp possible.

---

*Last updated: October 15, 2026*

[Go to top](#hiapp-addons)
