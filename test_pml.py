__author__ = 'Adam'
import unittest
import pml


class TestPML(unittest.TestCase):
    """
        Test the functionality of PML
    """
    def setUp(self):
        self.code = '''<html>
<head>
    <title>This is a Title</title>
</head>
    <body>
        <h1>Hello There</h1>
        <p>
            This is an example of a pml file
        </p>
        <pml>
            def f():
                return "<h2>Good Bye</h2>"

            pml = f()
        </pml>
        Sample Text

        <pml>
            pml = f()
        </pml>
    </body>
</html>'''
        self.filename = 'pml_sample.html'
        self.f = open(self.filename, 'r')
        self.pml = pml.PML(self.f)

    def test_pml_print(self):
        self.assertEquals(self.code, self.pml.print_file())
