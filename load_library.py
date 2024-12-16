import pandas as pd
from shop.models import Plant
from library.models import PlantLibrary   
 
df = pd.read_excel('library_data.xlsx')
 
for index, row in df.iterrows():
    try:         
        plant = Plant.objects.get(common_name=row['Plant'])   
         
        PlantLibrary.objects.create(
            plant=plant,
            information=row['Information']
        )
        print(f"Library entry for '{row['Plant']}' added successfully.")
    except Plant.DoesNotExist:
        print(f"Plant '{row['Plant']}' not found. Skipping entry.")
    except Exception as e:
        print(f"Error adding library entry for '{row['Plant']}': {e}")
