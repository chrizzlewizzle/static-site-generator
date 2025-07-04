class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag # HTML tag (p, a, h1, h2, etc)
        self.value = value # Value of the HTML tag, so the text inside the paragraph
        self.children = children # HTML is nested nodes, so these are all the children of this node
        self.props = props # Dictionary of key-value pairs with attributes of the HTML tag. So <a> tag might have {"href": "https://www.watbenjedan.nl"}
    
    def to_html(self): # Child classes will override this method to render themselves as HTML?
        raise NotImplementedError
    
    def props_to_html(self):
        output = "" 
        local_props = self.props # Local variable so we can change it when props is not defined
        if self.props == None: # If props is none, then use an empty dictionary so it's still iterable
            local_props = {}
        
        for attribute in local_props: # Props is a dictionary of key-value pairs, here we loop over each pair in the dictionary
            value = local_props[attribute] # Attribute is the key, value is value
            output += " " + attribute + "=\"" + value + "\"" # Combine attribute and value with leading space, = in the middle and "" around value
        
        return output
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode)        :
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
            if self.value == None:
                return ValueError("All leaf nodes must have a value")
            elif self.tag == None:
                return value
            else:
                return "<" + self.tag + self.props_to_html() + ">" + self.value + "</" + self.tag + ">"