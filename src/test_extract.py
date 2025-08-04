import unittest

from extract import extract_markdown_images, extract_markdown_links

class Testextract(unittest.TestCase):
    def test_simple_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        test1 = extract_markdown_images(text)
        self.assertEqual([('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')], test1)
    
    def test_simple_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        test1 = extract_markdown_links(text)
        self.assertEqual([('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')], test1)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_image_link_extract(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and image ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        test1 = extract_markdown_links(text)
        self.assertEqual([('to boot dev', 'https://www.boot.dev')], test1)
    
    def test_link_image_extract(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and image ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        test1 = extract_markdown_images(text)
        self.assertEqual([('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')], test1)

    
if __name__ == "__main__":
    unittest.main()