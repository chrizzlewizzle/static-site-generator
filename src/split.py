from textnode import TextNode, TextType
from extract import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = []
    
    for node in old_nodes:
        # print(f"Node is ", node)
        if node.text_type == text_type.TEXT:
            split_text = node.text.split(delimiter)
            
            if len(split_text) % 2 == 0: # even amount of items in the list must mean a closing delimiter is missing
                raise Exception("You've not properly closed your markdown you dummy")
            
            for i in range(len(split_text)):
                # print(f"Split text is ", split_text[i])
                node_type = TextType.TEXT if i % 2 == 0 else text_type # if is even this must be a text node, otherwise use parameter from split_nodes_delimiter
                split_nodes.append(TextNode(split_text[i], node_type))

        else:
            split_nodes.append(node)
    
    return split_nodes

def split_nodes_image(old_nodes):
    split_nodes = []        
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
            
        original_text = node.text
        images = extract_markdown_images(original_text)
        
        if len(images) == 0:
            split_nodes.append(node)
            continue
        
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("You've not properly closed your image section markdown you dummy")
            
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            split_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
            
        if original_text != "":
            split_nodes.append(TextNode(original_text, TextType.TEXT))
    
    return split_nodes       
               
    
def split_nodes_link(old_nodes):
    split_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
            
        original_text = node.text
        links = extract_markdown_links(original_text)
        
        if len(links) == 0:
            split_nodes.append(node)
            continue
        
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("You've not properly closed your link section markdown you dummy!")
            
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
                
            split_nodes.append(
                TextNode(
                    link[0],
                    TextType.LINK,
                    link[1],
                )
            )
            original_text = sections[1]
            
        if original_text != "":
            split_nodes.append(TextNode(original_text, TextType.TEXT))
    
    return split_nodes