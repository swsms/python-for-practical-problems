import xmltodict

person_dict = xmltodict.parse("""<?xml version="1.0" ?>
<person>
  <name>John</name>
  <age>20</age>
</person>
""")

print(person_dict)  # OrderedDict([('person', OrderedDict([('name', 'John'), ('age', '20')]))])
print(person_dict['person']['name'])  # John
