# -*- coding: utf-8 -*-

"""
Created on 2015-10-26
:author: Joseph Rawson (joseph.rawson.works@gmail.com)
"""

from __future__ import absolute_import

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource

library = Library("kotti_compass", "static")

font_awesome = Resource(
    library,
    'font-awesome.css')

BASECOLORS = ['bisque', 'BlanchedAlmond',
              'DarkSeaGreen', 'LavenderBlush', 'cornsilk']

STYLES = ['bootstrap-custom', 'jqueryui', 'screen']

mystyles = dict()
#for style in STYLES:
#    mystyles[style] = dict()
#    for basecolor in BASECOLORS:
#        filename = '%s-%s.css' % (style, basecolor)
#        mystyles[style][basecolor] = Resource(library, filename)

mystyles['jqueryui'] = dict()
mystyles['bootstrap-custom'] = dict()
for basecolor in BASECOLORS:
    jqf = 'jqueryui-%s.css' % basecolor
    jq = Resource(library, jqf, depends=[font_awesome])
    mystyles['jqueryui'][basecolor] = jq

    bcf = 'bootstrap-custom-%s.css' % basecolor
    bc = Resource(library, bcf, depends=[jq])
    mystyles['bootstrap-custom'][basecolor] = bc



css = Resource(
    library,
    "styles.css",
    minified="styles.min.css")

js = Resource(
    library,
    "scripts.js",
    minified="scripts.min.js")

css_and_js = Group([css, js])

styles = mystyles
