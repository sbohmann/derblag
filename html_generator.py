import os


class HtmlGenerator:
    def __init__(self, configuration):
        self._configuration = configuration
        self._md_files = []
        self._image_files = []

    def run(self):
        self.walk_source_directory()
        self.transform_md_files()
        self.copy_image_files()

    def walk_source_directory(self):
        for directory, _, files in os.walk(self._configuration.source_directory):
            for file in files:
                self._handle_file(os.path.join(directory, file))

    def _handle_file(self, file):
        if self._is_md_file(file):
            self._md_files += file
        elif self._is_image_file(file):
            self._image_files += file

    @staticmethod
    def _is_md_file(file):
        return file.endswith('.md')

    @staticmethod
    def _is_image_file(file):
        return (file.endswith('svg') or
                file.endswith('.jpg') or
                file.endswith('png'))

    def transform_md_files(self):
        pass

    def copy_image_files(self):
        pass
