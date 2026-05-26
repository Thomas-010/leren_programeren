from test_lib import test, report
import math
 
def calculate_cilinder_content(height: float, diameter: float) -> float:
    radius = diameter / 2
    content = radius * radius * math.pi * height
    return round(content, 1)

diameter = 8.0
height = 5.0
expect_content = 251.3
name = f'test cilinder: diameter={diameter} height={height}'
test(name, expect_content, calculate_cilinder_content(height, diameter))
 
diameter = 11.0
height = 7.0
expect_content = 665.2
name = f'test cilinder: diameter={diameter} height={height}'
test(name, expect_content, calculate_cilinder_content(height, diameter))
 
diameter = 18.0
height = 7.0
expect_content = 1781.3
name = f'test cilinder: diameter={diameter} height={height}'
test(name, expect_content, calculate_cilinder_content(height, diameter))
 
diameter = 15.0
height = 2.0
expect_content = 353.4
name = f'test cilinder: diameter={diameter} height={height}'
test(name, expect_content, calculate_cilinder_content(height, diameter))
 
diameter = 0.0
height = 6.0
expect_content = 0.0
name = f'test cilinder: diameter={diameter} height={height}'
test(name, expect_content, calculate_cilinder_content(height, diameter))
 
report()