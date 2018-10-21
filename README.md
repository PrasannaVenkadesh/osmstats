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

1. Visit [this link](http://www.openstreetmap.org/export).
2. Manually select your area.
3. Export!

**Exporting OSM data options**
1. Overpass API - Download this bounding box from a mirror of the OpenStreetMap database
2. Planet OSM - Regularly updated copies of the complete OpenStreetMap database
Geofabrik Downloads
3. Regularly - updated extracts of continents, countries, and selected cities
4. [Other Sources](https://wiki.openstreetmap.org/wiki/Download) - Additional sources listed on the OpenStreetMap wiki 

![osm_export](https://github.com/manimaran96/osmstats/blob/master/osm_export.png)
----

**Usage**

    from osmstats import OSMStats

    location = OSMStats('/path/to/map.osm')

    # get lat, lon of this map data
    location.bounds

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
