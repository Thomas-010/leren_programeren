import math

def calculate_cilinder_content(height: float, diameter: float) -> float:
    radius = diameter / 2
    content = radius * radius * math.pi * height
    return round(content, 1)

print(calculate_cilinder_content(5.0, 8.0))  
print(calculate_cilinder_content(7.0, 11.0))  
print(calculate_cilinder_content(7.0, 18.0)) 
print(calculate_cilinder_content(2.0, 15.0)) 
print(calculate_cilinder_content(6.0, 0.0))   

