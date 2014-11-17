__author__ = 'Adam'
import unittest
import pml


class TestPML(unittest.TestCase):
    def setUp(self):
        self.code = '''
                <html>
                <head>
                    <title></title>
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
                    </body>
                </html>
                '''

