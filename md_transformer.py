import pathlib
import markdown2

class MdTransformer:
    def __init__(self, source_file, destination_directory, template):
        self._source_file = source_file
        self._destination_directory = destination_directory
        self._template = template

    def run(self):
        markdown = markdown2.Markdown()
        md = pathlib.Path(self._source_file).read_text(encoding='UTF-8')
        return self._create_html_file(markdown.convert(md))

    def _create_html_file(self, converted_content):
        return self._template.replace('@_content;', converted_content)
