import unittest

from split import split_nodes_delimiter, split_nodes_image, split_nodes_link
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
            
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()