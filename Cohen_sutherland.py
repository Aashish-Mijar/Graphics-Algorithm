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

def compute_code(x, y, x_min, y_min, x_max, y_max):
    """Compute region code for point (x, y)"""
    code = INSIDE
    
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
        
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
        
    return code

def cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    """Implement Cohen-Sutherland line clipping algorithm"""
    code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max)
    code2 = compute_code(x2, y2, x_min, y_min, x_max, y_max)
    accept = False
    
    clipped_points = [(x1, y1, x2, y2)]  # Store original line
    
    while True:
        # Both endpoints inside clipping window
        if code1 == 0 and code2 == 0:
            accept = True
            break
            
        # Both endpoints outside clipping window (same region)
        elif (code1 & code2) != 0:
            break
            
        # Some segment lies inside clipping window
        else:
            # Select endpoint outside clipping window
            code_out = code1 if code1 != 0 else code2
            
            # Find intersection point
            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min
                
            # Replace outside point with intersection point
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max)
                clipped_points.append((x1, y1, x2, y2))
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, x_min, y_min, x_max, y_max)
                clipped_points.append((x1, y1, x2, y2))
    
    return accept, (x1, y1, x2, y2), clipped_points

def visualize_clipping():
    """Create interactive visualization of Cohen-Sutherland algorithm"""
    fig, ax = plt.subplots(figsize=(12, 10))
    plt.subplots_adjust(bottom=0.3)
    
    # Clipping window
    x_min, x_max = 2, 8
    y_min, y_max = 2, 8
    
    # Initial line coordinates
    x1, y1 = 1, 1
    x2, y2 = 9, 9
    
    # Create clipping window rectangle
    clip_rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min, 
                                 linewidth=2, edgecolor='blue', facecolor='lightblue', alpha=0.3)
    ax.add_patch(clip_rect)
    
    # Plot region codes
    ax.text(0.5, 0.5, '1001', fontsize=10, ha='center', va='center', color='red')
    ax.text(5, 0.5, '1000', fontsize=10, ha='center', va='center', color='red')
    ax.text(9.5, 0.5, '1010', fontsize=10, ha='center', va='center', color='red')
    
    ax.text(0.5, 5, '0001', fontsize=10, ha='center', va='center', color='red')
    ax.text(5, 5, '0000', fontsize=10, ha='center', va='center', color='red')
    ax.text(9.5, 5, '0010', fontsize=10, ha='center', va='center', color='red')
    
    ax.text(0.5, 9.5, '0101', fontsize=10, ha='center', va='center', color='red')
    ax.text(5, 9.5, '0100', fontsize=10, ha='center', va='center', color='red')
    ax.text(9.5, 9.5, '0110', fontsize=10, ha='center', va='center', color='red')
    
    # Draw the original line
    original_line, = ax.plot([x1, x2], [y1, y2], 'ro-', linewidth=2, markersize=8, label='Original Line')
    
    # Draw the clipped line (initially hidden)
    clipped_line, = ax.plot([], [], 'go-', linewidth=3, markersize=10, label='Clipped Line')
    
    # Set plot properties
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Cohen-Sutherland Line Clipping Algorithm')
    ax.legend()
    
    # Add text information
    info_text = ax.text(0.02, 0.98, '', transform=ax.transAxes, verticalalignment='top',
                       bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    # Update function for the visualization
    def update_visualization():
        accept, clipped_coords, all_steps = cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max)
        
        # Update original line
        original_line.set_data([x1, x2], [y1, y2])
        
        # Update clipped line
        if accept:
            cx1, cy1, cx2, cy2 = clipped_coords
            clipped_line.set_data([cx1, cx2], [cy1, cy2])
            clipped_line.set_visible(True)
            info_text.set_text(f'Line Accepted!\nClipped: ({cx1:.2f}, {cy1:.2f}) to ({cx2:.2f}, {cy2:.2f})')
        else:
            clipped_line.set_visible(False)
            info_text.set_text('Line Rejected!')
        
        # Draw intermediate steps
        for i, step in enumerate(all_steps):
            sx1, sy1, sx2, sy2 = step
            if i == 0:
                # Original line
                ax.plot([sx1, sx2], [sy1, sy2], 'ro-', alpha=0.3, linewidth=1)
            else:
                # Intermediate steps
                ax.plot([sx1, sx2], [sy1, sy2], 'mo-', alpha=0.5, linewidth=1, markersize=4)
        
        plt.draw()
    
    # Initial visualization
    update_visualization()
    
    # Create sliders for line endpoints
    axcolor = 'lightgoldenrodyellow'
    ax_x1 = plt.axes([0.2, 0.2, 0.65, 0.03], facecolor=axcolor)
    ax_y1 = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor=axcolor)
    ax_x2 = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
    ax_y2 = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor=axcolor)
    
    slider_x1 = Slider(ax_x1, 'X1', 0.0, 10.0, valinit=x1)
    slider_y1 = Slider(ax_y1, 'Y1', 0.0, 10.0, valinit=y1)
    slider_x2 = Slider(ax_x2, 'X2', 0.0, 10.0, valinit=x2)
    slider_y2 = Slider(ax_y2, 'Y2', 0.0, 10.0, valinit=y2)
    
    def update(val):
        global x1, y1, x2, y2
        x1 = slider_x1.val
        y1 = slider_y1.val
        x2 = slider_x2.val
        y2 = slider_y2.val
        
        # Clear previous intermediate steps
        for line in ax.lines[2:]:  # Keep original and clipped lines
            line.remove()
        
        update_visualization()
    
    slider_x1.on_changed(update)
    slider_y1.on_changed(update)
    slider_x2.on_changed(update)
    slider_y2.on_changed(update)
    
    # Add reset button
    resetax = plt.axes([0.8, 0.25, 0.1, 0.04])
    button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
    
    def reset(event):
        slider_x1.reset()
        slider_y1.reset()
        slider_x2.reset()
        slider_y2.reset()
    
    button.on_clicked(reset)
    
    # Add example buttons
    examples_ax = plt.axes([0.1, 0.25, 0.15, 0.15])
    example_text = examples_ax.text(0.5, 0.5, 'Examples:\n1. Completely Inside\n2. Completely Outside\n3. Partially Inside', 
                                   transform=examples_ax.transAxes, ha='center', va='center', fontsize=9)
    examples_ax.axis('off')
    
    def set_example_inside(event):
        slider_x1.set_val(3)
        slider_y1.set_val(4)
        slider_x2.set_val(7)
        slider_y2.set_val(6)
    
    def set_example_outside(event):
        slider_x1.set_val(0)
        slider_y1.set_val(1)
        slider_x2.set_val(1)
        slider_y2.set_val(0)
    
    def set_example_partial(event):
        slider_x1.set_val(1)
        slider_y1.set_val(1)
        slider_x2.set_val(9)
        slider_y2.set_val(9)
    
    # Add example buttons
    inside_ax = plt.axes([0.1, 0.2, 0.2, 0.04])
    outside_ax = plt.axes([0.1, 0.15, 0.2, 0.04])
    partial_ax = plt.axes([0.1, 0.1, 0.2, 0.04])
    
    button_inside = Button(inside_ax, 'Inside', color=axcolor)
    button_outside = Button(outside_ax, 'Outside', color=axcolor)
    button_partial = Button(partial_ax, 'Partial', color=axcolor)
    
    button_inside.on_clicked(set_example_inside)
    button_outside.on_clicked(set_example_outside)
    button_partial.on_clicked(set_example_partial)
    
    plt.show()

if __name__ == "__main__":
    visualize_clipping()