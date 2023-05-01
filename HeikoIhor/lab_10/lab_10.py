class IsNotTitleException(Exception):
 pass

cities = ['Zurich', 'work', 'Frankfurt', 'Venice']
try:
 for city in cities:
    if city.title() != city:
        raise IsNotTitleException(city)
except IsNotTitleException as exc:
    print(exc)
