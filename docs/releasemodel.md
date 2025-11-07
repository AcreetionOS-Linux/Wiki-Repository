# AcreetionOS Release Model

AcreetionOS is a rolling-release distribution based on Arch Linux. We leverage the power and flexibility of Arch while providing a curated and stable experience for our users. This document outlines our release model and package management strategy.

---

## Relationship with Arch Linux

AcreetionOS is not a fork of Arch Linux, but rather a distribution that builds upon it. We use the Arch Linux package repositories as our upstream source and add our own layer of customization and testing. Our goal is to make Arch Linux more accessible to a wider audience by providing a user-friendly installer, sane defaults, and a stable release cycle.

---

## Package Repositories

AcreetionOS uses a combination of our own package repositories and the official Arch Linux repositories.

*   **AcreetionOS Repository:** This repository contains all AcreetionOS-specific packages, including our branding, themes, and system configuration tools. It is enabled by default in `/etc/pacman.conf`.
*   **Arch Linux Repositories:** We pull packages from the official Arch Linux repositories. These packages are then moderated and tested by our team to ensure stability before being released to our users. This ensures that our users have access to a large and up-to-date software collection, with an added layer of quality control.
*   **ACUR (AcreetionOS Community User Repository):** Similar to the AUR, the ACUR is a place for community-contributed packages made specifically for AcreetionOS. These packages generally come from the Chaotic AUR. Those of which do not, come directly from the AcreetionOS Team.
*   **AUR:** You have access to the vast collection of community-maintained packages for Arch Linux.
*   **Flatpak:** We also include support for Flatpak out of the box. This allows you to install sandboxed applications that work across different Linux distributions.
*   **Snapd:** We do not officially support Snapd, although, you can install it from the AUR. We will do our best to support you with it, but we can not make any promises on full functionality.

We host our own repository to ensure that we have full control over the packages we ship and to provide a stable and tested experience for our users. If you are interested in hosting a package mirror, please contact us at `developers.acreetionos.org` via email. Requests will be evaluated based on end-user interest and our current needs.

---

## Update Cycle

We offer two main branches for our users:

*   **Stable Branch:** This is the default branch for all AcreetionOS users. It is updated on a regular basis, typically every two weeks, with packages that have been thoroughly tested by our team and the community. This approach provides a balance between having up-to-date software and a stable system. In addition to regular updates, hotfixes are released promptly for any significant breakages.
*   **Testing Branch:** This branch is for users who want to get the latest packages as soon as they are available. It is synced nightly from the Arch Linux upstream repositories and our own development branches. This branch is intended for developers and experienced users who are willing to deal with potential instability.

We actively monitor the Arch Linux mailing lists and forums to stay informed about any upstream issues that may affect our users.

---

## Package Flow

The following diagram illustrates our package flow from the Arch Linux upstream to our stable users:

```
   ┌────────────────────────────┐
   │    Arch Linux Upstream     │
   └──────────────┬─────────────┘
                  │
          Nightly Sync
                  │
   ┌──────────────▼─────────────┐
   │  AcreetionOS Testing Repo  │
   └──────────────┬─────────────┘
                  │
     Package Testing & Tweaks
                  │
   ┌──────────────▼─────────────┐
   │  AcreetionOS Stable Repo   │
   └──────────────┬─────────────┘
                  │
             Monthly Push
                  │
   ┌──────────────▼─────────────┐
   │ AcreetionOS Stable Users   │
   └────────────────────────────┘
```

---

## ISO Release Policy

New ISO images are released on an as-needed basis. We do not follow a fixed release schedule for our ISOs. A new ISO may be released for any of the following reasons:

*   Significant changes to the base system.
*   Major updates to the installer.
*   Important security fixes that require a new installation medium.

Our goal is to provide up-to-date ISO images without creating unnecessary work for our developers or confusion for our users.