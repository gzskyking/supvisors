#!/usr/bin/python
#-*- coding: utf-8 -*-

# ======================================================================
# Copyright 2017 Julien LE CLEACH
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ======================================================================

import sys
import unittest

from supvisors.tests.base import DummySupervisor


class PluignTest(unittest.TestCase):
    """ Test case for the plugin module. """

    def test_faults(self):
        """ Test the values set at construction. """
        from supvisors.plugin import SupvisorsFaults
        fault = SupvisorsFaults()
        self.assertIsNotNone(fault)

    def test_update_views(self):
        """ Test the values set at construction. """
        from supvisors.plugin import update_views
        # check views before and after
        update_views()

    def test_make_rpc(self):
        """ Test the values set at construction. """
        from supvisors.plugin import make_supvisors_rpcinterface
        # check views before and after
        # TODO: fix test_initializer before
        # make_supvisors_rpcinterface(DummySupervisor())


def test_suite():
    return unittest.findTestCases(sys.modules[__name__])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
