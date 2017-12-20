#!/usr/bin/env python3.6

from lxml import etree

class OSMStats(object):
    
    def __init__(self, osm_file):
        self.osm_file = osm_file
        self.xml_data = None
        self.contributors = {}
        self.amenities = {}
        

    def get_contributors(self):
        self.xml_data = etree.parse(self.osm_file)
        root = self.xml_data.getroot()
        for element in root:
            if 'user' in element.keys():
                if element.attrib['user'] in self.contributors.keys():
                    self.contributors[element.attrib['user']] += 1
                else:
                    self.contributors[element.attrib['user']] = 1
        return self.contributors

    def count_amenities(self, name):
        self.amenities[name] = len(self.xml_data.xpath(f"//tag[@v='{name}']"))
        return self.amenities[name]


if __name__ == "__main__":

    # load data from data directory
    pondicherry = OSMStats('../data/pondicherry.osm')

    # get total number of contributors
    p_contributors = pondicherry.get_contributors()
    total_contributors = len(p_contributors)
    print (f"Total Contributors: {total_contributors}")

    # get total number of amenitiee
    amenity_name = "cinema"
    print (f"{amenity_name}: ", pondicherry.count_amenities(amenity_name))
