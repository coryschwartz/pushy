# Copyright (c) 2008 Andrew Wilkins <axwalk@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import os, sys

thisdir = os.path.dirname(__file__)
sys.path.append(os.path.join(thisdir, ".."))

import pushy, unittest

class TestEval(unittest.TestCase):
    def setUp(self):
        self.conn = pushy.connect("local:")
    def tearDown(self):
        self.conn.close()

    def test_eval_expr(self):
        self.assertEquals(self.conn.eval("1+2"), 3)

    def test_throw(self):
        self.assertRaises(Exception, self.conn.eval, "1/0")

    def test_execute(self):
        locals_ = {}
        self.conn.execute("x = 123", locals=locals_)
        self.assertTrue("x" in locals_)
        self.assertEquals(123, locals_["x"])

if __name__ == "__main__":
    unittest.main()

