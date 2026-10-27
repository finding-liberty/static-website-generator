
from node_splitter import split_nodes_delimiter
from links_and_images import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType



def text_to_textnodes(text):
    exp_return = [TextNode(text, TextType.TEXT)]
    exp_return = split_nodes_delimiter(exp_return, "**", TextType.BOLD)
    exp_return = split_nodes_delimiter(exp_return, "_", TextType.ITALIC)
    exp_return = split_nodes_delimiter(exp_return, "`", TextType.CODE)
    exp_return = split_nodes_image(exp_return)
    exp_return = split_nodes_link(exp_return)
    return exp_return