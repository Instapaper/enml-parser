import lxml.html
from lxml import etree

class ENMLParser():
    content = None
    permitted_elements = ['a', 'abbr', 'acronym', 'address',
        'area', 'b', 'bdo', 'big', 'blockquote', 'br', 'caption',
        'center', 'cite', 'code', 'col', 'colgroup', 'dd', 'del',
        'dfn', 'div', 'dl', 'dt', 'em', 'font', 'h1', 'h2', 'h3',
        'h4', 'h5', 'h6', 'hr', 'i', 'img', 'ins', 'kbd', 'li',
        'map', 'ol', 'p', 'pre', 'q', 's', 'samp', 'small', 'span',
        'strike', 'strong', 'sub', 'sup', 'table', 'tbody', 'td',
        'tfoot', 'th', 'tfoot', 'th', 'thead', 'title', 'tr', 'tt',
        'u', 'var', 'xmp'
    ]
    permitted_attrs = ['href', 'src']

    def __init__(self, content):
        self.content = content
        parser = lxml.html.HTMLParser(encoding='utf-8')
        self.lxml = lxml.html.document_fromstring(content, parser=parser)

    def parse(self):
        if self.lxml == None:
            return content

        if not self.lxml.tag in self.permitted_elements:
            self.lxml.tag = 'div'

        for elem in self.lxml.xpath('//*'):
            if not etree.iselement(elem):
                elem.drop_tree()
            elif not elem.tag in self.permitted_elements:
                elem.drop_tag()
            elif elem.tag == 'a' and 'href' in elem.attrib and elem.attrib['href'].startswith('javascript:'):
                elem.drop_tag()
            
            for key in elem.attrib:
                if not key in self.permitted_attrs:
                    elem.attrib.pop(key)

        return etree.tostring(
            self.lxml, method='xml',
            encoding='utf-8', xml_declaration=None,
            pretty_print=False, with_tail=True,
            standalone=None
        )

