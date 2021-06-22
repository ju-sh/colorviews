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
sys.path.insert(0, os.path.abspath('../..'))


# -- Theme information  -----------------------------------------------------

#import stanford_theme

#import better

# -- Project information -----------------------------------------------------

project = 'colorviews'
copyright = '2021, Julin S'
author = 'Julin S'

# The full version, including alpha/beta/rc tags
release = '0.1a2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    #'sphinx.ext.autosummary',
    #'sphinx.ext.viewcode',
    'sphinxcontrib.napoleon',
#    'sphinx_rtd_theme',
]
#autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '../src/colorviews/name/*',
    '../src/colorviews/utils/*',
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#html_theme = 'bizstyle'
#html_theme = 'classic'
#html_theme = 'sphinx_rtd_theme'
#html_theme = 'python_docs_theme'
#html_theme = 'furo'
html_theme = 'pydata_sphinx_theme'


#html_theme = 'stanford_theme'
#html_theme_path = [stanford_theme.get_html_theme_path()]

#html_theme = 'better'
#html_theme_path = [better.better_theme_path]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']
html_static_path = []
html_css_files = [
    'css/custom.css',
]

autodoc_member_order = 'bysource'

autodoc_default_options = {
    #'members': 'var1, var2',
    'member-order': 'bysource',
    #'special-members': '__init__',

    # don't generate doc for members without docstrings
    'undoc-members': False,

    'exclude-members': '__weakref__'
}

# Napoleon settings
napoleon_google_docstring = True
#napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
#napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True
