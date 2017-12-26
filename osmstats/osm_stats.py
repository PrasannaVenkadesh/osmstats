from lxml import etree
from .osm_features import OSM_FEATURES

class OSMStats(object):

    def __init__(self, osm_file):
        self.osm_file = osm_file
        self.xml_data = etree.parse(self.osm_file)
        self.bounds = self.xml_data.xpath("//bounds")[0].attrib
        self.contributors = {}
        self.details = {}

    def get_contributors(self):
        '''Returns all contributors of this map,
           with their contribution count.

           :return: contributors with contribution count
           :rtype: dict
        '''
        if not self.contributors:
            for user in self.xml_data.xpath("//@user"):
                if user in self.contributors.keys():
                    self.contributors[user] += 1
                else:
                    self.contributors[user] = 1
        return self.contributors

    def get_count(self, feature_name, feature_type=None):
        '''Counts the total number of feature (or) a
           specific type of the feature supplied.

           :param feature_name: name of the OSM feature
           :param feature_type: name of the OSM sub-feature

           :example: get_count('amenity', 'pharmacy')
           :return: total number of feature (or) sub-feature
           :rtype: int
        '''
        if feature_type:
            s_query = "//tag[@k='{}' and @v='{}']".format(feature_name, feature_type)
        else:
            s_query = "//tag[@k='{}']".format(feature_name)
        return len(self.xml_data.xpath(s_query))

    def get_feature(self, feature_name):
        '''Returns sub-features of the feature with
           individual count for each sub-features.

           This method also incrementally builds the
           self.details dictionary with new feature names
           if not already present.

           :param feature_name: name of the OSM feature

           :example: get_feature('shops')
           :return: sub-features and it's count for the feature
           :rtype: dict
        '''
        if feature_name not in OSM_FEATURES:
            return "Unknown feature %s" %feature_name

        if feature_name not in self.details:
            self.details[feature_name] = {}
            for tag in self.xml_data.xpath("//tag[@k='%s']" %feature_name):
                if tag.attrib['v'] in self.details[feature_name]:
                    self.details[feature_name][tag.attrib['v']] += 1
                else:
                    self.details[feature_name][tag.attrib['v']] = 1
        return self.details[feature_name]
