import os


class HtmlGenerator:
    def __init__(self, configuration):
        self._configuration = configuration
        self._md_files = []
        self._image_files = []

    def run(self):
        self._walk_source_directory()
        self._transform_md_files()
        self._copy_image_files()

    def _walk_source_directory(self):
        for directory, _, files in os.walk(self._configuration.source_directory):
            for file in files:
                self._handle_file(os.path.join(directory, file))

    def _handle_file(self, file):
        if self._is_md_file(file):
            self._md_files.append(file)
        elif self._is_image_file(file):
            self._image_files.append(file)

    @staticmethod
    def _is_md_file(file):
        return file.endswith('.md')

    @staticmethod
    def _is_image_file(file):
        return (file.endswith('svg') or
                file.endswith('.jpg') or
                file.endswith('png'))

    def _transform_md_files(self):
        for file in self._md_files:
            print('md file:', file)

    def _copy_image_files(self):
        for file in self._image_files:
            print('image file:', file)
