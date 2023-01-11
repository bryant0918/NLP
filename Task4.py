# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:26:00 2022

@author: bryant
"""

import hfst
from hfst import regex


tr1 = hfst.regex('foo:bar')
tr2 = hfst.regex('bar:baz')
tr1.compose(tr2)
print(tr1)


hfst.set_default_fst_type(hfst.ImplementationType.FOMA_TYPE)
tr = hfst.compile_lexc_file('finntreebank.lexc')
tr.invert()
tr.convert(hfst.ImplementationType.HFST_OL_TYPE)