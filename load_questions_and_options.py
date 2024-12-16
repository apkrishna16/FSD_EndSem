from discover.models import Question, Option

# Define questions and options based on plant features
plant_questions = [
    {
        'text': 'What is the light level in the room where the plant will be placed?',
        'options': ['Low', 'Medium', 'High']
    },
    {
        'text': 'How often do you prefer to water your plants?',
        'options': ['Weekly', 'Bi-weekly', 'Monthly']
    },
    {
        'text': 'What level of maintenance are you comfortable with?',
        'options': ['Low', 'Medium', 'High']
    },
    {
        'text': 'What growth rate suits your preference?',
        'options': ['Slow', 'Medium', 'Fast']
    },
    {
        'text': 'Which climate does the plant need to thrive in?',
        'options': ['Tropical', 'Arid', 'Temperate', 'Cold', 'Subtropical']
    },
    {
        'text': 'What size plant are you looking for?',
        'options': ['Small', 'Medium', 'Large']
    },
    {
        'text': 'Do you have any allergy concerns?',
        'options': ['Yes', 'No']
    },
    {
        'text': 'What aesthetic preference do you have for your plant?',
        'options': ['Minimalist', 'Lush', 'Unique', 'Classic', 'Exotic']
    },
    {
        'text': 'What purpose should the plant serve?',
        'options': ['Decorative', 'Air Purification', 'Edible', 'Multipurpose']
    },
    {
        'text': 'What is the typical temperature of the room?',
        'options': ['Cold', 'Cool', 'Moderate', 'Warm', 'Hot']
    },
    {
        'text': 'What is the humidity level in the room?',
        'options': ['Low', 'Medium', 'High']
    },
]
 
for question_data in plant_questions: 
    question, created = Question.objects.get_or_create(text=question_data['text'])
 
    if not created:
        question.options.all().delete()    
        
    for option_text in question_data['options']:
        Option.objects.create(question=question, text=option_text)