PML
===
PML Project
A PML document is a standard HTML document with one additional feature. Any text between the starting <pml> tag and the ending </pml> tag is interpreted as Python source code.


Example input:
 
<html>
<h1>Hello There</h1>
<p>
This is an example of a pml file
</p>
<pml>
    def f():
        return "<h2>Good Bye</h2>"
 
    pml = f()
</pml>
</html>
 
 
Example output:
 
<html>
<h1>Hello There</h1>
<p>
This is an example of a pml file
</p>
<h2>Good Bye</h2>
</html>
