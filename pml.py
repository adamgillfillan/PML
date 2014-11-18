__author__ = 'Adam'
import re


class PML:
    """Create a PML file manager.
    A PML File is an HTML document with a twist. Python code is allowed in a PML document
    with a tag indicator <pml> ... </pml>.

    PML has file data, executes the python data, and parses it to provide an HTML readable document.

    This class performs the parsing of input and processing to return a valid output.
    """

    def __init__(self, file):
        self.code = file.read()
        self.blocks = []
        self.create_blocks()

    def print_file(self):
        return self.code

    def create_blocks(self):
        """Creates blocks of python code and returns them in a list."""
        pattern = r"<pml>(.*?)</pml>"
        p = re.compile(pattern, re.DOTALL)
        self.blocks = [x for x in re.findall(p, self.code)]

        # Substitute with a 1, 2, etc.
        # pattern = r"(\s*<pml>.*?</pml>)"
        # p = re.compile(pattern, re.DOTALL)
        # self.blocks = [x for x in re.findall(p, self.code)]


def main():
    # filename = raw_input("Please enter a filename")
    filename = 'pml_sample.html'
    f = open(filename, 'r')
    pml = PML(f)
    #print(pml.print_file())
    # for block in pml.blocks:
    #     print(block)
    print(pml.blocks)

if __name__ == "__main__":
    main()