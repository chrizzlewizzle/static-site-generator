import unittest

from split import split_nodes_delimiter
from textnode import TextNode, TextType


class Testsplit(unittest.TestCase):
    def test_single_code_creation(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        test1 = split_nodes_delimiter([node], "`", TextType.CODE)
        test2 = [TextNode("This is text with a ", TextType.TEXT, None), TextNode("code block", TextType.CODE, None), TextNode(" word", TextType.TEXT, None)]
        self.assertEqual(test1, test2)

    def test_single_bold_block(self):
        node = TextNode("This is text with a *bold block* word", TextType.TEXT)
        test1 = split_nodes_delimiter([node], "*", TextType.BOLD)
        test2 = [TextNode("This is text with a ", TextType.TEXT, None), TextNode("bold block", TextType.BOLD, None), TextNode(" word", TextType.TEXT, None)]
        self.assertEqual(test1, test2)

    def test_multiple_bold_block(self):
        node = TextNode("Text *bold* text *bold* text", TextType.TEXT)
        test1 = split_nodes_delimiter([node], "*", TextType.BOLD)
        test2 = [TextNode("Text ", TextType.TEXT, None), TextNode("bold", TextType.BOLD, None), TextNode(" text ", TextType.TEXT, None), TextNode("bold", TextType.BOLD, None), TextNode(" text", TextType.TEXT, None)]
        self.assertEqual(test1, test2)

    def test_not_properly_closed_markdown(self):
        node = TextNode("Text *bold* text *bold text", TextType.TEXT)
        
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "*", TextType.BOLD)

if __name__ == "__main__":
    unittest.main()