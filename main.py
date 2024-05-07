import io

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    json_file = io.BytesIO(json)
    data = JSONParser().parse(json_file)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    return instance
