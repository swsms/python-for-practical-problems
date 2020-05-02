import xmltodict

person_dict = xmltodict.parse("""<?xml version="1.0" ?>
<person>
  <name>John</name>
  <age>20</age>
</person>
""")

# OrderedDict([('person', OrderedDict([('name', 'John'), ('age', '20')]))])
print(person_dict)
print(person_dict['person']['name'])  # John
