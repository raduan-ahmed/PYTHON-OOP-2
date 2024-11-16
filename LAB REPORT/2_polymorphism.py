class Transport:
    def calculate_cost(self, weight, distance):
        raise NotImplementedError("This method should be overridden by subclasses")

class Truck(Transport):
    def calculate_cost(self, weight, distance):
        return weight * distance * 0.5  # Cost per kg per km for Truck

class Ship(Transport):
    def calculate_cost(self, weight, distance):
        return weight * distance * 0.3  # Cost per kg per km for Ship

class Plane(Transport):
    def calculate_cost(self, weight, distance):
        return weight * distance * 1.2  # Cost per kg per km for Plane

def calculate_delivery_costs(transports, weight, distance):
    costs = []
    for transport in transports:
        costs.append(transport.calculate_cost(weight, distance))
    return costs

# Example usage
transports = [Truck(), Ship(), Plane()]
weight = 20  # in kg
distance = 200  # in km
delivery_costs = calculate_delivery_costs(transports, weight, distance)
print(delivery_costs)
