# AcreetionOS Packages & Release Model

AcreetionOS builds on the incredible foundation provided by [Arch Linux](https://archlinux.org). We give full credit to Arch for their upstream work — our goal isn’t to reinvent the wheel, but to refine it and add our own touches of perfection to what they have already established.

We are **not** avoiding or distancing ourselves from the Arch Linux team.  
Our goals simply differ:
- Arch is focused on providing a **pure, rolling-release distribution** in its raw form.
- AcreetionOS aims to provide an **accessible, inclusive, and highly curated version** of Arch with sane defaults, extra polish, and a community-driven approach.

In other words: we **stand on their shoulders**, not apart from them.

---

## 📦 Package Repositories

We maintain our **own repositories** in addition to using Arch’s upstream repos.  
- **Personal Repository:** Contains AcreetionOS-specific packages, customizations, and utilities. It is already listed in your `pacman.conf` when you install AcreetionOS.  
- **Upstream Arch Repos:** Pulled directly from Arch for all standard packages, with our own fixes or improvements applied when needed.

We **host our repositories ourselves** wherever possible. This means:
- Full control over our packages.
- Updates that are intentional, tested, and not rushed.
- Sometimes slower propagation than large corporate distros — but this is by design.

---

## 🔄 Update Model

- **Stable Branch:** Updated **once a month** with curated, tested packages.
- **Testing Branch:** Synced **nightly** from Arch upstream and our own development work. We use this to test packages, catch breakages, and make improvements before they reach stable.

We monitor:
- The [Arch Linux mailing lists](https://lists.archlinux.org)
- Arch’s forums
- Community reports

…to catch major upstream issues before they impact AcreetionOS users.

---

## 🎨 Package Flow (Word Art)

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

## 🧑‍💻 Our Reality

AcreetionOS is **small, community-driven, and built by people who care deeply about quality**. Many of us, including the lead maintainer, are on disability.  
This means:
- We work around health limitations — but we do not use them as an excuse.
- We prioritize stability, safety, and usefulness over arbitrary deadlines.
- Releases come out **on time for quality**, not on a fixed calendar.

---

## 💿 ISO Release Policy

ISO images are released **when they are needed**, not on a rigid schedule.  
Reasons for a new ISO might include:
- Significant system changes
- Major security updates
- Installer improvements

We avoid overcomplicating releases or producing unnecessary ISOs.

---

## 📝 Summary

- **Stable branch:** Monthly updates.  
- **Testing branch:** Nightly syncs.  
- **Personal repo:** AcreetionOS packages, pre-configured in `pacman.conf`.  
- **Arch upstream:** We add polish to their excellent foundation while pursuing different goals.  
- **Monitoring:** Mailing lists + forums to catch issues.  
- **Reality:** Small team, self-hosted repos, health limitations — but always delivering.  
- **ISO releases:** As needed, not overproduced.  

---

> *Made with ❤️ by the AcreetionOS team.*
