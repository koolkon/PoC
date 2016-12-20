#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# The PoC-Library documentation build configuration file, created by
# sphinx-quickstart on Fri May  6 11:28:20 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

from subprocess import check_output

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../py'))
sys.path.insert(0, os.path.abspath('_extensions'))
sys.path.insert(0, os.path.abspath('_themes/sphinx_rtd_theme'))

import sphinx_rtd_theme

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.4.9'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
# Standard Sphinx extensions
	'sphinx.ext.autodoc',
	'sphinx.ext.extlinks',
	'sphinx.ext.intersphinx',
	'sphinx.ext.inheritance_diagram',
	'sphinx.ext.todo',
	# 'sphinx.ext.coverage',
	'sphinx.ext.graphviz',
	'sphinx.ext.mathjax',
	'sphinx.ext.ifconfig',
	'sphinx.ext.viewcode',
	# 'sphinx.ext.githubpages',
# SphinxContrib extensions
	# 'sphinxcontrib.actdiag',
	# 'sphinxcontrib.seqdiag',
	'sphinxcontrib.wavedrom',
	# 'sphinxcontrib.textstyle',
	# 'sphinxcontrib.spelling',
	'autoapi.sphinx',
	# 'changelog',
# local extensions (patched)
	'autoprogram',	             #'sphinxcontrib.autoprogram',
# local extensions
	'DocumentMember',
	'poc'
]

for tag in tags:
	print(tag)

# if (not (tags.has('PoCExternal') or tags.has('PoCInternal'))):
	# tags.add('PoCExternal')

from pathlib import Path
print("current path: {0!s}".format(Path.cwd())
pyInfrastructureDirectory = Path("docs/PyInfrastructure")
for path in pyInfrastructureDirectory.iterdir():
	print("  {0!s}".format(path))

autodoc_member_order = "bysource"

# Extract Python documentation and generate ReST files.
autoapi_modules = {
  'PoC':        {'output': "PyInfrastructure", 'template': "script"},
  'Base':       {'output': "PyInfrastructure"},
  'Compiler':   {'output': "PyInfrastructure"},
  'DataBase':   {'output': "PyInfrastructure"},
  'Parser':     {'output': "PyInfrastructure"},
  'Simulator':  {'output': "PyInfrastructure"},
  'ToolChain':  {'output': "PyInfrastructure"},
  'lib':        {'output': "PyInfrastructure"}
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates', '_themes']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'The PoC-Library'
copyright = '2007-2016 Technische Universitaet Dresden - Germany, Chair of VLSI-Design, Diagnostics and Architecture'
author = 'Patrick Lehmann, Thomas B. Preusser, Martin Zabel'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

def _IsUnderGitControl():
	return (check_output(["git", "rev-parse", "--is-inside-work-tree"], universal_newlines=True).strip() == "true")

def _LatestTagName():
	return check_output(["git", "describe", "--abbrev=0", "--tags"], universal_newlines=True).strip()

version = "1.1"     # The short X.Y version.
release = "1.1.1"   # The full version, including alpha/beta/rc tags.
try:
	if _IsUnderGitControl:
		latestTagName = _LatestTagName()[1:]		# remove prefix "v"
		versionParts =  latestTagName.split("-")[0].split(".")

		version = ".".join(versionParts[:2])
		release = latestTagName   # ".".join(versionParts[:3])
except:
	pass

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%d.%m.%Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
todo_link_only = True

# reST settings

rst_prolog = """\
.. |br| raw:: html

   <br />

"""

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [
	sphinx_rtd_theme.get_html_theme_path()
]

print(sphinx_rtd_theme.get_html_theme_path())

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#html_title = 'The PoC-Library v1.0.0'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
html_last_updated_fmt = "%b %d, %Y"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = True

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr', 'zh'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'ThePoC-Librarydoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
	'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ThePoC-Library.tex', 'The PoC-Library Documentation',
     'Patrick Lehmann, Thomas B. Preusser, Martin Zabel', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = True

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'thepoc-library', 'The PoC-Library Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ThePoC-Library', 'The PoC-Library Documentation',
     author, 'ThePoC-Library', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# ==============================================================================
# Sphinx.Ext.InterSphinx
# ==============================================================================
intersphinx_mapping = {
	'python': ('https://docs.python.org/3.5/', None),
	'ghdl':   ('http://ghdl.readthedocs.io/en/latest', None)
}

# ==============================================================================
# Sphinx.Ext.ExtLinks
# ==============================================================================
extlinks = {
	'pocissue': ('https://github.com/VLSI-EDA/PoC/issues/%s', 'issue #'),
	'pocpull':  ('https://github.com/VLSI-EDA/PoC/pull/%s', 'pull request #'),
	'pocsrc':   ('https://github.com/VLSI-EDA/PoC/blob/master/src/%s?ts=2', None),
	'poctb':    ('https://github.com/VLSI-EDA/PoC/blob/master/tb/%s?ts=2', None)
}


# ==============================================================================
# Sphinx.Ext.Graphviz
# ==============================================================================
graphviz_output_format = "svg"


# ==============================================================================
# Changelog
# ==============================================================================
# section names - optional
changelog_sections = ["general", "rendering", "tests"]

# tags to sort on inside of sections - also optional
changelog_inner_tag_sort = ["feature", "bug"]

# how to render changelog links - these are plain
# python string templates, ticket/pullreq/changeset number goes
# in "%s"
changelog_render_ticket = "http://bitbucket.org/myusername/myproject/issue/%s"
changelog_render_pullreq = "http://bitbucket.org/myusername/myproject/pullrequest/%s"
changelog_render_changeset = "http://bitbucket.org/myusername/myproject/changeset/%s"


# ==============================================================================
# SphinxContrib.Spelling
# ==============================================================================
# # String specifying the language, as understood by PyEnchant and enchant.
# # Defaults to en_US for US English.
# spelling_lang='en_US'
#
# # String specifying a file containing a list of words known to be spelled
# # correctly but that do not appear in the language dictionary selected by
# # spelling_lang. The file should contain one word per line.
# # Refer to the PyEnchant tutorial for details.
# #spelling_word_list_filename='spelling_wordlist.txt'
#
# # Boolean controlling whether suggestions for misspelled words are printed.
# # Defaults to False.
# spelling_show_suggestions=True
#
# # Boolean controlling whether words that look like package names from PyPI are
# # treated as spelled properly. When True, the current list of package names is
# # downloaded at the start of the build and used to extend the list of known
# # words in the dictionary.
# # Defaults to False.
# spelling_ignore_pypi_package_names=False
#
# # Boolean controlling whether words that follow the CamelCase conventions used
# # for page names in wikis should be treated as spelled properly.
# # Defaults to True.
# spelling_ignore_wiki_words=True
#
# # Boolean controlling treatment of words that appear in all capital letters, or
# # all capital letters followed by a lower case s. When True, acronyms are
# # assumed to be spelled properly.
# # Defaults to True.
# spelling_ignore_acronyms=True
#
# # Boolean controlling whether names built in to Python should be treated as
# # spelled properly.
# # Defaults to True.
# spelling_ignore_python_builtins=True
#
# # Boolean controlling whether words that are names of modules found on
# # sys.path are treated as spelled properly.
# # Defaults to True.
# spelling_ignore_importable_modules=True
#
# # List of filter classes to be added to the tokenizer that produces words to be
# # checked. The classes should be derived from enchant.tokenize.Filter. Refer to
# # the PyEnchant tutorial for examples.
# spelling_filters=[]


# ==============================================================================
# Custom changes
# ==============================================================================
def setup(app):
	app.add_stylesheet('css/custom.css')
	if tags.has('PoCInternal'):
		app.add_config_value('visibility', 'PoCInternal', True)
		print("="* 40)
	else:
		app.add_config_value('visibility', 'PoCExternal', True)
		print("-"* 40)
