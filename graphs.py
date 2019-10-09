class Parabola:

    def __init__(self, points = None, equation = None, upper_limit = 'AUTO', lower_limit = 'AUTO'):
    # self.a, self.b and self.c reflects constants in the standard form
    # of a parabola equation, which is
    #                  y = a * x^2 + b * x + c
    # The upper and lower limit are required to prevent very high values from
    # decreasing the confidence score. If you want the confidence to be basically
    # 100% at x=7, the confidence will start to lower and at x=10 the confidence
    # might be 80%. Assigning a low confidence to a pair with 10 word matches is
    # obviously wrong. Thus, in this case, any values past the upper_limit will
    # automatically have the same confidence as that of the limit.
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

        if len(points) >= 3:
            self.set_equation_from_points(points)

            # If the limit is 'AUTO', it is assigned to the values first and last x values given
            if self.lower_limit == 'AUTO':
                self.lower_limit = points[0][0]
            if self.upper_limit == 'AUTO':
                self.upper_limit = points[2][0]

        elif len(equation) >= 3:
            self.a = equation[0]
            self.b = equation[1]
            self.c = equation[2]

            if self.lower_limit == 'AUTO':
                self.lower_limit = None
            if self.upper_limit == 'AUTO':
                self.upper_limit = None

        else:
            print("Error in the given parabola parameters. Not enough points or equation parameters where given")


    def set_equation_from_points(self, points):
        # adapted from http://chris35wills.github.io/parabola_python/

        x1, y1, x2, y2, x3, y3 = points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1]

        denominator = (x1 - x2) * (x1 - x3) * (x2 - x3)
        self.a = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / denominator
        self.b = (x3 * x3 * (y1 - y2) + x2 * x2 * (y3 - y1) + x1 * x1 * (y2 - y3)) / denominator
        self.c = (x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / denominator


    def print_range(self, resolution = 1):
        print('Points in graph:\t', end='')

        x = 0
        while x <= self.upper_limit + resolution:
            print(str(x) + ":" + str(round(self.y(x), 2)), end=', ')
            x += resolution


    def y(self, x):
        if x <= self.lower_limit and self.lower_limit is not None:
            x = self.lower_limit
        elif x >= self.upper_limit and self.upper_limit is not None:
            x = self.upper_limit

        return self.a * x ** 2 + self.b * x + self.c




# Creates a "Polygon" from a set of points (basically it just draws lines between
# these points.
# The result is essentially a linear graph with different equations at different sections
# It could look something like this:
'''

  ^
  |
  y
                    ̷	
                  ̷	
                ̷	
               /
              /
             /	
    ________/	            
                                
                                
                                x ->

'''
class Polygon:

    def __init__(self, points):
        self.points = points


    def y(self, x):
        if x < self.points[0][0]:
            return self.points[0][1]
        elif x > self.points[len(self.points) - 1][0]:
            return self.points[len(self.points) - 1][1]
        else:  # ok, the x input is somewhere between the points
            i = 0
            while self.points[i + 1][0] < x:
                i += 1

            y = self.points[i][1] + \
                (x - self.points[i][0]) * \
                (self.points[i + 1][1] - self.points[i][1]) / (self.points[i + 1][0] - self.points[i][0])

            return y

