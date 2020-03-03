"""Task 7 module."""
import random


class Item:
    """Class for items representation."""

    def __init__(self, name: str, price: float) -> None:
        """An instance of class (item) with name and price attributes
        initialization.

        >>> item1 = Item('book', 110)
        >>> item1.name
        'book'
        >>> item1.price
        110
        >>> item2 = Item('chupachups', 44)
        >>> item2.name
        'chupachups'
        >>> item2.price
        44
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        r"""Returns a user-friendly string representation of an instance of the
        class (item).

        >>> item1 = Item('book', 110)
        >>> print(item1)
        Name: book
        Price: 110
        >>> item2 = Item('chupachups', 44)
        >>> print(item2)
        Name: chupachups
        Price: 44
        """
        return f"Name: {self.name}\nPrice: {self.price}"


class Vehicle:
    """Class for vehicle representation."""

    def __init__(self, vehicleNo: int, isAvailable=True) -> None:
        """An instance of class (vehicle) with vehicleNo and isAvailable
        attributes initialization.

        >>> vehicle1 = Vehicle(1)
        >>> vehicle1.vehicleNo
        1
        >>> vehicle1.isAvailable
        True
        """
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable


class Location:
    """Class for location representation."""

    def __init__(self, city: str, postoffice: int) -> None:
        """An instance of class (location) with city and postoffice attributes
        initialization.

        >>> location1 = Location('Lviv', 53)
        >>> location1.city
        'Lviv'
        >>> location1.postoffice
        53
        """
        self.city = city
        self.postoffice = postoffice


class Order:
    """Class for order representation."""

    def __init__(self, user_name: str, city: str, postoffice: int,
                 items: list) -> None:
        """An instance of class (order) with user_name, city, postoffice  and
        items attributes initialization.

        The orderId is assigned randomly, so doctests can only be written
        using seed.
        """
        self.orderId = random.randint(100000000, 999999999)
        print(f"Your order number is {self.orderId}.")
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.vehicle = None

    def __str__(self) -> str:
        """Returns a user-friendly string representation of an instance of the
        class (order)."""
        return f"Order ID: {self.orderId}\nUsername: {self.user_name}\n" \
               f"City: {self.location.city}\n" \
               f"Post Office: {self.location.postoffice}\n" \
               f"Items: {', '.join(item.name for item in self.items)}\n" \
               f"Vehicle: {self.vehicle}"

    def calculateAmount(self) -> float:
        """Return the total price of the order."""
        return sum(item.price for item in self.items)

    def assignVehicle(self, vehicle: int) -> None:
        """Assigns vehicle to the order."""
        self.vehicle = vehicle


class LogisticSystem:
    """Class for logistic system representation."""

    def __init__(self, vehicles: list) -> None:
        """An instance of class (logistic system) with vehicles attribute
        initialization."""
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order) -> None:
        """Places order."""
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                self.orders.append(order)
                order.assignVehicle(vehicle.vehicleNo)
                vehicle.isAvailable = False
                break

        print("There is no available vehicle to deliver an order.")

    def trackOrder(self, orderId: int) -> str:
        """Returns information about order given by its ID."""
        for order in self.orders:
            if order.orderId == orderId:
                destination = order.location.city
                total_price = order.calculateAmount()
                return f"Your order #{orderId} is sent to {destination}. " \
                       f"Total price: {total_price} UAH. "

        print("No such order.")


if __name__ == '__main__':
    import doctest

    doctest.testmod()
