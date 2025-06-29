import pyautogui
from PIL import Image
import time

# print("Move mouse to the top-left of the progress bar...")
# time.sleep(5)
# print("Mouse position:", pyautogui.position())


# Region of the screen to monitor
region_x = 1212
region_y = 834
region_width = 458
region_height = 1

# RGB color when the region is idle
IDLE_COLOR = (205, 185, 150)

# Allowed color difference before considering the pixel changed
TOLERANCE = 20


def color_diff(c1, c2):
    """Calculate simple average absolute difference between two RGB colors."""
    return sum(abs(a - b) for a, b in zip(c1, c2))


print(
    f"Watching region ({region_x}, {region_y}, {region_width}, {region_height})"
    " for color change..."
)
while True:
    screenshot = pyautogui.screenshot(
        region=(region_x, region_y, region_width, region_height)
    )
    for dx in range(region_width):
        current_color = screenshot.getpixel((dx, 0))
        if color_diff(current_color, IDLE_COLOR) > TOLERANCE:
            click_x = region_x + dx
            click_y = region_y
            pyautogui.click(click_x, click_y)
            print(
                f"Clicked at ({click_x}, {click_y}) when color changed to {current_color}"
            )
            raise SystemExit
    time.sleep(0.001)
