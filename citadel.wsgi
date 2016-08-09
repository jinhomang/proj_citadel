# -*- coding: utf-8 -*-

activate_this = '/Users/jinho/proj_citadel/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/Users/jinho/proj_citadel/')

from mytest import app as application 