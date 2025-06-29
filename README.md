# dig.io example script

`click_on_color_change.py` waits for a specific screen pixel to change color and clicks on it. Update `x` and `y` with the desired coordinates before running.

`scan_region_click.py` watches a small region for the target color to change and clicks on the exact pixel that changed. Update the `region_*` values for your progress bar area.

Example usage:
```bash
python click_on_color_change.py
python scan_region_click.py
```
