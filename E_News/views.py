import json

from django.shortcuts import render

# Create your views here.
from django.template import loader
from elasticsearch import Elasticsearch


def news_items(request):
    newsData = []

    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    for x in range(2,40):
        results = es.get(index='finalnewsstore', doc_type='lankadeepa', id=x)

        pyData1 = json.dumps(results)
        pyData2 = json.loads(pyData1)

        id = pyData2['_id']
        TempNewsData = pyData2['_source']

        pyNewsData1 = json.dumps(TempNewsData)
        pyNewsData2 = json.loads(pyNewsData1)

        headline = pyNewsData2['newsHeadline']

        newsText = pyNewsData2['Summary']

        # commentsList = pyNewsData2['comments']

        date = pyNewsData2['date']

        # readerNames = pyNewsData2['readerNames']

        positivePercentage = pyNewsData2['PositivePercentage:']

        negativePercentage = pyNewsData2['NegativePercentage']

        neutralPercentage = pyNewsData2['NeutralPercentage']

        #     # "negativeSentimentScore": 0,

        # jobject = {
        #     "id": id,
        #     "newsHeadline": headline,
        #     "newsText": newsText,
        #     "comments": commentsList,
        #     "date": date,
        #     "readerNames": readerNames,
        #     # "positiveSentimentScore": 0,
        #     # "negativeSentimen
        #     tScore": 0,
        # }

        list = [id, headline, newsText, date, positivePercentage, negativePercentage, neutralPercentage]
        # newsData.append(list)

        # print(list[0])
        # print(list[1])
        # print(list[2])
        # print(list[3])

        newsData.append(list)

    template = 'E_News/news.html'
    return render(request, template, {'nd': newsData})


def myView(request):
    template = 'E_News/searchData.html'
    print(request.POST['search'])

    return render(request, template)


def crimeNewsDisplay(request):
    newsData = []

    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    for x in range(2, 32):
        results = es.get(index='finalnewsstore', doc_type='lankadeepa', id=x)

        pyData1 = json.dumps(results)
        pyData2 = json.loads(pyData1)

        id = pyData2['_id']
        TempNewsData = pyData2['_source']

        pyNewsData1 = json.dumps(TempNewsData)
        pyNewsData2 = json.loads(pyNewsData1)

        headline = pyNewsData2['newsHeadline']

        newsText = pyNewsData2['Summary']

        # commentsList = pyNewsData2['comments']

        date = pyNewsData2['date']

        # readerNames = pyNewsData2['readerNames']

        positivePercentage = pyNewsData2['PositivePercentage:']

        negativePercentage = pyNewsData2['NegativePercentage']

        neutralPercentage = pyNewsData2['NeutralPercentage']

        category=pyNewsData2['Category']


        list = [id, headline, newsText, date, positivePercentage, negativePercentage, neutralPercentage]

        if category == 'crime':
         newsData.append(list)

    template = 'E_News/crime.html'
    return render(request, template, {'nd': newsData})


def economicNewsDisplay(request):
    newsData = []

    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    for x in range(2, 32):
        results = es.get(index='finalnewsstore', doc_type='lankadeepa', id=x)

        pyData1 = json.dumps(results)
        pyData2 = json.loads(pyData1)

        id = pyData2['_id']
        TempNewsData = pyData2['_source']

        pyNewsData1 = json.dumps(TempNewsData)
        pyNewsData2 = json.loads(pyNewsData1)

        headline = pyNewsData2['newsHeadline']

        newsText = pyNewsData2['Summary']

        # commentsList = pyNewsData2['comments']

        date = pyNewsData2['date']

        # readerNames = pyNewsData2['readerNames']

        positivePercentage = pyNewsData2['PositivePercentage:']

        negativePercentage = pyNewsData2['NegativePercentage']

        neutralPercentage = pyNewsData2['NeutralPercentage']

        category=pyNewsData2['Category']


        list = [id, headline, newsText, date, positivePercentage, negativePercentage, neutralPercentage]

        if category == 'economic':
         newsData.append(list)

    template = 'E_News/economic.html'
    return render(request, template, {'nd': newsData})



def economicNewsDisplay(request):
    newsData = []

    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    for x in range(2, 32):
        results = es.get(index='finalnewsstore', doc_type='lankadeepa', id=x)

        pyData1 = json.dumps(results)
        pyData2 = json.loads(pyData1)

        id = pyData2['_id']
        TempNewsData = pyData2['_source']

        pyNewsData1 = json.dumps(TempNewsData)
        pyNewsData2 = json.loads(pyNewsData1)

        headline = pyNewsData2['newsHeadline']

        newsText = pyNewsData2['Summary']

        # commentsList = pyNewsData2['comments']

        date = pyNewsData2['date']

        # readerNames = pyNewsData2['readerNames']

        positivePercentage = pyNewsData2['PositivePercentage:']

        negativePercentage = pyNewsData2['NegativePercentage']

        neutralPercentage = pyNewsData2['NeutralPercentage']

        category=pyNewsData2['Category']


        list = [id, headline, newsText, date, positivePercentage, negativePercentage, neutralPercentage]

        if category == 'economic':
         newsData.append(list)

    template = 'E_News/economic.html'
    return render(request, template, {'nd': newsData})





def politicNewsDisplay(request):
    newsData = []

    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    for x in range(2, 32):
        results = es.get(index='finalnewsstore', doc_type='lankadeepa', id=x)

        pyData1 = json.dumps(results)
        pyData2 = json.loads(pyData1)

        id = pyData2['_id']
        TempNewsData = pyData2['_source']

        pyNewsData1 = json.dumps(TempNewsData)
        pyNewsData2 = json.loads(pyNewsData1)

        headline = pyNewsData2['newsHeadline']

        newsText = pyNewsData2['Summary']

        # commentsList = pyNewsData2['comments']

        date = pyNewsData2['date']

        # readerNames = pyNewsData2['readerNames']

        positivePercentage = pyNewsData2['PositivePercentage:']

        negativePercentage = pyNewsData2['NegativePercentage']

        neutralPercentage = pyNewsData2['NeutralPercentage']

        category=pyNewsData2['Category']


        list = [id, headline, newsText, date, positivePercentage, negativePercentage, neutralPercentage]

        if category == 'politics':
         newsData.append(list)

    template = 'E_News/politics.html'
    return render(request, template, {'nd': newsData})




def sportNewsDisplay(request):
    newsData = []

    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    for x in range(2, 100):
        results = es.get(index='finalnewsstore', doc_type='lankadeepa', id=x)

        pyData1 = json.dumps(results)
        pyData2 = json.loads(pyData1)

        id = pyData2['_id']
        TempNewsData = pyData2['_source']

        pyNewsData1 = json.dumps(TempNewsData)
        pyNewsData2 = json.loads(pyNewsData1)

        headline = pyNewsData2['newsHeadline']

        newsText = pyNewsData2['Summary']

        # commentsList = pyNewsData2['comments']

        date = pyNewsData2['date']

        # readerNames = pyNewsData2['readerNames']

        positivePercentage = pyNewsData2['PositivePercentage:']

        negativePercentage = pyNewsData2['NegativePercentage']

        neutralPercentage = pyNewsData2['NeutralPercentage']

        category=pyNewsData2['Category']


        list = [id, headline, newsText, date, positivePercentage, negativePercentage, neutralPercentage]

        if category == 'sports':
         newsData.append(list)

    template = 'E_News/sports.html'
    return render(request, template, {'nd': newsData})


def foreignNewsDisplay(request):
    newsData = []

    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    for x in range(2, 100):
        results = es.get(index='finalnewsstore', doc_type='lankadeepa', id=x)

        pyData1 = json.dumps(results)
        pyData2 = json.loads(pyData1)

        id = pyData2['_id']
        TempNewsData = pyData2['_source']

        pyNewsData1 = json.dumps(TempNewsData)
        pyNewsData2 = json.loads(pyNewsData1)

        headline = pyNewsData2['newsHeadline']

        newsText = pyNewsData2['Summary']

        # commentsList = pyNewsData2['comments']

        date = pyNewsData2['date']

        # readerNames = pyNewsData2['readerNames']

        positivePercentage = pyNewsData2['PositivePercentage:']

        negativePercentage = pyNewsData2['NegativePercentage']

        neutralPercentage = pyNewsData2['NeutralPercentage']

        category=pyNewsData2['Category']


        list = [id, headline, newsText, date, positivePercentage, negativePercentage, neutralPercentage]

        if category == 'foreign':
         newsData.append(list)

    template = 'E_News/foreign.html'
    return render(request, template, {'nd': newsData})