class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def plus(self, v):
        new_coodinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coodinates)

    def minus(self, v):
        new_coodinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coodinates)

    def times_scalar(self, c):
        new_coodinates = [c*x for x in self.coordinates]
        return Vector(new_coodinates)


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
