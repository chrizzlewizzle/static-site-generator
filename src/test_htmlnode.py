import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>")     

    def test_to_html_many_children(self):
        parent_node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Second normal text")])
        self.assertEqual(parent_node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Second normal text</p>")

    def test_headings(self):
        parent_node = ParentNode("h2", [
            LeafNode("i", "Italic text"),
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Normal text")])
        self.assertEqual(parent_node.to_html(), "<h2><i>Italic text</i><b>Bold text</b>Normal text<i>Italic text</i>Normal text</h2>")

if __name__ == "__main__":
    unittest.main()