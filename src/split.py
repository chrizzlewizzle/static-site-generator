from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = []
    
    for node in old_nodes:
        if node.text_type == text_type.TEXT:
            split_text = node.text.split(delimiter)
            
            if len(split_text) % 2 == 0: # even amount of items in the list must mean a closing delimiter is missing
                raise Exception("You've not properly closed your markdown dummy")
            
            for i in range(len(split_text)):
                node_type = TextType.TEXT if i % 2 == 0 else text_type # if is even this must be a text node, otherwise use parameter from split_nodes_delimiter
                split_nodes.append(TextNode(split_text[i], node_type))

        else:
            split_nodes.append(node)
    
    return split_nodes