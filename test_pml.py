__author__ = 'Adam'
import unittest
import pml


class TestPML(unittest.TestCase):
    """
        Test the functionality of PML
    """
    def setUp(self):
        self.filename = 'pml_sample.html'
        self.f = open(self.filename, 'r')
        self.pml = pml.PML(self.f)

        self.code_config = '''<html>
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
        self.code_func_1 = """<html>
<head>
    <title>This is a Title</title>
</head>
    <body>
        <h1>Hello There</h1>
        <p>
            This is an example of a pml file
        </p>
        <h2>Good Bye</h2>
        Sample Text



        <h2>Good Bye</h2>
    </body>
</html>"""

    def test_pml_config(self):
        """Tests that the initialization values of the file are matched. """
        self.assertEquals(self.code_config, self.pml.code)

    def test_pml_print_with_function(self):
        """Tests printing PML when the python code has a function"""
        self.assertEquals(self.code_func_1, self.pml.print_file())
