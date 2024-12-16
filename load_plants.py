import csv
from shop.models import Plant  

 
csv_to_model_fields = {
    "Plant Name": "common_name",
    "Scientific Name": "scientific_name",
    "Light Requirements": "light_requirements",
    "Watering Frequency": "watering_frequency",
    "Maintenance Level": "maintenance_level",
    "Growth Rate": "growth_rate",
    "Preferred Climate": "preferred_climate",
    "Plant Size": "plant_size",
    "Allergy Concerns": "allergy_concerns",
    "Aesthetic Preference": "aesthetic_preference",
    "Purpose": "purpose",
    "Room Temperature": "room_temperature",
    "Humidity Level": "humidity_level",
    "Description": "description",
    "Image Path": "image_path",
}

 
csv_file_path = "plant_data_30.csv"

 
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader: 
        plant_data = {}
        for csv_field, model_field in csv_to_model_fields.items(): 
            if model_field == "allergy_concerns":
                plant_data[model_field] = True if row[csv_field].strip().lower() == "yes" else False
            else:
                plant_data[model_field] = row[csv_field].strip()
        
        plant, created = Plant.objects.update_or_create(
            common_name=plant_data["common_name"],
            defaults=plant_data
        )
    
        print(f"{'Created' if created else 'Updated'}: {plant.common_name}")
