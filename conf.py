# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add paths here if needed
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate UHC Account'
copyright = '2025, UnitedHealthcare Guide'
author = 'UHC Help Center (Unofficial)'

# Release version
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions
extensions = []

# Allow raw HTML inside .rst files (for buttons)
raw_enabled = True

# Templates and excluded files
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (optional)
# html_theme = 'sphinx_rtd_theme'

# SEO-friendly titles
html_title = "Activate UHC Account at activate.uhc.com – Step-by-Step Guide"
html_short_title = "UHC Activation Guide"

# Favicon (place file in root or _static)
html_favicon = 'favicon.ico'

# Hide source link
html_show_sourcelink = False

# Allow raw / unsafe HTML (required for CTA buttons)
html_allow_unsafe = True

# Theme options
html_theme_options = {
    'show_powered_by': False,
}

# Static files (optional)
# html_static_path = ['_static']
