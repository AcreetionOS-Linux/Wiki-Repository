# AcreetionOS: Calamares Installer Walkthrough

This document provides a visual, step-by-step guide to the AcreetionOS installation process using the Calamares installer. For detailed instructions on preparing your installation media, please refer to the [AcreetionOS Installation Guide](installation.md).

---

## 1. Preparation

Before proceeding with the installation, ensure you have created a bootable USB drive with the AcreetionOS ISO. You can use our dedicated USB Flasher Utility or manually write the ISO to a USB drive. Refer to the [Installation Guide](installation.md) for more information.

---

## 2. Booting the Live Environment

Boot your system from the prepared USB drive. The method for accessing the boot menu varies by motherboard (commonly F2, F10, F12, or DEL). Once booted, the AcreetionOS live environment will start, and the Calamares installer will launch automatically.

### Language Selection

Select your preferred language for the installation process.

---

## 3. System Configuration

### Kernel and Drivers Selection

This step allows you to select the appropriate kernel and drivers for your hardware. Choose the options that best match your CPU and GPU to ensure optimal performance and compatibility.

### Software Selection

Select any additional software packages you wish to install alongside the base system. This includes common applications and utilities.

### Location and Keyboard Layout

Configure your geographical location and keyboard layout. These settings will determine your system's timezone and input method.

---

## 4. Disk Partitioning

This is a critical step where you configure how AcreetionOS will be installed on your storage device. **Proceed with caution, as incorrect partitioning can lead to data loss.**

*   **Erase Disk:** This option will wipe the entire disk and install AcreetionOS. This is the simplest option for a fresh installation.
*   **Manual Partitioning:** This option allows you to create and manage partitions manually. This is recommended for advanced users or dual-boot setups.

---

## 5. User Account Setup

Create your user account by providing a username, password, and hostname for your system. You can also configure automatic login and whether to use the same password for the administrator account.
---

## 6. Summary and Installation

Review the summary of your installation choices. If everything is correct, proceed with the installation. The installer will then begin writing the system to your disk.

Once the installation is complete, you will be prompted to restart your system. Remove the USB installation media and boot into your new AcreetionOS installation.
