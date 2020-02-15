import json

from django.shortcuts import render

# Create your views here.
from django.template import loader
from elasticsearch import Elasticsearch


def news_items(request):
    newsData = []

    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    for x in range(1, 31):
        results = es.get(index='prenews', doc_type='lankadeepa', id=x)

        pyData1 = json.dumps(results)
        pyData2 = json.loads(pyData1)

        id = pyData2['_id']
        TempNewsData = pyData2['_source']

        pyNewsData1 = json.dumps(TempNewsData)
        pyNewsData2 = json.loads(pyNewsData1)

        headline = pyNewsData2['newsHeadline']

        newsText = pyNewsData2['newsText']

        commentsList = pyNewsData2['comments']

        date = pyNewsData2['date']

        readerNames = pyNewsData2['readerNames']

        # jobject = {
        #     "id": id,
        #     "newsHeadline": headline,
        #     "newsText": newsText,
        #     "comments": commentsList,
        #     "date": date,
        #     "readerNames": readerNames,
        #     # "positiveSentimentScore": 0,
        #     # "negativeSentimentScore": 0,
        # }

        list = [id, headline, newsText, date]
        # newsData.append(list)

        # print(list[0])
        # print(list[1])
        # print(list[2])
        # print(list[3])

        newsData.append(list)

    template = 'AppOne/news.html'
    return render(request, template, {'nd': newsData})
