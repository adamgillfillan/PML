__author__ = 'Adam'
import unittest
import sys
import pml


class TestPML(unittest.TestCase):
    """
        Test the functionality of PML
    """
    def setUp(self):
#         self.filename = 'pml_sample.html'
#         self.f = open(self.filename, 'r')
#         self.pml = pml.PML(self.f)
#
        self.pml_provided_input = """<html>
<h1>Hello There</h1>
<p>
This is an example of a pml file
</p>
<h2>Good Bye</h2>
</html>"""
        self.pml_class = """<html>
<head>
    <title>This is a Title</title>
</head>
    <body>
        <h1>Hello There</h1>
        <p>
            This is an example of a pml file
        </p>
        Sample Text

        Billy barks!
        More Sample Text
    </body>
</html>"""
        self.pml_func = """<html>
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

        More Sample Text
    </body>
</html>"""
        self.pml_no_method = """<html>
<head>
    <title>This is a Title</title>
</head>
    <body>
        <h1>Hello There</h1>
        <p>
            This is an example of a pml file
        </p>
        Sample Text

        More Sample Text
    </body>
</html>"""
        self.pml_simple_statement = """<html>
<head>
    <title>This is a Title</title>
</head>
    <body>
        <h1>Hello There</h1>
        <p>
            This is an example of a pml file
        </p>
        Hello World
        Sample Text

        More Sample Text
    </body>
</html>"""

    def return_pml_object(self, filename):
        """Helper method that returns a PML object of a given filename"""

        f = open(filename, 'r')
        return pml.PML(f)

    def return_output_of_pml(self, pml_object):
        """Helper method that returns the value of sys.stdout of a given pml_object"""

        pml_object.print_file()
        return sys.stdout.getvalue().strip()

    def test_pml_print_with_provided_input(self):
        """Tests printing PML with the input provided in the project specification"""

        filename = 'test_PML_FILES/pml_provided_input.html'
        pml = self.return_pml_object(filename)
        output = self.return_output_of_pml(pml)
        self.assertEquals(self.pml_provided_input, output)

    def test_pml_print_with_class(self):
        """Tests printing PML when the python code has a class"""

        filename = 'test_PML_FILES/pml_class.html'
        pml = self.return_pml_object(filename)
        output = self.return_output_of_pml(pml)
        self.assertEquals(self.pml_class, output)

    def test_pml_print_with_func(self):
        """Tests printing PML when the python code has a function"""

        filename = 'test_PML_FILES/pml_func.html'
        pml = self.return_pml_object(filename)
        output = self.return_output_of_pml(pml)
        self.assertEquals(self.pml_func, output)

    def test_pml_print_no_methods(self):
        """Tests printing PML when the python code has no 'pml = ' statement to return anything"""

        filename = 'test_PML_FILES/pml_no_method.html'
        pml = self.return_pml_object(filename)
        output = self.return_output_of_pml(pml)
        self.assertEquals(self.pml_no_method, output)

    def test_pml_simple_statement(self):
        """Tests printing PML when the python code has only a simple statement, ex: "pml = Hello World" """

        filename = 'test_PML_FILES/pml_simple_statement.html'
        pml = self.return_pml_object(filename)
        output = self.return_output_of_pml(pml)
        self.assertEquals(self.pml_simple_statement, output)


if __name__ == "__main__":
    assert not hasattr(sys.stdout, "getvalue")
    unittest.main(module=__name__, buffer=True, exit=False)