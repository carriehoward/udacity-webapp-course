CACHE = {}

#return True after setting the data
def set(key, value):
    CACHE[key] = value
    return True

#return the value for key
def get(key):
    return CACHE.get(key)

#delete key from the cache
def delete(key):
    if key in CACHE:
        del CACHE[key]

#clear the entire cache
def flush():
    CACHE.clear()

# QUIZ - implement gets() and cas() below
#return a tuple of (value, h), where h is hash of the value. a simple hash
#we can use here is hash(repr(val))

def gets(key):
    value = get(key)
    return value, hash(repr(value))

# set key = value and return True if cas_unique matches the hash of the value
# already in the cache. if cas_unique does not match the hash of the value in
# the cache, don't set anything and return False.
def cas(key, value, cas_unique):
    r = gets(key)
    if r:
        if cas_unique == r[1]:
            return set(key, value)
        else:
            return False

print set('x', 1)
#>>> True

print get('x')
#>>> 1
#
print get('y')
#>>> None
#
delete('x')
print get('x')
#>>> None
#
set('x', 2)
print gets('x')
#>>> 2, HASH
#
print cas('x', 3, 0)
#>>> False

print cas('x', 4, 6400019251)
#>>> True

print get('x')
#>>> 4
