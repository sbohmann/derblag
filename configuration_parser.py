
import argparse


class ConfigurationParser(object):
    source_directory_key = 'source-directory'
    destination_directory_key = 'destination-directory'

    def run(self):
        parser = argparse.ArgumentParser(allow_abbrev=False)
        parser.add_argument('-' + self.source_directory_key, type=str, required=True)
        parser.add_argument('-' + self.destination_directory_key, type=str, required=True)
        result = parser.parse_args()
        print(type(result))
        print(result)
        return result
