# AcreetionOS Installation Guide

This guide provides instructions for installing AcreetionOS. We use the Calamares installer, which should be familiar to users who have installed other Linux distributions. An active internet connection is required for the installation.

---

## 1. Obtaining Installation Media

You have two options for creating a bootable USB drive:

### Option A: USB Flasher Utility (Recommended)

We provide a graphical utility that simplifies the process of downloading the ISO and writing it to a USB drive. 

*   **Windows:** [Download the AcreetionOS USB Flasher for Windows](https://iso.acreetionos.org:8448/Flashing_Utility/dist/AcreetionOS_USB_Flasher_Setup_1.0.0.exe). This utility uses Rufus internally.
*   **Linux:** [Download the AcreetionOS USB Flasher for Linux (AppImage)](https://iso.acreetionos.org:8448/Flashing_Utility/dist/AcreetionOS%20USB%20Flasher-1.0.0.AppImage).

To use the AppImage on Linux, you first need to make it executable:

```bash
chmod +x AcreetionOS_USB_Flasher-1.0.0.AppImage
```

You will also need to have FUSE installed. The package name varies depending on your distribution:

*   **Arch Linux and derivatives:** `fuse2`
*   **Debian, Ubuntu and derivatives:** `fuse`
*   **Fedora and derivatives:** `fuse`
*   **openSUSE:** `fuse`

### Option B: Manual Installation

Alternatively, you can download the ISO image directly from our website and use a tool of your choice to write it to a USB drive.

1.  Download the desired ISO image from [https://acreetionos.org](https://acreetionos.org).
2.  Use a utility such as `dd` or Etcher to write the ISO to a USB drive.

For example, on Linux, you can use `dd`:

```bash
# Replace /dev/sdX with your USB device
sudo dd if=/path/to/acreetionos.iso of=/dev/sdX bs=4M status=progress
```

**Warning:** Be careful to specify the correct device for `of`, as this command will overwrite the target device.

---

## 2. Booting and Installing

1.  Insert the bootable USB drive into the target machine.
2.  Reboot the machine and enter the boot menu (commonly by pressing F2, F10, F12, or DEL during startup).
3.  Select the USB drive to boot from.
4.  The AcreetionOS live environment will start, and the Calamares installer will launch automatically.
5.  Follow the on-screen instructions to partition your drive and install the system.
6.  Once the installation is complete, reboot the machine and remove the USB drive.

---

## 3. Post-Installation

AcreetionOS comes with a minimal set of pre-installed applications:

*   **Firefox:** Web browser
*   **Pamac:** A graphical package manager for installing and updating software.

### Installing Additional Software

AcreetionOS gives you access to a wide range of software through several sources. We want to make sure you can get the tools you need, so we've integrated them all into Pamac, our graphical package manager.

Here's where your software comes from:

*   **AcreetionOS Repositories:** These are our official repositories. We pull packages from Arch Linux and test them to ensure they're stable before we release them to you. This is your primary, safest source of software.
*   **The ACUR (AcreetionOS Community User Repository):** Similar to the AUR, the ACUR is a place for community-contributed packages made specifically for AcreetionOS.
*   **The AUR (Arch User Repository):** You have access to the vast collection of community-maintained packages for Arch Linux. It's a fantastic resource, but be aware that these packages are built from source on your machine and are maintained by the community, so use your judgment.
*   **Flatpak:** We also include support for Flatpak out of the box. This allows you to install sandboxed applications that work across different Linux distributions.

You can manage all of these sources through Pamac. To enable or disable support for AUR, ACUR, or Flatpak, just open Pamac, go to the preferences, and you'll find the toggles in the "Third Party" tab.

For those who prefer the command line, you can still use `pacman` for managing packages from the official AcreetionOS repositories.

---

## 4. Getting Help

If you encounter any issues during or after installation, you can find help in the following places:

*   **AcreetionOS Discord:** (https://discord.acreetionos.org)
*   **AcreetionOS Wiki:** You are here.

We encourage you to search the wiki and forums for solutions before asking for help. When asking for help, please provide as much detail as possible, including any error messages and logs. We will guide you through how to get the information, and we may ask for the build number, and provide instructions on how to get it! We will walk you through everything, if needbe.