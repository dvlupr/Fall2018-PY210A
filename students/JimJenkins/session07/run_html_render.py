#!/usr/bin/env python3

from io import StringIO

# importing the html_rendering code with a short name for easy typing.
import html_render as hr


# writing the file out:
def render_page(page, filename, indent=None):
    """
    render the tree of elements

    This uses StringIO to render to memory, then dump to console and
    write to file -- very handy!
    """

    f = StringIO()
    if indent is None:
        page.render(f)
    else:
        page.render(f, indent)

    print(f.getvalue())
    with open(filename, 'w') as outfile:
        outfile.write(f.getvalue())


page = hr.Element()

page.append("Here is a paragraph of text -- there could be more of them, "
            "but this is enough  to show that we can do some text")

page.append("And here is another piece of text -- you should be able to add any number")

render_page(page, "test_html_output1.html")


page = hr.Html()

body = hr.Body()

body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough  to show that we can do some text"))

body.append(hr.P("And here is another piece of text -- you should be able to add any number"))

page.append(body)

render_page(page, "test_html_output2.html")

page = hr.Html()

head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough  to show that we can do some text"))
body.append(hr.P("And here is another piece of text -- you should be able to add any number"))

page.append(body)

render_page(page, "test_html_output3.html")

page = hr.Html()

head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough  to show that we can do some text",
              style="text-align: center; font-style: oblique;"))

page.append(body)

render_page(page, "test_html_output4.html")

page = hr.Html()

head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough  to show that we can do some text",
              style="text-align: center; font-style: oblique;"))

body.append(hr.Hr())

page.append(body)

render_page(page, "test_html_output5.html")


page = hr.Html()

head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough  to show that we can do some text",
              style="text-align: center; font-style: oblique;"))

body.append(hr.Hr())

body.append("And this is a ")
body.append( hr.A("http://google.com", "link") )
body.append("to google")

page.append(body)

render_page(page, "test_html_output6.html")

page = hr.Html()

head = hr.Head()
head.append(hr.Title("PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append( hr.H(2, "PythonClass - Class 6 example") )

body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough  to show that we can do some text",
              style="text-align: center; font-style: oblique;"))

body.append(hr.Hr())

list = hr.Ul(id="TheList", style="line-height:200%")

list.append( hr.Li("The first item in a list") )
list.append( hr.Li("This is the second item", style="color: red") )

item = hr.Li()
item.append("And this is a ")
item.append( hr.A("http://google.com", "link") )
item.append("to google")

list.append(item)

body.append(list)

page.append(body)

render_page(page, "test_html_output7.html")

page = hr.Html()


head = hr.Head()
head.append( hr.Meta(charset="UTF-8") )
head.append(hr.Title("PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append( hr.H(2, "PythonClass - Example") )

body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough  to show that we can do some text",
                 style="text-align: center; font-style: oblique;"))

body.append(hr.Hr())

list = hr.Ul(id="TheList", style="line-height:200%")

list.append( hr.Li("The first item in a list") )
list.append( hr.Li("This is the second item", style="color: red") )

item = hr.Li()
item.append("And this is a ")
item.append( hr.A("http://google.com", "link") )
item.append("to google")

list.append(item)

body.append(list)

page.append(body)

render_page(page, "test_html_output8.html")
