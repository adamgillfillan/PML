__author__ = 'Adam'


class PML:
    """
        A PML File is an HTML document with a twist. Python code is allowed in a PML document
        with a tag indicator <pml> ... </pml>.

        PML has this file data, executes the python data, and parses it to provide an HTML readable document.
    """

    def __init__(self, file):
        self.file = file
        self.code = file.read()

    def print_file(self):
        return self.code


def main():
    # filename = raw_input("Please enter a filename")
    filename = 'pml_sample.html'
    f = open(filename, 'r')
    pml = PML(f)
    print(pml.print_file())


if __name__ == "__main__":
    main()