### osmstats is a python package for parsing OpenStreetMap XML data and to derive statistics out of it.

**Install**

To install from pypi

    pip install osmstats

To install from this source code

    pip install .

To install into a specific path

    pip install -t <path> .

----

**Where to Download OSM Data?**

1. Visit [this link](www.openstreetmap.org/export).
2. Manually select your area.
3. Export!

----

**Usage**

    from osmstats import OSMStats

    location = OSMStats('/path/to/map.osm')

    # collection of all contributors with count
    location.get_contributors()

    # total count of a feature
    location.get_count('amenity')

    # total count of a specific sub-feature
    location.get_count('amenity', 'pharmacy')

    # collection of all sub-feature of this feature with count
    location.get_feature('shop')

    # result of all get_feature() so far
    location.details

    # list of supported features
    from osmstats import OSM_FEATURES
    print(OSM_FEATURES.keys())

    # dump the data as json
    import json
    json.dumps(location.details)
