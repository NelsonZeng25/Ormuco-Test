class Line():
    # Simple Line class with x1 and x2 as attributes
    # When initializing, it makes sure that x1 is always less or equal to x2 and assigns the variable accordingly if it's not respected
    # It also checks if x1 and x2 are both valid inputs by attempting to int() them. If they're not valid, set x1 and x2 to None
    def __init__(self, x1, x2):
        try:
            if int(x1) <= int(x2):
                self.x1 = int(x1)
                self.x2 = int(x2)
            else:
                self.x1 = int(x2)
                self.x2 = int(x1)
        except ValueError:
            self.x1 = None
            self.x2 = None


def overlap(line1, line2):
    """
        There are only 5 possible outcomes for the 2 lines
        1. Line 1 is before line 2 and they don't overlap
        2. Line 1 is before line 2 and they overlap
        3. Line 1 is on top of line 2 so they overlap
        4. Line 1 is after line 2 and they overlap
        5. Line 1 is after line 2 and they don't overlap
        The solution here is to check for only when they don't overlap since that will lead to less comparisons
        We also check if Line 1 and Line 2 have valid inputs and return False if they're invalid
    """
    if (line1 == None or line2 == None or line1.x1 == None or line2.x1 == None):
        print("Invalid input")
        return False
    else:
        return not (line2.x2 < line1.x1 or line1.x2 < line2.x1)
        # This basically checks if the lines don't overlap and returns the negation since they must overlap if this condition is not met.