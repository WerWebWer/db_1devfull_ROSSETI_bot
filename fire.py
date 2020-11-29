import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore
import datetime

def send_data(name, solution):
    now = datetime.datetime.now()
    cred = credentials.Certificate('c:/Users/Werwe/Desktop/hack/bot/ppp.json')
    firebase_admin.initialize_app(cred, 
    {
    'databaseURL': 'https://rosseti-c446a.firebaseio.com/'
    })
    db = firestore.client()
    doc_ref = db.collection(u'applications')

    data = {
        u'authorlogin': u"+7(999)1001212",
        u'authors': [{u"department" : u"тех сервис магистральных сетей",u'login': u"+7(999)1001212",u"name": u"Андрей Светаев",u"password":u"1",u"role":u"user"}],
        u"authorsPositions": [u"нормальный поц"],
        u"bounty": [],
        u'branch': u'Отдел название',
        u'category': u'  эксплуатация магистральных сетей',
        u"cost": [{u"этап1": u"100"}, {u"этап2": u"200"}, {u"этап3": u"300"}],
        u'createDate': 1606507384,
        u"current": u"ээээ",
        u"effect": u"оптимизация",
        u"makeEconomy": u"true",
        u"name": u"" + str(name),
        u"scope": u"ээээ",
        u"solution": u"" + str(solution),
        u"stages": [{"этап1": "описание1"},{"этап2": "описание2"},{"этап3": "описание3"}],
        u"status": u"на расмотрении этап 1 из 3",
    }

    db.collection(u'suggestions').document(u'one'+str(now.microsecond)+str(now.second)+str(now.minute)).set(data)
