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
    def __init__(self, tag, value, props = None): # No children here because the leaf has no children. Props is optional
        super().__init__(tag, value, None, props) # Children is set to None but included because here you initialize LeafNode as a HTMLNode subclass
        
    def to_html(self):
            if self.value is None:
                raise ValueError("All leaf nodes must have a value")
            elif self.tag is None:
                return self.value # If there's no tag just return the value
            else:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>" # Make a line of proper HTML out of tag and value
            
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
            
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None): # Props is optional, tag and children are not
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if self.children is None:
            raise ValueError("All parent nodes must have at least 1 child")
        else:
            children_html = ""
            for child in self.children:
                children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"