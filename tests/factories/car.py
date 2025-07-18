from faker import Faker
from faker_vehicle import VehicleProvider

from src.models.car import Car


fake = Faker()
fake.add_provider(VehicleProvider)


class CarFactory:
    @staticmethod
    def create_car() -> Car:
        car: Car = Car(
            color=fake.safe_color_name(),
            model=fake.vehicle_model(),
            brand=fake.vehicle_make(),
            year=fake.random_int(min=1930, max=2025),
            fuel=fake.random_element(elements=["gasoline", "diesel", "electric"]),
            cylinders=fake.random_int(min=3, max=8),
            power=fake.pyfloat(min_value=40, max_value=300),
            gearshift=fake.random_element(elements=["manual", "automatic"]),
            weight=fake.random_int(min=910, max=3000),
            seats=fake.random_int(min=2, max=7),
            abs=fake.pybool(),
        )
        return car

