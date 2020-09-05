from flask import Flask, request
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)


@app.route('/')
def Welcome():
    return "Hello All"


@app.route('/predict', methods=['GET', 'POST'])
def Inputs():
    Age = request.args.get('Age')
    df = pd.read_csv('scaled.csv')
    Scaler = MinMaxScaler()
    df['Age'] = Scaler.fit_transform(df[['Age']])
    Age = Scaler.transform([[Age]])[0][0]
    print(Age)
    Gender = request.args.get('Gender')

    if Gender == 'female':
        Gender = 0
    elif Gender == 'male':
        Gender = 1
    else:
        Gender = 2

    print(Gender)
    family_history = request.args.get('Family_History')

    if family_history == 'No':
        family_history = 0
    else:
        family_history = 1

    print(family_history)

    benefits = request.args.get('Benefits')
    if benefits == 'No idea':
        benefits = 0
    elif benefits == 'No':
        benefits = 1
    else:
        benefits = 2

    print(benefits)

    care_options = request.args.get('Care_Options')

    if care_options == 'No':
        care_options = 0
    elif care_options == 'Not Sure':
        care_options = 1
    else:
        care_options = 2
    print(care_options)
    anonymity = request.args.get('Anonymity')

    if anonymity == 'No idea':
        anonymity = 0
    elif anonymity == 'No':
        anonymity = 1
    else:
        anonymity = 2
    print(anonymity)
    Leave = request.args.get('Leave')

    if Leave == 'No idea':
        Leave = 0
    elif Leave == 'Somewhat difficult':
        Leave = 1
    elif Leave == 'Somewhat easy':
        Leave = 2
    elif Leave == 'Very Difficult':
        Leave = 3
    else:
        Leave = 4
    print(Leave)

    Work_interfere = request.args.get('Work_Interfere')

    if Work_interfere == 'No idea':
        Work_interfere = 0
    elif Work_interfere == 'Never':
        Work_interfere = 1
    elif Work_interfere == 'Often':
        Work_interfere = 2
    elif Work_interfere == 'Rarely':
        Work_interfere = 3
    else:
        Work_interfere = 4

    print(Work_interfere)


    Input = [Age, Gender, family_history, benefits, care_options, anonymity, Leave, Work_interfere]
    print(Input)

    pickle_in = open('depress.pkl', "rb")
    classifier = pickle.load(pickle_in)
    print(classifier.predict([Input])[0])
    return Result(classifier.predict([Input])[0])

def Result(val):
    if val == 1:
        return "It is advisable to visit a psychiatrist"
    else:
        return "Your are perfectly alright"



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
