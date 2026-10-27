from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    exp_return = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            exp_return.append(node)
            continue
        rebuild = node.text.split(delimiter)
        if len(rebuild)%2 == 0:
            raise Exception("incorrect delimiter pairing")
        elif len(rebuild) == 1:
             exp_return.append(node)
             continue
        for i, x in enumerate(rebuild):
            if i%2 == 0:
                exp_return.append(TextNode(rebuild[i], TextType.TEXT))
            else:
                    exp_return.append(TextNode(rebuild[i], text_type))
    return exp_return