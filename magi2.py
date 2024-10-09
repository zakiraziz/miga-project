import turtle
import random

# Initialize the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
tree = turtle.Turtle()
tree.speed(0)  # Fastest drawing speed
tree.left(90)  # Start the turtle facing upwards
tree.penup()
tree.goto(0, -250)  # Set starting position for the tree trunk
tree.pendown()
tree.color("brown")  # Initial color for the trunk

# Recursive function to draw a fractal tree
def draw_branch(branch_length, angle, depth):
    if branch_length > 5 and depth > 0:  # Base case for recursion
        # Vary color based on depth
        tree.pensize(max(1, depth // 2))
        tree.color((0, depth * 10 % 255, 0))
        
        # Draw the main branch
        tree.forward(branch_length)
        
        # Left branch
        tree.left(angle)
        draw_branch(branch_length - random.randint(10, 20), angle, depth - 1)
        
        # Right branch
        tree.right(2 * angle)
        draw_branch(branch_length - random.randint(10, 20), angle, depth - 1)
        
        # Go back to the previous position and reset angle
        tree.left(angle)
        tree.penup()
        tree.backward(branch_length)
        tree.pendown()

# Function to initiate the fractal tree drawing
def fractal_tree():
    tree.penup()
    tree.setpos(0, -250)  # Starting position for the trunk
    tree.pendown()
    draw_branch(branch_length=100, angle=30, depth=10)  # Call the recursive function

# Main execution
fractal_tree()

# Close the turtle screen on click
screen.exitonclick()
