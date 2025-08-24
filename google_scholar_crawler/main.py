# from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os

# 不再爬取谷歌学术数据，直接生成空值
# author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
# scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])

# 创建空的作者数据
author = {
    'name': 'Empty Data',
    'citedby': 0,
    'publications': {},
    'updated': str(datetime.now())
}

name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
