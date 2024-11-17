from sec_parsers.detectors import StyleTagDetector
from sec_parsers.style_detection import (
    detect_link,
    detect_bold_from_html,
    detect_strong_from_html,
    detect_emphasis_from_html,
    detect_italic_from_html,
    detect_underline_from_html,
    detect_table,
    detect_table_of_contents,
    detect_image,
    detect_type,
    detect_sequence,
    detect_filename,
    detect_description,
    detect_text,
)


class LinkTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style="link;", **kwargs)

    def detect(self, element):
        if detect_link(element):
            return "link;"
        else:
            return ""


class BoldTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style="bold;", **kwargs)

    def detect(self, element):
        if detect_bold_from_html(element):
            return "bold;"
        else:
            return ""


class StrongTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style="strong;", **kwargs)

    def detect(self, element):
        if detect_strong_from_html(element):
            return "strong;"
        else:
            return ""


class EmphasisTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style="emphasis;", **kwargs)

    def detect(self, element):
        if detect_emphasis_from_html(element):
            return "emphasis;"
        else:
            return ""


class ItalicTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style="italic;", **kwargs)

    def detect(self, element):
        if detect_italic_from_html(element):
            return "italic;"
        else:
            return ""


class UnderlineTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style="underline;", **kwargs)

    def detect(self, element):
        if detect_underline_from_html(element):
            return "underline;"
        else:
            return ""


class TableTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style="table;", **kwargs)

    def detect(self, element):
        if detect_table(element):
            return "table;"

        return ""


class TableOfContentsTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style="table of contents;", **kwargs)

    def detect(self, element):
        if detect_table(element):
            if detect_table_of_contents(element) == "toc":
                return "table of contents;"

        return ""


class ImageTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style="image;", **kwargs)

    def detect(self, element):
        if detect_image(element):
            return "image;"
        else:
            return ""


class TypeTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style="type;", **kwargs)

    def detect(self, element):
        if detect_type(element):
            return "type;"
        else:
            return ""


class SequenceTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style="sequence;", **kwargs)

    def detect(self, element):
        if detect_sequence(element):
            return "sequence;"
        else:
            return ""


class FilenameTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style="filename;", **kwargs)

    def detect(self, element):
        if detect_filename(element):
            return "filename;"
        else:
            return ""


class DescriptionTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style="description;", **kwargs)

    def detect(self, element):
        if detect_description(element):
            return "description;"
        else:
            return ""


class TextTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style="text;", **kwargs)

    def detect(self, element):
        if detect_text(element):
            return "text;"
        else:
            return ""
