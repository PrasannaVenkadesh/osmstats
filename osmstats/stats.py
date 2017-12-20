#!/usr/bin/env python3.6

from lxml import etree

class OSMStats(object):

    def __init__(self, osm_file):
        self.osm_file = osm_file
        self.xml_data = etree.parse(self.osm_file)
        self.contributors = {}
        self.amenities = {}

    def get_contributors(self):
        if not self.contributors:
            for user in self.xml_data.xpath("//@user"):
                if user in self.contributors.keys():
                    self.contributors[user] += 1
                else:
                    self.contributors[user] = 1
        return self.contributors

    def count_amenities(self, name):
        if name not in self.amenities.keys():
            return len(self.xml_data.xpath(f"//tag[@v='{name}']"))
        else:
            return self.amenities[name]

    def count_all_amenities(self):
        if not self.amenities:
            for tag in self.xml_data.xpath("//tag[@k='amenity']"):
                if tag.attrib['v'] in self.amenities.keys():
                    self.amenities[tag.attrib['v']] += 1
                else:
                    self.amenities[tag.attrib['v']] = 1
        return self.amenities


if __name__ == "__main__":

    # load data from data directory
    pondicherry = OSMStats('../data/pondicherry.osm')

    # get total number of contributors
    p_contributors = pondicherry.get_contributors()
    total_contributors = len(p_contributors)
    print (f"Total Contributors: {total_contributors}")

    # count a particular amenity
    amenity_name = "cinema"
    print (pondicherry.count_amenities(amenity_name))

    # get all amenities count by amenity
    print (pondicherry.count_all_amenities())

    # sum of all amenities
    print (sum(pondicherry.amenities.values()))
