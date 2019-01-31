





class Parabola:


    def __init__(self, points=[], equation=[], upper_limit = 'AUTO', lower_limit = 'AUTO'):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

        if len(points) >= 3:
            self.a, self.b, self.c = self.equation_from_points(points)

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



    def equation_from_points(self, points):
        # adapted from http://chris35wills.github.io/parabola_python/

        x1, y1, x2, y2, x3, y3 = points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1]

        denominator = (x1 - x2) * (x1 - x3) * (x2 - x3)
        a = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / denominator
        b = (x3 * x3 * (y1 - y2) + x2 * x2 * (y3 - y1) + x1 * x1 * (y2 - y3)) / denominator
        c = (x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / denominator

        return a, b, c


    def y_from_equation(self, x, a, b, c):
        y = a * x**2 + b * x + c
        return y


    def y_from_points(self, x_input, points):
        y = 1

        if x_input < points[0][0]:
            y = 0
        elif x_input < points[2][0]:
            a, b, c = Parabola.equation_from_points(points)
            y = Parabola.y_from_equation(x_input, a, b, c)

            if y > 1:
                y = 1

        return y


    def print_range(self, resolution = 1):
        print ('Points in graph:\t', end='')

        x = 0
        while x <= self.upper_limit + resolution:
            print(str(x) + ":" + str(round(self.y(x), 2)), end=', ')
            x += resolution


    def y(self, x):
        if x <= self.lower_limit and self.lower_limit is not None:
            return 0
        elif x >= self.upper_limit and self.upper_limit is not None:
            return 1
        else:
            return self.a * x**2 + self.b * x + self.c





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


# para1 = Parabola([[0, 0], [50, 40], [85, 100]])
# para1.print_range(10)