# Gaming Benchmarking on AcreetionOS

Accurate benchmarking is crucial for evaluating system performance and optimizing your gaming experience. This guide provides a comprehensive overview of setting up your AcreetionOS system for gaming benchmarks, including driver installation, tool setup, and recommended methodologies.

---

## 1. Prerequisites

### Enable AUR Support

Many essential gaming and benchmarking tools are available in the Arch User Repository (AUR). Ensure AUR support is enabled in Pamac or configure your AUR helper (e.g., `yay`).

*   **Pamac (GUI):**
    1.  Open Pamac (Add/Remove Software).
    2.  Navigate to `☰ Menu > Preferences > Third Party`.
    3.  Enable "AUR support" and optionally "Check for updates from AUR".

*   **Command Line (using `yay`):**

    ```bash
    # yay is an AUR helper. If you don't have it, install it first:
    # sudo pacman -S --needed git base-devel
    # git clone https://aur.archlinux.org/yay.git
    # cd yay
    # makepkg -si
    yay -Syu
    ```

---

## 2. Graphics Driver Installation

Properly configured graphics drivers are fundamental for gaming performance. Refer to the [Common Problems and Solutions](problems.md#graphics-issues) page for detailed instructions on installing drivers for AMD, NVIDIA, and Intel GPUs.

---

## 3. Benchmarking and Performance Monitoring Tools

Install the following tools to conduct and monitor your benchmarks.

### Benchmarking Tools

*   **Vulkan Tools:** Provides `vulkaninfo` for verifying Vulkan support and `vkcube` for basic Vulkan rendering.
    *   **Pamac (GUI):** Search for `vulkan-tools`.
    *   **pacman (CLI):** `sudo pacman -S vulkan-tools`

*   **GLMark2:** An OpenGL 2.0 benchmark.
    *   **Pamac (GUI):** Search for `glmark2`.
    *   **pacman (CLI):** `sudo pacman -S glmark2`

*   **Unigine Heaven/Superposition:** Popular GPU stress tests and benchmarks.
    *   **Pamac (GUI):** Search for `unigine-heaven` (AUR) and `unigine-superposition` (AUR).
    *   **yay (CLI):** `yay -S unigine-heaven unigine-superposition`

### Performance Monitoring Tools

*   **MangoHud:** An in-game overlay for displaying FPS, frame times, GPU/CPU usage, temperatures, and more.
    *   **Pamac (GUI):** Search for `mangohud` (AUR).
    *   **yay (CLI):** `yay -S mangohud`

*   **GOverlay:** A graphical user interface for configuring MangoHud.
    *   **Pamac (GUI):** Search for `goverlay` (AUR).
    *   **yay (CLI):** `yay -S goverlay`

*   **GPU-Specific Monitoring:**
    *   **AMD:** `radeontop` (AUR) for real-time GPU usage.
        *   **yay (CLI):** `yay -S radeontop`
    *   **NVIDIA:** `nvidia-smi` (included with `nvidia-utils`) for GPU information and usage.
    *   **Intel Arc:** `intel-gpu-tools` for GPU usage monitoring.
        *   **pacman (CLI):** `sudo pacman -S intel-gpu-tools`

---

## 4. Benchmarking Methodology

To ensure consistent and comparable benchmark results, follow these guidelines:

1.  **System Warm-up:** Run a demanding application or game for 5-10 minutes before benchmarking to allow components to reach operating temperatures.
2.  **Consistent Settings:** Use identical resolution, graphics presets, and API (Vulkan/OpenGL) across all benchmark runs.
3.  **Multiple Passes:** Execute each benchmark at least three times and average the results to minimize variance.
4.  **Monitor System Load:** Utilize MangoHud or GPU-specific tools to confirm that the CPU and GPU are consistently utilized during the benchmark.
5.  **Record Key Metrics:** Document average, minimum, and maximum FPS, 1% and 0.1% low FPS values, GPU temperature, and GPU utilization.
6.  **Synthetic vs. Real-World:** Combine synthetic benchmarks (e.g., Unigine) with in-game performance monitoring (MangoHud) for a comprehensive assessment.

---

## 5. GPU-Specific Optimizations

### AMD

*   Keep your Mesa drivers updated, as new versions often bring significant performance improvements.
*   Consider using `RADV_PERFTEST=aco` in game launch options for potential performance gains with the ACO compiler.

### NVIDIA

*   Always use the proprietary NVIDIA drivers for optimal performance.
*   In the NVIDIA X Server Settings, set the "PowerMizer" mode to "Prefer Maximum Performance" for benchmarking.

### Intel Arc

*   Ensure your kernel and Mesa drivers are up-to-date for the best Arc support.
*   Prioritize Vulkan API usage whenever possible, as Arc GPUs generally perform best with Vulkan.
*   Keep `intel-media-driver` updated for hardware video acceleration.