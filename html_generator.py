import os
import shutil
import pathlib
import md_transformer


class HtmlGenerator:
    def __init__(self, configuration):
        self._configuration = configuration
        self._md_files = []
        self._image_files = []
        self._template = self._read_template()
        print('source directory:', configuration.source_directory)
        print('destination directory:', configuration.destination_directory)

    def _read_template(self):
        return pathlib.Path('template.html').read_text(encoding='UTF-8')

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
            self._transform_md_file(file)

    def _transform_md_file(self, file):
        print('md file:', file)
        destination_directory = self._get_destination_directory(file)
        print('destination directory:', destination_directory)
        os.makedirs(destination_directory, mode=0o755, exist_ok=True)
        transformed_document = md_transformer.MdTransformer(file, destination_directory, self._template).run()
        raw_basename = os.path.splitext(os.path.basename(file))[0]
        destination_path = os.path.join(destination_directory, raw_basename + '.html')
        print('destination path:', destination_path)
        pathlib.Path(destination_path).write_text(transformed_document, encoding='UTF-8')

    def _get_destination_directory(self, file):
        if not os.path.isfile(file):
            raise ValueError('Not a file [' + file + ']')
        return self._get_destination_directory_path(os.path.dirname(file))

    def _copy_image_files(self):
        for file in self._image_files:
            self._copy_image_file(file)

    def _copy_image_file(self, file):
        destination_path = self._get_destination_file(file)
        print('Copying [', file, '] to [', destination_path, ']', sep='')
        shutil.copy(file, destination_path)

    def _get_destination_directory_path(self, file):
        destination_path = self._get_output_path(file)
        if os.path.exists(destination_path) and not os.path.isdir(destination_path):
            raise ValueError('Destination path is not a file: ' + destination_path)
        return destination_path

    def _get_destination_file(self, file):
        destination_path = self._get_output_path(file)
        if os.path.exists(destination_path) and not os.path.isfile(destination_path):
            raise ValueError('Destination path is not a file: ' + destination_path)
        return destination_path

    def _get_output_path(self, file):
        relative_path = _safe_relative_path(file, self._configuration.source_directory)
        destination_path = os.path.join(self._configuration.destination_directory, relative_path)
        return destination_path


def _safe_relative_path(path, base_path):
    result = os.path.relpath(path, base_path)
    if path != base_path and os.path.join(base_path, result) != path:
        raise ValueError('Path [' + path + '] is not a sub path of base path [' + base_path + '] - joined: [' + joined + ']')
    return result
