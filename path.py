class Path:

    def __init__(self, route):
        if type(route) is list:
            self.route = route
        else:
            self.route = [route]

        self.head = self.route[0]
        self.last = self.route[-1]
        if len(self.route) >= 2: self.penultimate = self.route[-2]
        # Real cost
        self.g = 0
        # Heuristic cost
        self.h = 0
        # Combination of the two
        self.f = 0

    def __eq__(self, other):
        if other is not None:
            return self.route == other.route

    def update_h(self, h):
        self.h = h

    def update_g(self, g):
        self.g += g

    def update_f(self):
        self.f = self.g + self.h

    def add_route(self, children):
        # Adding a new station to the route list
        self.route.append(children)
        self.penultimate = self.route[-2]
        self.last = self.route[-1]
 