# ENMLParser

ENMLParser is a Python class that converts HTML to [Evernote Markup Language](https://dev.evernote.com/doc/articles/enml.php).

# About

ENMLParser is the class Instapaper uses to convert HTML displayed within Instapaper to ENML that can be uploaded to the Evernote API.

# Usage

    from enml_parser import ENMLParser
    parser = ENMLParser(html_content)
    enml = parser.parse()
    print 'ENML: %s' % enml

