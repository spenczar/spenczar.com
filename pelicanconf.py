#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Spencer Nelson'
SITENAME = u'spenczar'
SITEURL = 'http://spenczar.com'

TIMEZONE = 'America/Los_Angeles'

THEME = 'theme'

DEFAULT_LANG = u'en'

# Categories
DEFAULT_CATEGORY = u'blog'
CATEGORY_URL = 'posts/category/{slug}.html'
CATEGORY_SAVE_AS = 'posts/category/{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Menu settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False


# Dated archives
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

ARCHIVE_SAVE_AS = 'posts/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'


# Dates
DATE_FORMATS = {
    'verbose': '%a, %b %d %Y',
    'terse': '%Y-%m-%d',
}


# No author page
AUTHOR_SAVE_AS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

FILES_TO_COPY = (
    ('extra/CNAME', 'CNAME'),
)


STATIC_PATHS = ['css']

TEMPLATE_PAGES = {
    'archives.html': 'posts/index.html',
    'error.html': 'error.html',
}
def a(x, y):
    """ comment """
    return x + y * y

class HelloWorld():
    f = a
    hash(f)
    # little comment
    def __init__(self):
        print True


