__author__ = 'Adam'
import re

# TODO: Write Test Cases
# TODO: exec code
# TODO: Write Algorithm to replace <pml> .. <pml> blocks with the exec code
# While looping through final code set, line by line, if it reaches a "STOPHERE", then exec code


class PML:
    """Create a PML file manager.
    A PML File is an HTML document with a twist. Python code is allowed in a PML document
    with a tag indicator <pml> ... </pml>.

    PML has file data, executes the python data, and parses it to provide an HTML readable document.

    This class performs the parsing of input and processing to return a valid output.
    """

    def __init__(self, filename):
        self.filename = filename
        self.code = filename.read()
        # self.formatted_code = self.format()
        self.blocks = self.create_blocks()
        self.sub_blocks = self.format()
        self.code_transition = self.replace_text()
        self.blocks_transition = self.split_code_transition()

    def format(self):
        """Formats blocks of python code by removing unnecessary indents in the code."""
        blocks = []
        # We need a new array that is composed of each line of the blocks array
        for block in self.blocks:
            blocks.append(block.split('\n'))

        # We need a multi-dimensional array to represent each occurrence of a <pml> ... </pml> code block
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
        """Takes a formatted list of python blocks and searches for the string 'pml = '.
        Replace this with 'print '. This is needed for the 'exec' command used later.
        """
        new_blocks = [[], []]
        i = 0
        for sub_block in blocks:
            for element in sub_block:
                new_blocks[i].append(element.replace("pml = ", "print "))
            i += 1

        # a = "\n".join(new_blocks[0])
        # b = "\n".join(new_blocks[1])
        # exec a
        # exec b

        return new_blocks

    def create_blocks(self):
        """Creates blocks of python code and returns them in a list."""
        pattern = r"<pml>(.*?)</pml>"
        p = re.compile(pattern, re.DOTALL)
        # TODO: Replace self.code with self.formatted_code
        blocks = [x for x in re.findall(p, self.code)]
        return blocks

    def replace_text(self):
        """Replaces all occurrences of a pml code block with the identifier value, REPLACE_ME
        This is not the best solution. Given time limitations, this will have to do for now.
        """

        # Substitute with string "REPLACE_ME"
        pattern = r"\s*(<pml>.*?</pml>)"
        p = re.compile(pattern, re.DOTALL)
        new_string = re.sub(p, "\nREPLACE_ME", self.code)
        return new_string

    def split_code_transition(self):
        """Split code_transition by line."""

        return self.code_transition.split("\n")

    def print_file(self):
        """Prints the formatted PML file"""
        return self.code


def main():
    # filename = raw_input("Please enter a filename")
    filename = 'pml_sample.html'
    f = open(filename, 'r')
    pml = PML(f)
    #print(pml.print_file())
    #for block in pml.blocks:
    #    print(block)

    # TODO: Uncomment this
   # print(pml.blocks)
    #print(pml.sub_blocks)
    #print(pml.code_transition)
    #print(pml.blocks_transition)
    # for block in pml.blocks:
    #     exec block
    for block in pml.blocks_transition:
        print(block)

    #print pml.code
   # print pml.formatted_code

if __name__ == "__main__":
    main()