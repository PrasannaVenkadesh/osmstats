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

    def count_amenity(self, name):
        if name not in self.amenities.keys():
            return len(self.xml_data.xpath("//tag[@v='{}']".format(name)))
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
