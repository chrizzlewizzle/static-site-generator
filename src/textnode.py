from enum import Enum

class TextType(Enum): # what inline texts do we support?
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text # text content
        self.text_type = text_type # What text type? See TextType
        self.url = url # url for link or image
        
        
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        
    def __repr__ (self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"