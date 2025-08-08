\# Comprehensive Gaming Benchmark & Setup Guide for Arch-Based Systems (Pamac GUI)

This guide will walk you through:

\- Enabling AUR support in Pamac

\- Installing all necessary benchmarking & gaming tools (including GPU drivers)

\- Setting up for AMD, NVIDIA, and Intel Arc GPUs

\- How to run benchmarks and interpret results

\- Recommended gaming benchmark methodologies

\---

\## 1. Enable AUR Support in Pamac

1\. Open \*\*Pamac\*\* (also called "Add/Remove Software" in your applications menu).

2\. Click the \*\*☰\*\* menu in the top right corner.

3\. Select \*\*Preferences\*\* (enter your password if asked).

4\. Go to the \*\*Third Party\*\* tab.

5\. Enable \*\*AUR support\*\* and optionally check \*\*Enable AUR updates\*\*.

6\. Close Preferences.

\---

\## 2. Install GPU Drivers

\### AMD

1\. Search for and install:

\- \`mesa\`

\- \`mesa-utils\`

\- \`vulkan-radeon\`

\- \`lib32-vulkan-radeon\`

2\. For performance monitoring:

\- \`radeontop\` (AUR) — shows GPU usage in real-time.

\### NVIDIA

1\. Search for and install:

\- \`nvidia\`

\- \`nvidia-utils\`

\- \`lib32-nvidia-utils\`

\- \`vulkan-icd-loader\`

\- \`lib32-vulkan-icd-loader\`

2\. For performance monitoring:

\- \`nvidia-smi\` (included with \`nvidia-utils\`).

\### Intel Arc

1\. Search for and install:

\- \`mesa\`

\- \`mesa-utils\`

\- \`vulkan-intel\`

\- \`lib32-vulkan-intel\`

\- \`intel-gpu-tools\` (for GPU usage monitoring)

2\. Make sure your kernel is up to date for the latest Arc support.

\---

\## 3. Install Benchmarking & Gaming Tools

Search for and install the following \*\*using Pamac GUI\*\*:

\### Benchmarking Tools

\- \`vulkan-tools\` — Vulkan info and benchmarking.

\- \`glmark2\` — OpenGL benchmark.

\- \`unigine-heaven\` (AUR) — GPU stress test.

\- \`unigine-superposition\` (AUR) — modern GPU stress test.

\- \`gpu-burn\` (AUR) — GPU stress/thermal testing.

\- \`mangohud\` (AUR) — in-game performance overlay.

\- \`goverlay\` (AUR) — GUI for MangoHud settings.

\### Gaming Tools

\- \`bottles\` (AUR) — manage Wine environments.

\- \`protonup-qt\` (AUR) — install custom Proton-GE builds.

\- \`lutris\` — manage games from multiple platforms.

\- \`steam\` — Steam client.

\- \`heroic-games-launcher-bin\` (AUR) — Epic & GOG games launcher.

\---

\## 4. How to Use the Tools

\### MangoHud

\- Launch games with \`mangohud\` to display FPS, frame time, GPU usage, temperature, etc.

\- Example (terminal):

\`\`\`bash

mangohud glxgears

In Steam:

Right-click a game → Properties → In Launch Options, type:

mangohud %command%

GOverlay

Open GOverlay from your applications menu.

Customize MangoHud's appearance, metrics, and position.

Vulkan-Tools

Run:

vulkaninfo

to verify Vulkan support and see GPU capabilities.

GLMark2

Run:

glmark2

for a quick OpenGL performance score.

Unigine Heaven / Superposition

Open from your applications menu after install.

Select resolution and settings.

Run benchmark → record score.

GPU Usage Monitoring

AMD: radeontop

NVIDIA: nvidia-smi

Intel Arc: intel\_gpu\_top

5\. Recommended Benchmark Methodology

Warm up your GPU — Run a quick game or stress test for 5 minutes before benchmarking to normalize temps.

Use consistent settings — Always benchmark with the same resolution, graphics preset, and API (e.g., Vulkan or OpenGL).

Run multiple passes — Run each benchmark 3 times, average the results.

Monitor system load — Use MangoHud to ensure CPU/GPU usage is maxed consistently.

Record data — Note down:

FPS average, min, and max

1% and 0.1% low FPS values

GPU temperature

GPU utilization

Test both synthetic and real-world scenarios — Use Unigine for stress, MangoHud in actual games for real usage numbers.

Compare across APIs — If a game supports Vulkan and OpenGL, test both.

6\. Quick GPU-Specific Notes

AMD

Mesa updates can significantly improve performance; keep your system updated.

Use RADV\_PERFTEST=aco in launch options for some performance boosts.

NVIDIA

Use proprietary drivers (nvidia, not nouveau) for best performance.

Enable Prefer Maximum Performance in NVIDIA Settings for benchmarking.

Intel Arc

Requires latest kernel + Mesa for best results.

Arc performs best in Vulkan; use it whenever possible.

Keep intel-media-driver updated for video acceleration.

✅ With these steps, you now have everything needed for accurate Linux gaming benchmarks and can manage your gaming library across multiple platforms with maximum performance.

This is now \*\*everything\*\* — one big copy/paste box, covers AMD, NVIDIA, and Intel Arc, gives installation + usage + methodology, all GUI-only via Pamac for installing.

If you want, I can also prepare a \*\*matching illustrated version\*\* with Pamac screenshots for a polished PDF guide.
