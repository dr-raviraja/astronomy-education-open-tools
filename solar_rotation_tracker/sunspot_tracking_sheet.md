# Solar Rotation & Sunspot Tracking Log
**Developer:** Dr. Ravi Raja Pothineni (ASTRO / Novae Astro Club)

> **Safety First:** Never look at the Sun with the naked eye, binoculars, or an unfiltered telescope. Use a certified solar filter on the front of the telescope or project the solar image safely onto a white screen.

## How to Track Sunspots Across Days
1. **Mark a Reference Circle:** Draw a circle on a white projection card or solar log sheet and mark **North (N)**, **South (S)**, **East (E)**, and **West (W)** according to your optical setup.
2. **Sketch Active Regions:** Trace the positions of sunspot groups (umbra and penumbra) at roughly the same time of day every 1–2 days over 1 to 2 weeks.
3. **Measure Motion:** Note how each sunspot group shifts across the solar disk from day to day as the Sun rotates.

## Daily Observation Log

| Date | Time (IST) | No. of Sunspot Groups | Total Spots Counted | Observed Shift / Notes |
| :--- | :--- | :--- | :--- | :--- |
| Day 1 | | | | |
| Day 2 | | | | |
| Day 4 | | | | |
| Day 6 | | | | |
| Day 8 | | | | |

## Estimating Solar Rotation Period
- Suppose a prominent sunspot group moves across the visible face of the Sun (about half a full rotation, or $\sim 180^\circ$, in roughly 13.5 days).
- **Synodic rotation period ($P_{\text{syn}}$):** A full $360^\circ$ return to the same apparent position on the Sun takes roughly **27 days** near the solar equator (and slightly longer at higher solar latitudes due to differential rotation).
- **Sidereal rotation period ($P_{\text{sid}}$):** Because Earth also moves along its orbit around the Sun during those ~27 days, convert the synodic period to the true sidereal rotation period using:

$$\frac{1}{P_{\text{sid}}} = \frac{1}{P_{\text{syn}}} + \frac{1}{P_{\text{Earth}}}$$

where $P_{\text{Earth}} \approx 365.25\text{ days}$.

---

### Next Step for Your Repo
Upload these three Markdown files into `spectroscope_cardboard/`, `crater_impact_lab/`, and `solar_rotation_tracker/` alongside your `generate_sundial_svg.py` and `teacher_guide_en_te.md` in `sundial_17_5N/`, and your `astronomy-education-open-tools` repository will have all four core modules in place.
