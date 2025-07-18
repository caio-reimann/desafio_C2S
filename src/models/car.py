from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from src.data.database import Base


class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(primary_key=True)
    color: Mapped[str]
    model: Mapped[str]
    brand: Mapped[str]
    year: Mapped[int]
    fuel: Mapped[str]
    cylinders: Mapped[int]
    power: Mapped[float]
    gearshift: Mapped[str]
    weight: Mapped[int]
    seats: Mapped[int]
    abs: Mapped[bool]

    @property
    def one_line(self):
        return f" {self.brand} {self.model} -> color: {self.color} - brand: {self.brand} - year: {self.year} - fuel: {self.fuel} - cylinders: {self.cylinders} - power: {self.power} - gearshift: {self.gearshift} - weight: {self.weight} - seats: {self.seats} - abs: {self.abs}\n"
