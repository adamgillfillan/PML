__author__ = 'Adam'
import re
import sys


class PML:
    """A PML file manager.

    A PML File is an HTML document with a twist. Python code is allowed in a PML document
    with a tag indicator <pml> ... </pml>.
    PML has file data, executes the python data, and parses it to provide an HTML readable document.

    This class performs the parsing of an input PML file and the processing to return a valid HTML output.

    """
    def __init__(self, filename):
        self.filename = filename
        self.code = filename.read()
        self.blocks = self.create_blocks()
        self.sub_blocks = self.format()
        self.code_transition = self.replace_text()
        self.blocks_transition = self.code_transition.split("\n")

    def format(self):
        """Formats blocks of python code by removing unnecessary indents in the code."""
        blocks = []
        # We need a new array that is composed of each line of the blocks array
        for block in self.blocks:
            blocks.append(block.split('\n'))

        # We need a list of lists of <pml> ... </pml> code blocks
        new_blocks = [[], []]
        i = 0

        # For each sub_block, append the formatted line of code to new_blocks
        for sub_block in blocks:
            on_first_code_element = True
            # Assume that python code always begins on a new line after the <pml> tag. Therefore, skip the first element
            for element in sub_block[1:]:
                if on_first_code_element:
                    new_blocks[i].append(element.lstrip())
                    # This value is the number of white spaces before the python code.
                    value = len(element) - len(element.lstrip())
                    on_first_code_element = False
                else:
                    # This value is the number of white spaces before the python code.
                    new_value = len(element) - len(element.lstrip())
                    # Subtract the value from the first element from the new_value to determine how many white spaces
                    # we need to remove. Then, replace the old number of white spaces with this difference.
                    difference = new_value - value
                    new_blocks[i].append(element.replace(" "*new_value, " "*difference))

            i += 1
        new_blocks[0].insert(0, "")

        formatted_blocks = self.pml_replace(new_blocks)

        return formatted_blocks

    @staticmethod
    def pml_replace(blocks):
        """Parses a list of lists and returns a list of lists of blocks of python code.

        Takes a formatted list of lists of python blocks and searches for the string 'pml = '.
        Replaces this with 'print '. This is needed for the 'exec' command used later.

        """
        new_blocks = [[], []]
        i = 0
        for sub_block in blocks:
            for element in sub_block:
                new_blocks[i].append(element.replace("pml = ", "print "))
            i += 1

        return new_blocks

    def create_blocks(self):
        """Return a list of blocks of python code."""
        pattern = r"<pml>(.*?)</pml>"
        p = re.compile(pattern, re.DOTALL)
        blocks = [x for x in re.findall(p, self.code)]

        return blocks

    def replace_text(self):
        """Replace the identifier value, REPLACE_ME, in a string of a pml file and return the new string"""
        pattern = r"(<pml>.*?</pml>)"
        p = re.compile(pattern, re.DOTALL)
        new_string = re.sub(p, "REPLACE_ME", self.code)

        return new_string

    def print_file(self):
        """Prints the formatted PML file."""
        count = 0
        for block in self.blocks_transition:
            if "REPLACE_ME" in block:
                # the length of the leading whitespace
                leading_whitespace = len(block) - len(block.lstrip())-1
                a = "\n".join([str(x) for x in self.sub_blocks[count]])
                if "print" in a:
                    try:
                        # value will be less than 0 when the indent should be flushed to the left.
                        if leading_whitespace < 0:
                            exec a
                        else:
                            print " "*leading_whitespace,
                            exec a
                    except IndentationError, e:
                        print "ERROR:", e
                    except SyntaxError, e:
                        print "ERROR:", e
                else:
                    try:
                        exec a
                    except IndentationError, e:
                        print "ERROR:", e
                    except SyntaxError, e:
                        print "ERROR:", e

                count += 1
            else:
                print(block)


if __name__ == "__main__":
    # filename = raw_input("Please enter a filename")
    # filename = 'test_PML_files/pml_bad_python_indent.html'
    args = [arg for arg in sys.argv]
    f = open(args[1], 'r')
    pml = PML(f)
    pml.print_file()