import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node,node2)

    def test_print(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.__repr__(),"TextNode(This is a text node,bold,None)")

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is not a text node", "italic")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
