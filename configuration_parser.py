
import argparse


class ConfigurationParser(object):
    source_directory_key = 'source-directory'
    destination_directory_key = 'destination-directory'

    def __init__(self):
        self.parser = self.create_parser()

    def run(self):
        result = self.parser.parse_args()
        return result

    def create_parser(self):
        parser = argparse.ArgumentParser(allow_abbrev=False)
        parser.add_argument('-' + self.source_directory_key, type=str, required=True)
        parser.add_argument('-' + self.destination_directory_key, type=str, required=True)
        return parser
