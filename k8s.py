#!/usr/bin/env python3

import os
from jinja2 import Template

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('k8s'))

YAML_PATH = os.environ['YAML_PATH']
template = env.get_template(YAML_PATH)
print(template.render(**os.environ))

