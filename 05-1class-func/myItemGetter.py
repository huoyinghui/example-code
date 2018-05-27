from operator import itemgetter


class MyItemGetter(object):
    """
    Return a callable object that fetches the given item(s) from its operand.
    After f = itemgetter(2), the call f(r) returns r[2].
    After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
    """
    __slots__ = ('_items', '_call')

    def __init__(self, *items):
        if not items:
            items = []

        def func(obj):
            return [obj[i] for i in self._items]

        self._items = items
        self._call = func

    def __call__(self, obj):
        return self._call(obj)

    def __repr__(self):
        return '%s.%s(%s)' % (self.__class__.__module__,
                              self.__class__.__name__,
                              ', '.join(map(repr, self._items)))


metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def main():
    # for city in sorted(metro_areas, key=itemgetter(1)):
    #     print(city)
    # cc_name = itemgetter(1, 0, 2, 3)
    cc_name = MyItemGetter(1, 0, 2, 3)
    for city in metro_areas:
        print(cc_name(city))


if __name__ == '__main__':
    main()