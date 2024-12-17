# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path Setup -------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..')) # change this from . to ..


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'NBA_Draft_Analysis'
copyright = '2024, Josh Bergstrom, Morgan Kurth'
author = 'Josh Bergstrom, Morgan Kurth'
release = '0.0.1'



# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc", 
    "sphinx.ext.napoleon", 
    "myst_parser", 
    "sphinx.ext.viewcode", 
    "sphinx.ext.githubpages" 
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
source_suffix = ['.rst','.md']