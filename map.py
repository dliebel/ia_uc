class Map:
# """
#    self.stations: is a dictionary of dictionary with the format of
#             {station_id: {"name": name_value, "line": line_value, ...}

#     self.connections: is a dictionary of dictionary holding all the connection information with the format of
#             {
#                 station_1 : {first_connection_to_station_1: cost_1_1, second_connection_to_station_1: cost_1_2}
#                 station_2 : {first_connection_to_station_2: cost_2_1, second_connection_to_station_1: cost_2_2}
#                 ....
#             }
#     """
    def __init__(self):
        self.stations = {}
        self.connections = {}

    def add_station(self, id, name, line, x, y):
        self.stations[id] = {'name': name, 'line': int(line), 'x': x, 'y': y}

    def add_connection(self, connections):
        self.connections = connections

    def combine_dicts(self):
        for k, v in self.stations.items():
            v.update({'velocity': self.velocity[v['line']]})

    def add_velocity(self, velocity):
        self.velocity = {ix+1: v for ix, v in enumerate(velocity)}
        self.combine_dicts()