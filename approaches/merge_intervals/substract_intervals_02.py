class RangeSet:
    def __init__(self, elements):
        self.ranges = list(elements)

    def __iter__(self):
        return iter(self.ranges)

    def __repr__(self):
        return 'RangeSet: %r' % self.ranges

    def has(self, time_range):
        for date, i in enumerate(self.ranges):
            if i[0] <= time_range[0] and i[1] >= time_range[1]:
                return date, i
        raise ValueError('Invalid range or overlapping range')

    def minus(self, time_range):
        date, (x, y) = self.has(time_range)
        out = []
        if x < time_range[0]:
            out.append((x, time_range[0] - 1))
        if y > time_range[1]:
            out.append((time_range[1] + 1, y))
        self.ranges[date:date + 1] = out

    def __sub__(self, r):
        r1 = RangeSet(self)
        for i in r: r1.minus(i)
        return r1

    def sub(self, r):  # inplace subtraction
        for i in r:
            self.minus(i)


if __name__ == '__main__':
    r1 = RangeSet([(1, 100), ])
    r2 = RangeSet([(30, 40), (35, 80)])
    r1.sub(r2)
    print(r1)
