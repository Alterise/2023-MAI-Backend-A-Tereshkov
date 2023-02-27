from cache import LRUCache

cache = LRUCache(5)

cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
print("Output:", cache.get('Jesse'))  # вернёт 'James'
cache.rem('Walter')
print("Output:", cache.get('Walter'))  # вернёт ''

cache.rem('Jesse')

cache.set('1', 'a')
cache.set('2', 'b')
cache.set('3', 'c')
cache.set('4', 'd')
cache.set('5', 'e')

print("Output:", cache.get('1'))

cache.set('6', 'f')

print("Output:", cache.get('1'))
print("Output:", cache.get('2'))
print("Output:", cache.get('3'))
print("Output:", cache.get('6'))
