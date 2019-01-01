#!/usr/bin/env python3


class Element:
    tag = "html"
    indent = "    "


    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

        self.attributes = ''.join(' {} = "{}"'.format(k, v)
            for k, v in kwargs.items())


    def append(self, content):
        self.contents.append(content)


    def render(self, out_file, indent = ''):
        out_file.write('<{}>\n'.format(self.tag))

        for line in self.contents:
            out_file.write(line)
            out_file.write('\n')

        out_file.write('</{}>\n'.format(self.tag))


class Html(Element):
    tag = 'html'

    def render(self, file_out, indent=""):
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self, file_out, indent)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    tag = ''

    def render(self, file_out, indent=""):
        file_out.write('{}<{}{}>{}</{}>\n'.format(indent, self.tag, self.attributes, self.contents[0], self.tag))


class Title(OneLineTag):
    tag = 'title'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, html_address, text):
        OneLineTag.__init__(self, text, a=html_address)


class Ul(Element):
    tag = 'u1'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    """
    subclass for H tag from one line tag
    """
    def __init__(self, h_counter, header):
        self.tag = u'h' + str(h_counter)
        Element.__init__(self, header)


class SelfClosingTag(Element):
    """
    subclass for closing tag from element
    """
    def render(self, file_out, indent=""):
        file_out.write('{}<{}{} />\n'.format(indent, self.tag, self.attributes))


class Hr(SelfClosingTag):
    """
    subclass for hr closing from self closing tag
    """
    tag = 'hr'


class Br(SelfClosingTag):
    """
    subclass for break from self closing tag
    """
    tag = 'br'


class Meta(SelfClosingTag):
    """
    subclass for meta from self closing tag
    """
    tag = 'meta'


"""
Creating classes
"""

e = Element()
e = Element('hello')
print(e)
