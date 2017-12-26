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
