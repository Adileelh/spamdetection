
from django.shortcuts import render
from joblib import load
import pandas as pd

model = load('static/best_model.pkl')

# Create your views here.
def single_predict(request):
    message = ''

    if request.method == 'POST':
        email = request.POST['email']
        prediction = model.predict([email])
        is_spam = 'Yes' if prediction else 'No'
        message = f'The email is spam: {is_spam}'

    return render(request, 'single_predict.html', {'message': message})

def bulk_predict(request):
    message = ''

    if request.method == 'POST':
        dataset = pd.read_csv(request.FILES['file'], sep="\t", header=0, names=['label', 'message'])
        predictions = model.predict(dataset['message'])
        dataset['is_spam'] = ['Yes' if prediction else 'No' for prediction in predictions]
        message = dataset.to_html()

    return render(request, 'bulk_predict.html', {'message': message})
