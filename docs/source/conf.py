# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django

# Allow Sphinx to import Django project modules from the project root.
sys.path.insert(0, os.path.abspath("../.."))

# Configure Django settings before autodoc imports project modules.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_project.settings")
django.setup()

# -- Project information -----------------------------------------------------

project = "News Management System"
copyright = "2026, Tammie Davis"
author = "Tammie Davis"
release = "1.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = "alabaster"
html_static_path = ["_static"]