#purpose is get familarize with  structuring the program into distinct modules that can be imported and reused.
#practicing documentation and type anotation to be more professional
from supported_files.triangle_lib import *
def get_triangle_dimensions():
    # Initialize the dictionary with keys for length, breadth, and height
    dict_dimensions = {"length": None, "breadth": None, "height": None}
    
    # Iterate through the dictionary to get user input for each dimension
    for key in dict_dimensions.keys():
        dict_dimensions[key] = int(input(f"Enter {key}: "))
    
    l,b,h=dict_dimensions.values()
    
    #return l,b,h
    return l,b,h

l,b,h=get_triangle_dimensions()
# print(Triangle(5,5,5).info)