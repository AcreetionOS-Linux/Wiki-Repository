# StormOS

StormOS is a lightweight, fast, and elegant Arch Linux-based respin designed for speed, simplicity, and modern functionality out of the box. Built with Calamares installer support and optimized for both legacy and UEFI systems, StormOS is ideal for users who want a rolling release Arch experience without the setup hassle.

StormOS is available in two editions:

- XFCE Edition — For users who prefer a fast, minimal desktop with a classic interface.  
- KDE Plasma Edition — For users who want a modern, feature-rich desktop with advanced customization and built-in effects.

StormOS is a sister project to **AcreetionOS**. Both projects support one another closely and share the same installer builds for the most part, ensuring consistency and reliability across installations.

---

## Overview

| Feature              | Details                                                                 |
|----------------------|-------------------------------------------------------------------------|
| Base                 | Arch Linux (Rolling Release)                                            |
| Desktop Environments  | XFCE 4 (Custom themed), KDE Plasma                                      |
| Installer            | Calamares                                                               |
| Package Manager      | `pacman` + `yay` for AUR support                                        |
| Architecture         | x86_64                                                                  |
| Boot Support         | UEFI and Legacy BIOS                                                    |
| Display Manager      | LightDM (XFCE), SDDM (KDE)                                              |
| Init System          | `systemd`                                                               |
| Target Audience      | Intermediate to advanced Linux users who want a fast and stable setup   |

---

## Features

- XFCE with Storm Theme: Minimal, fast, and elegant. Customized panel, window manager, and icons.  
- KDE Plasma with Breeze Storm: Modern layout with polished theming, Wayland and X11 support.  
- Preinstalled tools include popular utilities like `neofetch`, `htop`, `nano`, `firefox`, `thunar`, `dolphin`, and more.  
- Gaming support with optional Steam, Lutris, Wine, and gaming-tuned kernel presets.  
- Calamares graphical installer with EFI and legacy GRUB bootloader support.  
- Custom desktop layouts tailored for usability and clean aesthetics.  
- Modular configuration allows easy package management through meta groups.  

---

## Installation

### From ISO

1. Boot the StormOS ISO using USB or DVD.  
2. Login to the live environment (autologin user: `stormg`).  
3. Launch Calamares Installer (from desktop or menu).  
4. Follow the guided setup:  
   - Choose timezone, language, keyboard.  
   - Select disk partition layout (manual or automatic).  
   - Set username and password.  
5. Click Install and wait for completion.  
6. Reboot and remove the install media.  

### Minimum Requirements

| Resource       | XFCE Edition                | KDE Edition                 |
|----------------|-----------------------------|-----------------------------|
| CPU            | x86_64 (64-bit)             | x86_64 (64-bit)             |
| RAM            | 1 GB (min), 2 GB+ recommended | 2 GB (min), 4 GB+ recommended |
| Disk Space     | 10 GB                      | 15+ GB                      |
| GPU            | Intel, AMD, or NVIDIA (open or proprietary) |

---

## Customization

StormOS includes preconfigured tweaks for both desktops:

- **XFCE**  
  - StormDark/StormLight themes  
  - Custom Thunar actions and layout  

- **KDE Plasma**  
  - Breeze-Storm theme  
  - Kvantum + GTK theming  
  - Custom panel layouts and wallpaper selection  

Wallpapers are available in `/usr/share/backgrounds/stormos/`.

---

## Internet & Networking

- NetworkManager for Wi-Fi and Ethernet.  
- GUI frontends like `nm-connection-editor` and `nm-applet` (XFCE) or Plasma's network widget.  
- Bluetooth supported via `bluez`, `blueman` (XFCE), or `bluedevil` (KDE).  

---

## Security & Updates

- All packages come directly from the official Arch repos or AUR.  
- Update the system using:

  ```bash
  sudo pacman -Syu

or to include AUR:

yay -Syu

    Flatpak and Snap are optional via post-install script.

Known Issues
Issue	Solution
Desktop shortcuts not executable (XFCE)	Right-click > Properties > Enable "Allow executing file"
Installer desktop icons persist after install	Manually remove from ~/Desktop/ after install
EFI boot failed on some boards	Ensure Secure Boot is disabled in BIOS/UEFI settings
KDE Wayland sessions may fail on older GPUs	Use X11 session from login screen for compatibility
Directory Layout (Live ISO)

/stormos/
├── custom/             # Desktop themes, Calamares configs
├── scripts/            # Post-install scripts
├── etc/skel/           # User default configs
├── usr/share/backgrounds/stormos/
├── liveuser/           # stormg live user config
└── calamares/          # Installer configs and modules

Development

StormOS is built using:

    archiso for the live ISO

    Calamares for installation

    Xfce and KDE Plasma session customization for persistent defaults

    Optional custom repo support for StormOS meta packages

Git repo: (GitHub: https://github.com/bfitzgit23/stormos-iso)
Credits

StormOS is maintained by the StormG team and community contributors.

Special thanks to:

    The Arch Linux community

    Calamares developers

    XFCE and KDE Plasma developers

    Art and theme contributors

Support

Have questions or suggestions?

    Join our Discord: https://discord.gg/4PTNjZNN

    Email: linuxstormos@gmail.com
