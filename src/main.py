from textnode import TextNode, TextType
from htmlnode import HTMLNode

# print("hello world")

# test1 = TextNode("text", TextType.BOLD)
# print("Test1: ", test1.text, test1.text_type.value, test1.url)
# print(test1)

def main():
    # textnode1 = TextNode("This is some anchor text", TextType.LINK,"https://www.boot.dev")
    # print(textnode1)
    
    htmlnode1 = HTMLNode("a", None, None,{"href": "https://www.google.com","target": "_blank"})
    print(htmlnode1.props)
    print(htmlnode1)
    
main()