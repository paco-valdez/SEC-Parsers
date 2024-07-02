from download import download_sec_filing
from lxml import etree
from parsers import recursive_parse, visualize_tree, construct_xml_tree
from style_detection import *
import os
from time import time

from xml_helper import find_by_text, get_all_text, get_text, print_tree,get_text_between_elements


dir_10k = "../../Data/10K"
files = os.listdir(dir_10k)
files = [dir_10k + "/" + file for file in files]

parser = etree.HTMLParser(encoding='utf-8',remove_comments=True)

for file in files[0:1]:
    print(file)
    with open(file, 'r',encoding='utf-8') as f:
        sec_html = f.read()

    s1 = time()
    parsed_html = etree.fromstring(sec_html, parser)
    # mutablity
    recursive_parse(parsed_html)
    e1 = time()
    print(e1-s1)
    #visualize_tree(parsed_html)
    #xml = construct_xml_tree(parsed_html)
    