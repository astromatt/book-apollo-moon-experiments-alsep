project = 'ALSEP'
author = 'Mateusz Matt Harasymczuk'
email = 'matt@astronaut.center'

# html_theme = 'sphinx_rtd_theme'
html_theme = 'thesis'
pygments_style = 'borland'

todo_emit_warnings = False
todo_include_todos = True

extensions = [
    'sphinxcontrib.bibtex',
    'sphinx.ext.imgmath',
    # 'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
]

language = 'pl'
numfig_format = {
    'section': 'Rozdz. %s.',
    'figure': 'Ryc. %s.',
    'table': 'Tabela %s.',
    'code-block': 'Listing %s.',
}

exclude_patterns = [
    'README.rst',
    'LICENSE.rst',
    '_not_used',
]

# article - for articles in scientific journals, presentations, short reports, program documentation, invitations, ...
# proc - a class for proceedings based on the article class.
# minimal - is as small as it can get. It only sets a page size and a base font. It is mainly used for debugging purposes.
# report - for longer reports containing several chapters, small books, thesis, ...
# book - for real books
# slides - for slides. The class uses big sans serif letters.
# memoir - for changing sensibly the output of the document. It is based on the book class, but you can create any kind of document with it (1)
# letter - For writing letters.
# beamer - For writing presentations (see LaTeX/Presentations).
latex_documentclass = 'report'

html_context = {
    'university': 'Akademia Górniczo Hutnicza',
    'faculty': 'Wydział Geologii, Geofizyki i Ochrony Środowiska',
    'thesis': 'Praca zaliczeniowa <br> Geofizyka Stosowana',
    'thesis_title': 'Badania geofizyczne w trakcie załogowej eksploracji Księżyca w ramach programu Apollo.',
    'thesis_author': 'Mateusz Matt Harasymczuk',
    'thesis_supervisor': 'Prof. dr hab. inż. Kaja Pietsch',
    'city': 'Kraków',
    'year': '2019',
}

# -- Standard book config -----------------------------------------------------

import os
import re
import subprocess
import sys
from datetime import date

needs_sphinx = '2.0'

exclude_patterns += [
    '.*',
    'venv*',
    'virtualenv*',
    '_build',
    '_extensions',
    '_img',
    '_slides',
    '_static',
    '_themes',
    '_tmp',
    '*/contrib/*',
    '*/solution/*',
    '*/solutions/*',
    '**.ipynb_checkpoints',
    'README.rst',
    'TODO.rst',
    'Thumbs.db',
    '.DS_Store',
]

templates_path = ['_templates']
highlight_language = 'python3'
sys.path.insert(0, os.path.abspath('_extensions'))


# 0 - sequence number of image in whole document
# 1 - sequence number of image in header level 1 (only if :numbered: option is present at toctree directive)
# 2 - sequence number of image in header level 2
#       will use x.1, x.2, … if located directly under a header level 1,
#       will use 1, 2, … if at the document level
numfig_secnum_depth = 0
numfig = True
smartquotes = False

project_slug = re.sub(r'[\W]+', '', project)
sha1 = subprocess.run('git log -1 --format="%h"', stdout=subprocess.PIPE, shell=True, encoding='utf-8').stdout.strip()
year = date.today().year
today = date.today().strftime('%Y-%m-%d')

version = f'#{sha1}, {today}'
release = f'#{sha1}, {today}'
copyright = f'{year}, {author} <{email}>'

html_show_sphinx = False
html_use_smartypants = False
html_search_language = language
html_theme_path = ['_themes']
html_secnumber_suffix = '. '

if os.path.isdir('_static'):
    html_static_path = ['_static']
    html_context.update({
        'css_files': [
            '_static/screen.css',
            '_static/print.css',
        ],
        'script_files': [
            '_static/jquery.min.js',
            '_static/onload.js',
        ],
    })

latex_documents = [('index', f'{project_slug}.tex', project, author, latex_documentclass)]
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'figure_align': 'htbp',

    # Fix for: LaTeX Backend Fails with Citations In Figure Captions
    'preamble': r"""
        \usepackage{etoolbox}
        \AtBeginEnvironment{figure}{\renewcommand{\phantomsection}{}}
    """
}