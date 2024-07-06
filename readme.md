# SEC Parsers
Parses non-standardized SEC 10-K filings into well structured detailed xml. This is a WIP. Not every file will parse correctly.

![](https://raw.githubusercontent.com/john-friedman/SEC-Parsers/main/Assets/tesla_visualization.png)
![](https://raw.githubusercontent.com/john-friedman/SEC-Parsers/main/Assets/tesla_tree.png)

### Installation
```pip install sec-parsers```

### Quickstart
```
from sec_parsers import *

html = download_sec_filing('https://www.sec.gov/Archives/edgar/data/1318605/000162828024002390/tsla-20231231.htm')
parsed_html = parse_10k(html)
xml = construct_xml_tree(parsed_html)
```

For more information look at the [quickstart](Examples/quickstart.ipynb), or view a parsed Tesla 10-K [here](Examples/tesla.xml).

### Links:
* [GitHub](https://github.com/john-friedman/SEC-Parsers/)
* [Archive of Parsed XMLs](https://www.dropbox.com/scl/fo/np1lpow7r3bissz80ze3o/AKGM8skBrUfEGlSweofAUDU?rlkey=cz1r78jofntjeq4ax2vb2yd0u&e=1&st=mdcwgfcm&dl=0) - Note: This is often out of date, as package is being updated frequently.

### Problem:
When you look at an SEC 10-K you can easily see the structure of the file, and what headers follow each other. Under the hood, these filings are non-standardized making it hard to convert into a well structured format suitable for NLP/RAG.

### How SEC Parsers works:
1. Detects headers in filings using:
* element tags, e.g. `<b>Item 1</b>`
* element css, e.g. `<p style="font-weight: bold;">Item 1.</p>`
* text style, e.g. emphasis style "Purchase of Significant Equipment"
* relative location of above elements to each other
2. Calculates hierarchy of headers, and converts to a tree structure

### Priority TODO
1. Test Parser + improve low hanging fruit
2. Get Input on design, etc
3. organize and clean code

### Future
* fix titles for xml (e.g. item 1 instead of item 1. business)
* better hierarchy calculation
* more supported filings: 10-Q, 8-K, etc
* better rag integration
* converting html tables to nice xml tables
* metadata, e.g. cik / data from xbrl in html
* hosting cleaned xml files online
* better attributes (names / format)
* better color scheme (color scheme for headers, ignored_elements - e.g. page numbers, text)
* better function naming
* better modules naming
* better parent handling
* better descriptions of functions
* better github and pypi pages

### Statistics
Not implemented yet.

### Some Other Packages that might be useful:
* [edgartools](https://github.com/dgunning/edgartools) - good interface for interacting with SEC's EDGAR system

### Alternative Approaches I've seen to parse SEC Filings
* [sec-parser](https://github.com/alphanome-ai/sec-parser) - oops, we have similar names. They were first, my bad. They parse 10-Qs well.
* [sec-api](https://sec-api.io/). Paid API to search / download SEC filings. Basically, SEC's EDGAR but setup in a much nicer format. I haven't used it since it costs money.
* [Bill McDonald's 10-X Archive](https://sraf.nd.edu/data/stage-one-10-x-parse-data/)
* Computer Vision using OpenCV
* LLMs (I believe unstructured.io does something like this)
* Transformers 