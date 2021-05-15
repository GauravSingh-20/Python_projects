import math
def paint_area(Height, width,can_coverage):
    area=Height*width

    cans_required=math.ceil(area/can_coverage)
    print(f"You have to paint {area} m sqare . You require {cans_required} cans to paint the whole area ")

height=int(input("Enter the height of the wall : "))
width=int(input("enter the width of the wall : "))
paint_area(height,width,5)