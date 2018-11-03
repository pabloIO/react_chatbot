import sys
import os.path
import json 
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import models.models as database
from sqlalchemy.exc import IntegrityError
import uuid
from config.config import env
from config.mongo_adapter import mongo
import time
import numpy as np
import pandas as pd
from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
import requests
import csv

class TfIdfCtrl(object):

    @staticmethod
    def word_cloud(db, response):
        try:
            res = {
                'success': False
            }
            total_df = []
            db_conversations = database.Conversacion.query.all()
            word_data =  []
            for conversation in db_conversations:
                word_data.append(conversation.texto)
            vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5)
            matrix = vectorizer.fit_transform(word_data).toarray()
            features = vectorizer.get_feature_names()
            data_frame = pd.DataFrame(matrix, columns=features)
            with open('local_data/analytics.csv', 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for f in features:
                    count = np.sum(data_frame[f])
                    total_df.append({'word': f, 'count': count})
                    writer.writerow([f, count])
            res['success'] = True
            res['word_cloud'] = total_df
        except Exception as e:
            print(e)
            res['msg'] = 'error'
            res['success'] = False
        finally: 
            return response(json.dumps(res), mimetype='application/json')
    @staticmethod
    def getConversations(db, response):
        try:
            res = {
                'success': False
            }
            db_conversations = database.Conversacion.query.all()
            user_conversation =  []
            for conversation in db_conversations:
                c = {
                    'id': conversation.id,
                    'created_at': str(conversation.fecha_creacion),
                    'message': conversation.texto,
                }
                user_conversation.append(c)
            res['success'] = True            
            res['conversations'] = user_conversation
        except Exception as e:
            res['msg'] = 'Hubo un error al obtener la conversación'
        finally:
            return response(json.dumps(res), mimetype='application/json')   