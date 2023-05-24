from abc import ABC, abstractmethod

class Geometry_prop(ABC):
    @abstractmethod
    def types(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def angle_sum(self):
        pass

intro_input = input("Welcome to 'GEOMETRY WITH FUN'"
                    "\nTo learn 3-sided geometry, enter '3'"
                    "\nTo learn 4-sided geometry, enter '4'"
                    "\n To learn Circular geometry, enter '0'"
                    "\nTo exit, enter 'Exit': ")
input_keys = ['3', '4', '0', 'Exit']
while intro_input in input_keys:
    if intro_input == '3':

        class Triangles(Geometry_prop):
            def __init__(self, side1, side2):
                self.side1 = side1
                self.side2 = side2

            def types(self):
                print("There are in general three types of triangles. They are as follows:"
                      "\n1. Equilateral triangle"
                      "\n2. Isoceles triangle"
                      "\n3. Isoceles-right triangle")

            def area(self):
                height = (self.side1**2 - self.side2**2)**0.5
                length = self.side2
                return 2*(0.5 * height * length)

            def angle_sum(self):
                print("The sum of the interior angles of any triangle is always '180 degrees'.")

        seq = ["1st", "2nd", "3rd"]
        tri_sides = []
        for i in seq:
            input_len = int(input(f"Please enter the length of {i} side: "))
            while True:
                if input_len > 0:
                    tri_sides.append(input_len)
                    break
                else:
                    input_len = int(input("Can't be a value of any Triangle's leg!"
                                          "\nPlease input a real value: "))

        while tri_sides[2] > tri_sides[0] + tri_sides[1] or tri_sides[2] < tri_sides[0] - tri_sides[1]:
            input_len = int(input("ERROR!\nAccording to Triangle's Third rule: 3rd side of any triangle"
                                  " must be less than the sum of other two sides or "
                                  "greater than the substraction of other "
                                  "two side!\nPlease enter an acceptable value: "))
            tri_sides[2] = input_len
        sorted_tri_sides = sorted(tri_sides)

        if sorted_tri_sides[0] == sorted_tri_sides[1] == sorted_tri_sides[2]:
            tri = Triangles(sorted_tri_sides[0], sorted_tri_sides[1]*0.5)
            tri.types()
            tri.angle_sum()
            print(f"According to your input, it's an 'Equilateral triangle'."
                  f"\nAnd the area of such triangle is: {tri.area()}")

        elif sorted_tri_sides[1] == sorted_tri_sides[2]:
            tri = Triangles(sorted_tri_sides[0], sorted_tri_sides[1] * 0.5)
            tri.types()
            tri.angle_sum()
            print(f"According to your input, it's an 'Isoceles/Isoceles-Right triangle'."
                  f"\nAnd the area of such triangle is: {tri.area()}")

        else:
            tri = Triangles(sorted_tri_sides[0], sorted_tri_sides[1] * 0.5)
            tri.types()
            tri.angle_sum()
            print("According to your input, it's an 'Irregular triangle'."
                  "\nAnd the area calculation required much more complex code!")

        intro_input = input("Which one you want to learn next?"
                            "\nPick as you like."
                            "\nTo learn 3-sided geometry, enter '3'"
                            "\nTo learn 4-sided geometry, enter '4'"
                            "\n To learn Circular geometry, enter '0'"
                            "\nTo exit, enter 'Exit': ")

        if intro_input == '0':

            class Circle(Geometry_prop):




