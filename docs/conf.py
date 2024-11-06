# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'unc'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
]

source_suffix = ['.rst', '.md']

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'
