
class HtmlGenerator:
    def __init__(self, configuration):
        self.configuration = configuration

    def run(self):
        print(self.configuration.source_directory)
        print(self.configuration.destination_directory)
