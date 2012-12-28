#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#	Copyright 2012 Maxim.S.Barabash <maxim.s.barabash@gmail.com>
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.


from math import *


class Function():
	def __init__(self, func=None):
		self.setFunc(func)
		self.dic = {"sin": sin,
				"cos": cos,
				"tan": tan,
				"sqrt": sqrt,
				"pi": pi,
				"i": 0,
				"n": 0,
				"e": e,
				"abs": fabs,
				"exp": exp,
				}

	def setFunc(self, func):
			self.func = func.strip()

	def __call__(self, cfg={}):
		if self.func:
			dic = self.dic
			dic.update(cfg)
			ret = eval("lambda a:" + self.func, {"__builtins__": dic})
		else:
			ret = None
		return ret
