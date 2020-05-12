# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'password-validator'
copyright = '2020, Tarun Batra'
author = 'Tarun Batra'

# The full version, including alpha/beta/rc tags
release = '0.2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        # Need the autodoc and autosummary packages to generate our docs.
        'sphinx.ext.autodoc',
        'sphinx.ext.intersphinx',
        'sphinx.ext.autosummary',
        # The Napoleon extension allows for nicer argument formatting.
        'sphinx.ext.doctest',
        'recommonmark',
        'sphinx_rtd_theme',
        'sphinx.ext.githubpages'
]
autoclass_content = "both"  # include both class docstring and __init__
autodoc_default_flags = [
        # Make sure that any autodoc declarations show the right members
        'members',
        'inherited-members',
        'show-inheritance',
]
autosummary_generate = True  # Make _autosummary files and include them


source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_logo = './_static/logo.png'
html_favicon = './_static/favicon.ico'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_copy_source = False
autodoc_mock_imports = ['mod']
