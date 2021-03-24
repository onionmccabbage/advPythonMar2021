class Point():
    points = 0 # static property
    __slots__ = ('x','y') # the names of the attributes are strings 'x' and 'y'
    @staticmethod
    def how_many_points():
        return Point.points
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.points += 1
        # we can restrict the slots for class properties
    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy
    def where_am_i(self):
        print('Point instance at x:{0:.2f} y:{1:.2f}'.format(self.x, self.y))
    def display(self):
        return (self.x, self.y)

if __name__ == '__main__':
    p1 = Point(5, 7)
    # if we try to add other parameters it will fail due to the slots restriction
    p2 = Point(3, 4)
    # p2.other = 99 # fails because slots is restricted to x and y
    p2.where_am_i()

