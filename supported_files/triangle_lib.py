#purpose is get familarize with  structuring the program into distinct modules that can be imported and reused.
#practicing documentation and type anotation to be more professional
class Triangle:
    """ it has different types of triangle and info"""
    def __init__(self, l: int, b: int, h: int):
        self.l = l
        self.b = b
        self.h = h
        self.properties = {"name":None,"length":self.l,"breadth":self.b,"height":self.h, "area": None, "perimeter": None}

        self.info=self.check_triangle_type()

    def check_result(self, is_valid: bool) -> str:
        """
        Evaluates the result and returns a corresponding message.

        Args:
            is_valid (bool): The boolean result to check.

        Returns:
            str: A message indicating whether the result is valid or not.
        """
        return "It's a" if is_valid else "Not a"
    
    def get_area(self) -> float:
        """Calculates the area of the triangle."""
        return 0.5 * self.l * self.b
    
    def get_perimeter(self) -> int:
        """Calculates the perimeter of the triangle."""
        return self.l + self.b + self.h
    
    def triangle_info(self) -> dict:
        """Returns a dictionary containing the triangle's properties."""
        if self.properties["name"] != None:
            self.properties["area"] = self.get_area()
            self.properties["perimeter"] = self.get_perimeter()
            return self.properties
        else:
            return self.properties    
    def is_equilateral_triangle(self) -> dict:
        """Checks whether the triangle is equilateral."""
        self.name_of_triangle = "equilateral triangle"
        res = self.check_result(self.l == self.b == self.h)
        return self.triangle_info()
    
    def is_isosceles_triangle(self) -> dict:
        """Checks whether the triangle is isosceles."""
        self.name_of_triangle = "isosceles triangle"
        res = self.check_result(self.l == self.b or self.b == self.h or self.l == self.h)
        self.properties["name"]=self.name_of_triangle
        return self.triangle_info()
    
    def is_scalene_triangle(self) -> dict:
        """Checks whether the triangle is scalene."""
        self.name_of_triangle = "scalene triangle"
        res = self.check_result(self.l != self.b and self.b != self.h and self.l != self.h)
        self.properties["name"]=self.name_of_triangle
        return self.triangle_info()
    
    def is_not_triangle(self) -> str:
        """Returns a message indicating that the given sides do not form a triangle."""
        self.name_of_triangle="It's not a triangle"
        self.properties["name"] = self.name_of_triangle
        return self.properties
    
    def check_triangle_type(self) -> dict:
        """Determines and returns the type of the triangle."""
        if self.l + self.b <= self.h or self.l + self.h <= self.b or self.b + self.h <= self.l:
            return self.is_not_triangle()
        elif self.l == self.b == self.h:
            return self.is_equilateral_triangle()
        elif self.l == self.b or self.b == self.h or self.l == self.h:
            return self.is_isosceles_triangle()
        elif self.l != self.b and self.b != self.h and self.l != self.h:
            return self.is_scalene_triangle()

# Example usage:
