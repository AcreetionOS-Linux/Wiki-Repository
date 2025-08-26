# Enabling Fractional Scaling on T2 MacBooks with GNOME

When running GNOME on a T2 MacBook, the high-resolution display can make user interface elements appear excessively small. To remedy this, you'll need to enable **fractional scaling**.

Fractional scaling in GNOME is considered an *experimental* feature. This means that while it is functional, some applications might not scale correctly and you could potentially experience some visual glitches.

By default, the display settings in GNOME will only offer scaling options of **100%** or **200%**. To enable more granular control, run the following command in your terminal:

```bash
gsettings set org.gnome.mutter experimental-features "['scale-monitor-framebuffer']"
```

After running this command, you may need to **log out and log back in** or **restart your system** for the new settings to appear. Once applied, you will see additional incremental scaling options in the **"Displays"** section of the GNOME settings.

For displays with a resolution of **2880x1800**, neither the 100% nor the 200% default scaling options are ideal:  

- At **100%**, everything will likely be too small to see comfortably.  
- At **200%**, everything will appear too large.  

A scaling factor of **150%** is recommended to make everything on the screen easily visible and usable.
