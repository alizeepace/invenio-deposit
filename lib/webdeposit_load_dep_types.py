# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2012, 2013 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

import os
#from wtforms import Form
from invenio.config import CFG_PYLIBDIR
from invenio.pluginutils import PluginContainer

def plugin_builder(plugin_name, plugin_code):
    all = getattr(plugin_code, '__all__')
    for name in all:
        return getattr(plugin_code, name)

CFG_DOC_METADATA = PluginContainer(os.path.join(CFG_PYLIBDIR, \
                                                'invenio', \
                                                'webdeposit_dep_types', \
                                                '*_metadata.py'),
                                   plugin_builder=plugin_builder)

"""
Create a dict with groups, names and deposition types
in order to render the deposition type chooser page

e.g.
deposition_types = {"Articles & Preprints": \
                    [{"name": "Articles", "dep_type": "Article"}, \
                     {"name": "Preprints", "dep_type": "Preprint"}, \
                     {"name": "Theses", "dep_type": "Thesis"}]}
"""

deposition_types = {}
for dep in CFG_DOC_METADATA.itervalues():
    if not deposition_types.has_key(dep['group']):
        deposition_types[dep['group']] = []
    if dep["enabled"]:
        deposition_types[dep['group']].append({"name": dep['plural'], "dep_type": dep["dep_type"]})

__all__ = ['deposition_types']
