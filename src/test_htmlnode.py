import unittest
from html_node import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "I Love Apples", [],{"href":"https://www.google.com","target":"_blank"})
        print(node)
        self.assertEqual(node.props_to_html(),"href=\"https://www.google.com\" target=\"_blank\"")

