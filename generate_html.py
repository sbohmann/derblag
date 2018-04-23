#!/usr/bin/env python3

import configuration_parser
import html_generator

configuration = configuration_parser.ConfigurationParser().run()

html_generator.HtmlGenerator(configuration).run()
