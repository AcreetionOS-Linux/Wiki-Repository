# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'AcreetionOS'
copyright = '2025, AcreetionOS Project'
author = 'AcreetionOS Team'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_favicon'
    'sphinx.ext.napoleon',      # For Google/NumPy style docstrings
    'sphinx.ext.viewcode',      # Add links to highlighted source code
    'sphinx.ext.githubpages',   # Creates .nojekyll for GitHub Pages
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'  # Use ReadTheDocs theme

html_static_path = ['_static']

# -- Options for autodoc -----------------------------------------------------

autodoc_member_order = 'bysource'
autoclass_content = 'both'

# Force Dark

html_theme_options = {
      "color_scheme": "dark"
}

html_static_path = ['_static']
html_favicon = 'acreetionos.ico'
