"""

Test the academic package

"""

import argparse
import importlib.metadata
import logging
import sys
from argparse import RawTextHelpFormatter
import os

from academic import import_bibtex, cli
from academic.editFM import EditableFM

print("Import worked correctly")

# Assuming that we can use hard coded input values

input = "data/references.bib"
abs_input = os.path.abspath(input)

content_path = "content/publication_test/"

import_bibtex.import_bibtex(input, content_path, dry_run=False)
