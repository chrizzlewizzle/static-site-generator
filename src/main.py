from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from split import split_nodes_delimiter

# print("hello world")

# test1 = TextNode("text", TextType.BOLD)
# print("Test1: ", test1.text, test1.text_type.value, test1.url)
# print(test1)

def main():
    # textnode1 = TextNode("This is some anchor text", TextType.LINK,"https://www.boot.dev")
    # print(textnode1)
    
    # htmlnode1 = HTMLNode("a", None, None,{"href": "https://www.google.com","target": "_blank"})
    #print(htmlnode1.props)
    #print(htmlnode1)
    
    #leafnode1 = LeafNode("a", "This is a paragraph of text.", {"href": "https://wwww.watbenjedan.nl"})
    #print(leafnode1)
    #print(leafnode1.to_html())
    
    # childnode1 = LeafNode("span", "child")
    # parentnode1 = ParentNode("div", [childnode1])
    #print(parentnode1.to_html())

main()