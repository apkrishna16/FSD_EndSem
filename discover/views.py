from django.shortcuts import render
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from .models import Question, Option
from shop.models import Plant
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def discover(request):
    if request.method == 'POST':
         
        user_responses = {}
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = int(key.split('_')[1])
                user_responses[question_id] = value

      
        plants = Plant.objects.all()

        plant_data = []
        for plant in plants:
            attributes = [
                plant.light_requirements,
                plant.watering_frequency,
                plant.maintenance_level,
                plant.growth_rate,
                plant.preferred_climate,
                plant.plant_size,
                'Yes' if plant.allergy_concerns else 'No',
                plant.aesthetic_preference,
                plant.purpose,
                plant.room_temperature,
                plant.humidity_level,
            ]
            plant_data.append({
                'id': plant.id,
                'common_name': plant.common_name,
                'attributes': " ".join(attributes),
            })

        df = pd.DataFrame(plant_data)
 
        user_input = " ".join(user_responses.values())
        user_row = pd.DataFrame({'id': [None], 'common_name': ['User'], 'attributes': [user_input]})
        df = pd.concat([df, user_row], ignore_index=True)

        vectorizer = CountVectorizer()
        vectors = vectorizer.fit_transform(df['attributes'])
        similarity_matrix = cosine_similarity(vectors)

        user_index = len(df) - 1
        similarities = similarity_matrix[user_index][:-1]
        closest_index = similarities.argmax()

        closest_plant = plants[int(closest_index)]

        return render(request, 'quiz_result.html', {'plant': closest_plant})

    questions = Question.objects.prefetch_related('options').all()
    return render(request, 'quiz_page.html', {'questions': questions})
