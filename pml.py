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
        self.file = file
        self.code = file.read()
        # self.formatted_code = self.format()
        self.blocks = self.create_blocks()
        self.sub_blocks = self.format()

    def print_file(self):
        return self.code

    def format(self):
        """Formats self.blocks by removing unnecessary indents in the code."""
        sub_blocks = []
        for block in self.blocks:
            sub_blocks.append(block.split('\n'))
        new_blocks = []
        for sub_block in sub_blocks:
            count = 0
            for element in sub_block[1:]:
                if count == 0:
                    new_blocks.append(element.lstrip())
                    value = len(element) - len(element.lstrip())
                    count = 1
                else:
                    new_value = len(element) - len(element.lstrip())
                    value_2 = new_value - value
                    new_blocks.append(element.replace(" "*new_value, " "*value_2))
        new_blocks.insert(0, "")
        # return "\n".join(new_blocks)
        return new_blocks

    def create_blocks(self):
        """Creates blocks of python code and returns them in a list."""
        pattern = r"<pml>(.*?)</pml>"
        p = re.compile(pattern, re.DOTALL)
        # TODO: Replace self.code with self.formatted_code
        blocks = [x for x in re.findall(p, self.code)]
        return blocks

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
    #for block in pml.blocks:
    #    print(block)

    # TODO: Uncomment this
    print(pml.blocks)
    print(pml.sub_blocks)
    # for block in pml.blocks:
    #     exec block

    #print pml.code
   # print pml.formatted_code

if __name__ == "__main__":
    main()