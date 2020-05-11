class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

class Plotter:

    def plot(self, ratio, topleft):
        # plotting logic
        print('Plotting at {0}, ratio {1}.'.format(topleft, ratio))

class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'

class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side

class RegularHexagon(RegularPolygon):
    geometric_type = 'RegularHexagon'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)

class Square(RegularPolygon):
    geometric_type = 'Square'

    def area(self):
        return self.side * self.side

class Rectangle2x1(Polygon):
    geometric_type = 'Rectangle'



class Circle(Shape):
    geometric_type = 'Circle'

hexagon = RegularHexagon(12)
square = Square(12)
rectangle = Rectangle2x1()
circle = Circle()

print(hexagon.__class__.__mro__)
print(square.__class__.__mro__)
print(rectangle.__class__.__mro__)
print(circle.__class__.__mro__)

# como se pode perceber pelos outputs, os MROs nada mais sao do que a
# sequencia das classes pai do objeto (na ordem do python)


