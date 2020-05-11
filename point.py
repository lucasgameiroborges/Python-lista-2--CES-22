class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect_x(self):
        q = Point(self.x, (-1)*self.y)
        return q

    def slope_from_origin(self):
        if self.x != 0:
            return self.y/self.x
        else:
            return 1000

    def get_line_to(self, ponto):
        q = Point((ponto.y - self.y)/(ponto.x - self.x), self.y - self.x*((ponto.y - self.y)/(ponto.x - self.x)))
        return q

