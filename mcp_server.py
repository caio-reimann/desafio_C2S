import asyncio
from typing import Optional

from dotenv import load_dotenv

from src.schemas.car import CarFilterSchema
from mcp.server.fastmcp import FastMCP
from src.services.car import CarService
from src.tools.car import *
from src.data.database import session


load_dotenv()

mcp = FastMCP("cars")
car_service = CarService(session=session)

@mcp.tool()
def get_all_filtered_cars(
    color: Optional[str] = None,
    model: Optional[str] = None,
    brand: Optional[str] = None,
    year: Optional[int] = None,
    fuel: Optional[str] = None,
    cylinders: Optional[int] = None,
    power: Optional[float] = None,
    gearshift: Optional[str] = None,
    weight: Optional[int] = None,
    seats: Optional[int] = None,
    abs: Optional[bool] = None,
) -> str:
    """
    Show a list of cars based .
    Args:
        color: The car color
        model: The car model
        brand: The car brand
        year: The car fabrication year
        fuel: The car fuel
        cylinders: The car engine cylinders number
        power: The car power (CV)
        gearshift: The car gearshift type
        weight: The car weight
        seats: The car seats number
        abs: The break car abs system
    Returns:
        A text with all filtered cars by user parameter(s)
    """
    
    filters_dict = {}

    for key, value in locals().items():
        if value:
            filters_dict[key] = value 
    
    filters = CarFilterSchema(**filters_dict)
    cars = car_service.get_filter_by_attributes(filters=filters)
    result = ""

    for car in cars:
        result += f"{car.one_line}\n"

    return result


async def run():
    await mcp.run_stdio_async()


if __name__ == "__main__":
    asyncio.run(run())
