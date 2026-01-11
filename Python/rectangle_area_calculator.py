"""
Rectangle Area Calculator

This script calculates the area of a rectangle based on width and height inputs,
and categorizes the rectangle as large, normal, or small based on the area.
"""


def calculate_rectangle_area(width, height):
    """
    Calculates the area of a rectangle.
    
    Args:
        width: Width of the rectangle
        height: Height of the rectangle
    
    Returns:
        Area of the rectangle
    """
    return width * height


def categorize_rectangle(area):
    """
    Categorizes rectangle based on area.
    
    Args:
        area: Area value
    
    Returns:
        Category string
    """
    if area > 100:
        return "Large rectangle"
    elif area == 100:
        return "Normal rectangle"
    else:
        return "The area is too small"


def main():
    """Main function to get user input and calculate rectangle area."""
    print("Rectangle Area Calculator")
    print("-" * 30)
    
    try:
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        
        if width <= 0 or height <= 0:
            print("Error: Width and height must be positive numbers")
            return
        
        area = calculate_rectangle_area(width, height)
        category = categorize_rectangle(area)
        
        print(f"\nRectangle area: {area:.2f}")
        print(f"Category: {category}")
    
    except ValueError:
        print("Error: Please enter valid numbers")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user")


if __name__ == "__main__":
    main()
