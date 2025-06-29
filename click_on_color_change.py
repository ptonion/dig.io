import pyautogui
import time

print("Move mouse to the top-left of the progress bar...")
time.sleep(5)
print("Mouse position:", pyautogui.position())

# Coordinates of pixel to monitor
x = 100  # TODO: replace with actual x coordinate
y = 100  # TODO: replace with actual y coordinate

# RGB color when the pixel is idle
IDLE_COLOR = (205, 185, 150)

# Allowed color difference before considering the pixel changed
TOLERANCE = 20


def color_diff(c1, c2):
    """Calculate simple average absolute difference between two RGB colors."""
    return sum(abs(a - b) for a, b in zip(c1, c2))


print(f"Watching pixel ({x}, {y}) for color change...")
while True:
    current_color = pyautogui.pixel(x, y)
    if color_diff(current_color, IDLE_COLOR) > TOLERANCE:
        pyautogui.click(x, y)
        print(f"Clicked at ({x}, {y}) when color changed to {current_color}")
        break
    time.sleep(0.001)
