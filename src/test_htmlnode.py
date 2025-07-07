import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_props(self):
        node1 = HTMLNode(tag="a", value="10", children=None)
        test1 = node1.props_to_html()
        test2 = ""
        self.assertEqual(test1, test2)

    def test_single_props(self):
        node1 = HTMLNode(props={"href": "https://www.watbenjedan.nl"})
        test1 = node1.props_to_html()
        test2 = " href=\"https://www.watbenjedan.nl\""
        self.assertEqual(test1, test2)
        
    def test_multiple_props(self):
        node1 = HTMLNode(props={"href": "https://www.watbenjedan.nl","target": "_blank"})
        test1 = node1.props_to_html()
        test2 = " href=\"https://www.watbenjedan.nl\" target=\"_blank\""
        self.assertEqual(test1, test2)
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "This is a link", {"href": "https://www.watbenjedan.nl","target": "_blank"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.watbenjedan.nl\" target=\"_blank\">This is a link</a>")