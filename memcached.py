# install: sudo apt install memcached
# Для Python есть специальные инструменты по работе с memcached: # pip install pymemcache

from pymemcache.client.base import Client

client = Client(('localhost', 11211))
client.set('some_key', 'some_value')
result = client.get('some_key')
print(result)