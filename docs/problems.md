# Common Problems and Solutions

This page lists some common problems that you may encounter while using AcreetionOS, along with their solutions.

---

## Installation Issues

### The installer fails with an error message

If the Calamares installer fails, please try the following:

1.  Ensure that you have a stable internet connection.
2.  Verify the integrity of the ISO image you downloaded.
3.  Try a different USB drive and USB port.
4.  If you are partitioning your drive manually, ensure that you have created an EFI System Partition (ESP) of at least 300MB and mounted it at `/boot/efi`.

If the problem persists, please file a bug report and provide the installer log, which can be found at `~/.cache/calamares/session.log` in the live environment.

### The system does not boot after installation

If the system does not boot after installation, it is likely an issue with the bootloader. Please try the following:

1.  Boot into the AcreetionOS live environment.
2.  Open a terminal and mount your system's root partition.
3.  Chroot into your installed system.
4.  Reinstall the GRUB bootloader:

    ```bash
    grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=AcreetionOS
    grub-mkconfig -o /boot/grub/grub.cfg
    ```

5.  Reboot your system.

---

## Graphics Issues

### Incorrect screen resolution or graphical artifacts

If you are experiencing graphics issues, it is likely that you need to install the correct graphics drivers for your hardware.

#### NVIDIA Drivers

To install the proprietary NVIDIA drivers, run the following command:

```bash
sudo pacman -S nvidia
```

Then, reboot your system.

#### AMD Drivers

The open-source AMD drivers (`mesa`) are installed by default and should work for most AMD GPUs. If you are experiencing issues, you can try installing the proprietary `amdgpu-pro` drivers, but this is generally not recommended.

---

## Audio Issues

### No sound or incorrect audio output device

If you are having audio issues, please try the following:

1.  Ensure that your audio device is not muted. You can use `alsamixer` in the terminal to check the volume levels.
2.  Install `pavucontrol` (PulseAudio Volume Control) for more granular control over your audio devices.

    ```bash
    sudo pacman -S pavucontrol
    ```

3.  If you are still having issues, you may need to install the `sof-firmware` package for newer hardware.

    ```bash
    sudo pacman -S sof-firmware
    ```

---

## Networking Issues

### Wi-Fi not working

If your Wi-Fi is not working, you may need to install the correct drivers for your wireless card. First, identify your wireless card:

```bash
lspci -k
```

Then, search for the appropriate driver package in the Arch Linux documentation or the AUR. For example, many Broadcom wireless cards require the `broadcom-wl` package from the AUR.

---

## Package Management Issues

### Errors while updating the system

If you encounter errors while updating your system with `sudo pacman -Syu`, it may be due to an issue with the package database or a corrupted package. Please try the following:

1.  Refresh the package database:

    ```bash
    sudo pacman -Syy
    ```

2.  Clear the package cache:

    ```bash
    sudo pacman -Scc
    ```

3.  Try updating the system again.

If the problem persists, please check the [Our Wiki](https://wiki.acreetionos.org) or come to our [Discord](https://discord.acreetionos.org) and we will do our best to help you!