class Solution(object):
    def coverPoints(self, X, Y):
        def distance(p0, p1):
            """
            p0 --- point (x0, y0)
            p1 --- point (x1, y1)
            return manhattan distance betwen them
            """
            x0, y0 = p0[0], p0[1]
            x1, y1 = p1[0], p1[1]
            difX = abs(x0 - x1)
            difY = abs(y0 - y1)
            return max(difX, difY)
        def mk_points(X, Y):
            points = []
            for i in range(len(X)):
                points.append((X[i], Y[i]))
            return points
        points = mk_points(X, Y)
        steps = 0
        if not points == []:
            p_prev = points[0]
            points = points[1:]
            for p_cur in points:
                steps += distance(p_prev, p_cur)
                p_prev = p_cur
        return steps
