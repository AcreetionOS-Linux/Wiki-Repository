# Gaming on AcreetionOS

Linux has become a first-class platform for gaming, and AcreetionOS is an excellent choice for it. This guide will walk you through the process of setting up your system for gaming.

---

## 1. Graphics Drivers

The first and most important step is to ensure that you have the correct graphics drivers installed. For detailed instructions on how to install graphics drivers for NVIDIA and AMD GPUs, please refer to the [Common Problems and Solutions](problems.md#graphics-issues) page.

---

## 2. Steam

Steam is the largest digital distribution platform for PC gaming and is the primary way to play games on Linux. It includes a compatibility layer called Proton, which allows you to run many Windows-only games on Linux.

### Installation

*   **Using Pamac (GUI):**
    1.  Open Pamac (Add/Remove Software).
    2.  Search for `steam`.
    3.  Click **Install**.

*   **Using pacman (CLI):**

    ```bash
    sudo pacman -S steam
    ```

### Enabling Proton for all games

By default, Steam only enables Proton for a curated list of games. You can enable it for all games by going to `Steam > Settings > Steam Play` and checking the box for "Enable Steam Play for all other titles".

---

## 3. Lutris

Lutris is an open-source gaming platform that allows you to install and manage games from a variety of sources, including GOG, Humble Bundle, and Epic Games Store. It also provides community-maintained installation scripts for many games.

### Installation

*   **Using Pamac (GUI):**
    1.  Open Pamac.
    2.  Search for `lutris`.
    3.  Click **Install**.

*   **Using pacman (CLI):**

    ```bash
    sudo pacman -S lutris
    ```

---

## 4. Heroic Games Launcher

The Heroic Games Launcher is an open-source alternative to the Epic Games Store and GOG Galaxy. It allows you to download and play your games from those stores on Linux.

### Installation

*   **Using Pamac (GUI):**
    1.  Open Pamac and ensure that AUR support is enabled (see the [Installation Guide](installation.md#enabling-aur-support)).
    2.  Search for `heroic-games-launcher-bin`.
    3.  Click **Install**.

*   **Using yay (CLI):**

    ```bash
    yay -S heroic-games-launcher-bin
    ```

---

## 5. Proton-GE

Proton-GE is a community-maintained version of Proton that often includes fixes and features that are not yet available in the official version. It can be useful for running games that do not work with the standard Proton.

To easily manage Proton-GE versions, you can use `ProtonUp-Qt`.

### Installation of ProtonUp-Qt

*   **Using Pamac (GUI):**
    1.  Open Pamac and ensure that AUR support is enabled.
    2.  Search for `protonup-qt`.
    3.  Click **Install**.

*   **Using yay (CLI):**

    ```bash
    yay -S protonup-qt
    ```

Once installed, you can use ProtonUp-Qt to install the latest version of Proton-GE and then select it in the compatibility settings for a game in Steam.

---

## 6. Performance Tips

### GameMode

GameMode is a daemon that allows games to request a set of optimizations to be temporarily applied to the host OS. This can improve gaming performance.

#### Installation

```bash
sudo pacman -S gamemode
```

To use it, add `gamemoderun %command%` to the launch options of a game in Steam.

### Gaming Kernels

There are several community-maintained kernels that are optimized for gaming, such as `linux-zen` and `linux-tkg`. These kernels often include features that can improve gaming performance and reduce input latency. You can install them from the official repositories or the AUR.