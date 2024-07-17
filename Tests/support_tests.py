from sec_parsers import set_headers, download_sec_filing
from sec_parsers import Filing
from sec_parsers.xml_helper import get_all_text
from sec_parsers.style_detection import detect_part
from sec_parsers.experimental_parsers import SEC10QParser
from time import time
set_headers('John Smith','example@example.com')

# looks like S-1 filings can be supported with minor tweaks, same for s3
s1_urls = ['https://www.sec.gov/Archives/edgar/data/1713445/000162828024006294/reddits-1q423.htm']
urls_10k = ['https://www.sec.gov/Archives/edgar/data/1318605/000095017022000796/tsla-20211231.htm']
urls_8k =['https://www.sec.gov/Archives/edgar/data/1318605/000095017023038779/tsla-20230804.htm']
html = download_sec_filing(urls_10k[0])

filing = Filing(html)

parent = filing.html.xpath("//span[text() = 'ART I']")[0].getparent()

s = time()
filing.parse()
#filing.visualize()
print(filing.get_title_tree())
filing.save_xml('test.xml')
print('Parsing time:',time()-s)

