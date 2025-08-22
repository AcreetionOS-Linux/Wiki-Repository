# AcreetionOS Installation Guide

Welcome! This page will guide you through installing AcreetionOS. We keep it **as simple as possible** so even if you’ve never installed Linux before, you’ll be fine.  

> **Important:** AcreetionOS currently requires an **active internet connection** to install.

---

## 1. Choosing Your Installation Method

You have two main ways to get AcreetionOS onto your computer:

### **Option A – Use Our USB Flasher Utility** (Recommended)
This is the easiest method. It handles downloading the ISO and writing it to your USB drive for you.

- **Windows**:  
  [Download AcreetionOS USB Flasher for Windows](https://iso.acreetionos.org:8448/Flashing_Utility/dist/AcreetionOS_USB_Flasher_Setup_1.0.0.exe)  
  - Uses **Rufus** under the hood for USB writing because of Windows driver signing.  
  - Just run it, follow the prompts, and you’re done.

- **Linux**:  
  [Download AcreetionOS USB Flasher for Linux (AppImage)](https://iso.acreetionos.org:8448/Flashing_Utility/dist/AcreetionOS%20USB%20Flasher-1.0.0.AppImage)  
  **Important:**  
  1. Make the AppImage **executable**:  
     ```bash
     chmod +x AcreetionOS\ USB\ Flasher-1.0.0.AppImage
     ```
  2. Install **FUSE** if it’s not already installed:  
     - **Arch / Manjaro**:  
       ```bash
       sudo pacman -S fuse2
       ```
     - **Debian / Ubuntu / Linux Mint / Pop!_OS**:  
       ```bash
       sudo apt install fuse
       ```
     - **Fedora / RHEL / Rocky / AlmaLinux**:  
       ```bash
       sudo dnf install fuse
       ```
     - **openSUSE**:  
       ```bash
       sudo zypper install fuse
       ```
     - **Gentoo**:  
       ```bash
       sudo emerge sys-fs/fuse
       ```
  *(Runs on almost any Linux system without installation — no need for Flathub.)*

---

### **Option B – Manual ISO Method**
If you prefer doing it yourself:

1. Go to [https://acreetionos.org](https://acreetionos.org).
2. Download the ISO you want.  
   - Mirror links are available if the main server is down.
3. Use your own USB writing tool (like Rufus on Windows or `dd` on Linux) to write it to a USB stick.  
   - We have manual instructions right below the download links on our website.

---

## 2. Installing AcreetionOS

Once your USB is ready:

1. Plug it into the computer you want to install AcreetionOS on.
2. Boot from the USB (this is usually done by pressing **F12**, **F2**, or **Esc** during startup).
3. When AcreetionOS starts, the **installer will automatically pop up**.
4. Go step-by-step through the installer (we use **Calamares**, which is simple).
5. **Internet is required** — the installer will download what it needs during setup.
6. Once done, restart, remove the USB, and boot into AcreetionOS.

---

## 3. What’s Included by Default

We ship AcreetionOS with a selection of software we believe **every user will need**:

- **Firefox** web browser (ready to go after install).
- **Pamac** — a friendly software store where you can install and remove apps without touching the terminal.
- Basic tools for everyday use.

---

## 4. Installing Extra Apps

Want Google Chrome or something else? You have options:

- **AUR (Arch User Repository)** — a huge collection of community-maintained software.
- You can enable AUR support directly in Pamac:
  1. Open Pamac.
  2. Go to **Preferences** (you may need your password).
  3. Enable **AUR**.
  4. Search for your app (e.g., “google-chrome”) and click install.

---

## 5. We’re Always Improving

We work on AcreetionOS **almost every day**.  
If you ever get stuck or have questions:
- We’re happy to help — even if we can’t reply instantly, we usually have Discord open.

---

## 6. Need Help or Have Questions?

Join our friendly **AcreetionOS Community on Discord**:  
🔗 [https://discord.gg/AJ6uuvtDXY](https://discord.gg/AJ6uuvtDXY)

---

## 7. If You’re the “I Read the Manual” Type

Some people like to dive into **documentation** instead of asking questions.  
If that’s you, check out:  
📚 [AcreetionOS Wiki – Problems & Fixes](https://wiki.acreetionos.org/en/latest/problems/)  

Just know… the wiki is written in the **classic old-school Linux style**, which is great if you like scrolling through text walls.  
Most newer users these days just:
- Ask on Discord.
- Or use AI to get an answer in 10 seconds.  

But hey, if you’re a “manual and coffee” person — we love you too. ❤️

