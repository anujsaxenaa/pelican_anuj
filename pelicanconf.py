#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Anuj'
SITENAME = u'anujsaxenaa'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
THEME = "/Users/Anuj/pelican-themes/waterspill-en"
# Blogroll
LINKS =  (('Linkedin', 'https://www.linkedin.com/profile/view?id=115969517&trk=nav_responsive_tab_profile'),
          ('Github', 'https://github.com/anujsaxenaa/'),
          ('Kaggle', 'http://www.kaggle.com/users/117756/anuj-saxena/'),
          ('You can modify those links in your config file', '#'),)
STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
'extra/CNAME': {'path': 'CNAME'}
}

# Social widget

SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
