"""
DIGM 131 - Assignment 2: Procedural Pattern Generator
======================================================

OBJECTIVE:
    Use loops and conditionals to generate a repeating pattern of 3D objects
    in Maya. You will practice nested loops, conditional logic, and
    mathematical positioning.

REQUIREMENTS:
    1. Use a nested loop (a loop inside a loop) to create a grid or pattern
       of objects.
    2. Include at least one conditional (if/elif/else) that changes an
       object's properties (type, size, color, or position offset) based
       on its row, column, or index.
    3. Generate at least 25 objects total (e.g., a 5x5 grid).
    4. Comment every major block of code explaining your logic.

GRADING CRITERIA:
    - [25%] Nested loop correctly generates a grid/pattern of objects.
    - [25%] Conditional logic visibly changes object properties based on
            position or index.
    - [20%] At least 25 objects are generated.
    - [15%] Code is well-commented with clear explanations.
    - [15%] Pattern is visually interesting and intentional.

TIPS:
    - A 5x5 grid gives you 25 objects. A 6x6 grid gives you 36.
    - Use the loop variables (row, col) to calculate X and Z positions.
    - The modulo operator (%) is great for alternating patterns:
          if col % 2 == 0:    # every other column
    - You can vary: primitive type, height, width, position offset, etc.

COMMENT HABITS (practice these throughout the course):
    - Add a comment before each logical section explaining its purpose.
    - Use inline comments sparingly and only when the code is not obvious.
    - Keep comments up to date -- if you change the code, update the comment.
"""
 """Generate a procedural pattern of objects using nested loops.

    This function should:
        1. Define variables for rows, columns, and spacing.
        2. Use a nested for-loop to iterate over rows and columns.
        3. Inside the loop, use a conditional to vary object properties.
        4. Create and position each object.
    """
import maya.cmds as cmds

# Clear scene
cmds.file(new=True, force=True)


def generate_pattern():

    # Grid settings
    num_rows = 5
    num_cols = 5
    spacing = 3.0

    # Center grid
    x_offset = (num_cols - 1) * spacing * 0.5
    z_offset = (num_rows - 1) * spacing * 0.5

    # Loop through grid
    for row in range(num_rows):
        for col in range(num_cols):

            # Default sizes
            cube_size = 2.0
            sphere_radius = 0.5
            cylinder_radius = 0.8
            cylinder_height = 2.0

            # Change values based on row
            if row % 2 == 0:
                cube_size = 2.5
                sphere_radius = 1.0
                cylinder_height = 3.0
            else:
                cube_size = 1.5
                sphere_radius = 0.5
                cylinder_height = 1.5

            # Position
            x_pos = col * spacing - x_offset
            z_pos = row * spacing - z_offset

            # Alternate object types (3 different shapes)
            if (row + col) % 3 == 0:
                obj = cmds.polyCube(width=cube_size, height=cube_size, depth=cube_size)[0]

            elif (row + col) % 3 == 1:
                obj = cmds.polySphere(radius=sphere_radius)[0]

            else:
                obj = cmds.polyCylinder(radius=cylinder_radius, height=cylinder_height)[0]

            # Move object into place
            cmds.move(x_pos, 0, z_pos, obj)

# ---------------------------------------------------------------------------
# Run the generator
# ---------------------------------------------------------------------------
generate_pattern()

# Frame everything in the viewport.
cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")
