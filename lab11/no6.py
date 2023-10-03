from abc import ABC, abstractmethod

class Transportation:
    def __init__(self, start_place, end_place, distance):
        self.start_place = start_place
        self.end_place = end_place
        self.distance = distance
        pass

    @abstractmethod
    def find_cost(self):
        pass

class Walk(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)
    def find_cost(self):
        return 0

class Taxi(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)
    def find_cost(self):
        return 40*self.distance

class Train(Transportation):
    def __init__(self, start_place, end_place, distance, station):
        super().__init__(start_place, end_place, distance)
        self.station = station
    def find_cost(self):
        return 40*self.station

p1 = Walk("KMITL", "Lawson", 0.6)
p2 = Taxi("Lawson", "Ladkrabang", 5)
p3 = Train("Lawson", "Ladkrabang", 5, 4)

print(p1.find_cost())
print(p2.find_cost())
print(p3.find_cost())