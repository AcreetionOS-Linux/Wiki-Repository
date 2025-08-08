# 🎮 Full Guide: Installing Gaming Tools on Arch-Based Systems with Pamac (GUI)

This guide is written for **beginners** and explains step-by-step how to install:

- **Bottles** – Manage Windows software with Wine in isolated environments.
- **ProtonUp-Qt** – Install and manage Proton-GE versions for Steam and Lutris.
- **Lutris** – Game launcher for multiple platforms.
- **Steam** – Popular gaming platform for Linux, Windows, and Mac.
- **Heroic Games Launcher** – Epic Games, GOG, and Amazon Games launcher for Linux.

We will **only** use the **Pamac GUI** (Add/Remove Software) — **no terminal commands required**.

---

## 🛠 1. Open Pamac (Add/Remove Software)
1. Click your **application menu**.
2. Search for **"Add/Remove Software"** or **"Pamac"**.
3. Click it to open.

---

## 🔓 2. Enable AUR (Arch User Repository) Support

Some of the programs we’re installing are only available in the **AUR**, so you need to turn this on.

1. In Pamac, click the **☰ menu** (three horizontal lines) in the top right corner.
2. Select **Preferences**.  
   *(You may be prompted to enter your administrator password — this is normal.)*
3. In the Preferences window, click the **Third Party** tab.
4. Under **AUR**, turn on:
   - ✅ **Enable AUR support**  
   - (Optional but recommended) ✅ **Check for updates from AUR**
5. Close the Preferences window.

---

## 🔍 3. Searching and Installing Applications

We’ll install the applications **one by one** using Pamac’s search feature.

### Install Bottles
1. In the search bar at the top, type **bottles**.
2. Click on **Bottles** in the results.
3. Click **Install**.

### Install ProtonUp-Qt
1. Clear the search bar, then type **protonup-qt**.
2. Make sure you select the one from the **AUR** tab if it doesn’t appear in the main search results.
3. Click **Install**.

### Install Lutris
1. Search for **lutris**.
2. Click **Install**.

### Install Steam
1. Search for **steam**.
2. Click **Install**.
3. When prompted, approve any **extra packages** Steam needs.

### Install Heroic Games Launcher
1. Search for **heroic-games-launcher-bin**.
2. This package will usually appear in the **AUR** tab — click it.
3. Click **Install**.

---

## ⏳ 4. Apply and Wait
- After marking each package for installation, click **Apply** in the bottom right corner.
- Pamac will:
  - Download the necessary files
  - Build AUR packages where needed (this can take a while depending on your system)
- You may be prompted to confirm and enter your password again.

---

## 🖥 5. After Installation

Once everything is installed, you can launch them from your applications menu:

- **Steam** – Installs its runtime on first launch; you can log in and start installing games.
- **ProtonUp-Qt** – Use it to install Proton-GE versions for Steam or Lutris.
- **Bottles** – Create isolated Wine environments for apps or games.
- **Lutris** – Connect accounts and install games from multiple sources.
- **Heroic Games Launcher** – Log in to Epic, GOG, or Amazon Games and install your games.

---

## 💡 Tips for Best Results
- Restart your system after installing these apps to make sure everything is set up correctly.
- Keep **AUR updates enabled** so your games and tools stay current.
- Some games may need extra dependencies; Lutris often prompts you to install them automatically.
- For Steam games that need newer Proton versions, open **ProtonUp-Qt** and install the latest Proton-GE, then select it in Steam’s game settings.

---

✅ **You’re now ready to enjoy gaming on Linux!**

