from modules.crawler.utils import parserTargetURL
from modules.crawler.utils import run
import pandas


# print(parserTargetURL('board', board='Baseball'))
# print(parserTargetURL('board',
#                       board='Baseball',
#                       pageNum='19621'))
# print(parserTargetURL('article'))
# print(parserTargetURL('article',
#                       articleURL='/bbs/Baseball/M.1752411597.A.6CA.html'))


data = run(board='Baseball', pageNum='19621')
print(pandas.DataFrame(data))