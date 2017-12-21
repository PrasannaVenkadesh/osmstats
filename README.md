## Python package for parsing OpenStreetMap XML data and to derive statistics out of it.

**Install**

To install from this source code

    pip install .

To install into a specific path

    pip install -t <path> .

To install from pypi

    pip install osmstats


----

**Usage**

    from osmstats import OSMStats

    location = OSMStats('map.osm')
    location.get_contributors()

    location.count_all_amenities()
    location.count_amentiy("pharmacy")
