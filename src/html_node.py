


class HTMLNode:
    def __init__(self, tag=None,value=None, children=[], props={}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props #{"href": "https://www.google.com"}

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        stringRes = ""
        last_key = list(self.props)[-1]
        
        for key, val in self.props.items():
            if key != last_key:
                stringRes += f"{key}=\"{val}\" "
            else:
                stringRes += f"{key}=\"{val}\""

        return stringRes

    def __repr__(self):
        return f"HTMLNODE({self.tag},{self.value},{self.children},{self.props})"


node = HTMLNode("a", "I Love Apples", [],{"href":"https://www.google.com","target":"_blank"})
node.to_html()