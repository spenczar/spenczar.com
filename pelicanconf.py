#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Spencer Nelson'
SITENAME = u'spenczar'
SITEURL = 'http://spenczar.com'

TIMEZONE = 'America/Los_Angeles'

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

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'


# Dates
DATE_FORMATS = {
    'verbose': '%a, %d %b %Y',
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
