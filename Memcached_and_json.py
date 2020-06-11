# TODO:Чтобы сделать из неё обратно словарь, надо сначала сделать decode, а затем json.loads.
#  Если мы исходно знаем, что у нас все данные будут представлять из себя json,
#  то можно задать сериализатор (функцию, которая будет преобразовывать объекты в понятный для сервиса вид) и
#  десериализатор (функцию, которая будет делать обратное преобразование из понятного для сервиса вида в объекты в Python). Например,
import json

from pymemcache.client.base import Client


def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2


def json_deserializer(key, value, flags):
    if flags == 1:
        return value.decode("utf-8")
    if flags == 2:
        return json.loads(value.decode("utf-8"))
    raise Exception("Unknown serialization format")


client = Client(('localhost', 11211), serializer=json_serializer,
                deserializer=json_deserializer)
client.set('key', {'a': 1, 'c': 2})
result = client.get('key')
print(result)
