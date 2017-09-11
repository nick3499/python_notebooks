COUNTRY_RANK = [
    (1, 'United States'),
    (2, 'China'),
    (3, 'Russia'),
    (4, 'Germany'),
    (5, 'United Kingdom')
]

# comprehensions
country_ranks = {country: code
                 for code, country in COUNTRY_RANK}
print(country_ranks)

top_ranks = {code: country.upper()
             for country, code in country_ranks.items()
             if code < 4}
print(top_ranks)

print(country_ranks.__contains__('United States')) # True
print(country_ranks.get('United States')) # 1
print(country_ranks['United States']) # 1
print(country_ranks.__iter__()) # <dict_keyiterator object at 0x7fa3aaf89d68>
print(len(country_ranks)) # 5
print(country_ranks.items())
# dict_items([('United States', 1), ('China', 2), ('Russia', 3), ('Germany', 4), ('United Kingdom', 5)])
print(country_ranks.keys())
# dict_keys(['United States', 'China', 'Russia', 'Germany', 'United Kingdom'])
print(country_ranks.values())
# dict_values([1, 2, 3, 4, 5])
# https://docs.python.org/3.6/library/functions.html#enumerate
