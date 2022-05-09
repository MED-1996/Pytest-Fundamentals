class Geometry:

    def is_triangle(side_1: int, side_2: int, side_3: int) -> bool:
        if (side_1 + side_2 > side_3) and (side_1 + side_3 > side_2) and (side_2 + side_3 > side_1):
            return True
        return False
