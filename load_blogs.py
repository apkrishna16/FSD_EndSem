import pandas as pd
from home.models import User   
from blogs.models import Blog

df = pd.read_excel('blog_data.xlsx')
 
for index, row in df.iterrows():
    try:
         
        author = User.objects.get(username=row['Author'])   
        
        Blog.objects.create(
            title=row['Title'],
            tagline=row['Tagline'],
            content=row['Content'],
            author=author
        )
        print(f"Blog '{row['Title']}' added successfully.")
    except User.DoesNotExist:
        print(f"User '{row['Author']}' not found. Skipping blog '{row['Title']}'.")
    except Exception as e:
        print(f"Error adding blog '{row['Title']}': {e}")
