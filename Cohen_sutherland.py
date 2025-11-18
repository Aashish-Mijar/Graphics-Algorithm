import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Button, Slider
import numpy as np

# Cohen-Sutherland region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

