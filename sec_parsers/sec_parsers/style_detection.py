import re
from xml_helper import get_all_text



# since we need styles that are non standardized this will be fun

def detect_style(string):
    def detect_emphasis_capitalization(string):
        """Seen in amazon's 2024 10k e.g. We Have Foreign Exchange Risk"""
        words = string.split()
        if not words:
            return False
        for word in words:
            if word.lower() in ["of",'to','a','and','by','in','the','or','on','for']:
                continue
            if not word[0].isupper():
                return False
        return True
    
    def detect_item(string):
        """e.g. Item 1A. Risk Factors"""
        match = re.search(r"^Item\s+\d+[A-Z]",string, re.IGNORECASE)
        if match:
            return True
        return False
        
    def level_detection(string):
        """e.g. amazon Level 1"""
        match = re.search(r"^Level\s+\d+",string)
        if match:
            return True
        return False
        
    def title_case(string):
        """e.g. The power of AI from google 10k"""

        if '.' in string:
            return False
        words = string.split()
        if not words:
            return False
        
        if words[0].istitle():
            return True
        
        return False

    def note_detection(string):
        """e.g. Note 1"""
        match = re.search(r"^Note\s+\d+",string, re.IGNORECASE)
        if match:
            return True
        return False

    
    if detect_emphasis_capitalization(string):
        return 'emphasis'
    elif detect_item(string):
        return 'item'
    elif level_detection(string):
        return 'level'
    elif title_case(string):
        return 'title case'
    elif note_detection(string):
        return 'note'
    else:
        return 'no style found'
    

def detect_table(table):
    """Detects if table or header disguised as a table"""
    def is_number(s):
        """
        Checks if a string is a number.

        Args:
            s: The string to check.

        Returns:
            True if the string is a number, False otherwise.
        """
        try:
            float(s)
            return True
        except ValueError:
            return False
        
    number_count = 0
    if table.tag == 'table':
        for row in table.xpath('tr'):
            for cell in row.xpath('td | th'):
                text = get_all_text(cell)
                if is_number(text):
                    number_count += 1

        if number_count > 5:
            return True
    return False

def detect_toc_link(node):
    """Detects if a node is a table of contents link."""
    if node.tag == 'a':
        text = get_all_text(node)
        if text.lower() in ['table of contents','toc']:
            return True
    return False