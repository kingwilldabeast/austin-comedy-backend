
import os
import pandas as pd
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comedy_django.settings')
django.setup()

# Import your models
from comedy_app.models import open_mic

# Clear the table before populating
open_mic.objects.all().delete()

# Load the Excel file
file_path = '/Users/willisenberg/Downloads/mics.xlsx'
df = pd.read_excel(file_path)

# Iterate over rows and create database entries
for index, row in df.iterrows():
    # Assuming your model has 'name', 'age', and 'email' fields
    open_mic.objects.create(
        weekday=row['Weekday'],
        name=row['Name'],
        start_time=row['Time'],
        venue=row['Venue'],
        address=row['Address'],
        host=row['Host'],
        ig_link=row['Instagram'],
        link=row['Link'],
        frequency=row['Frequency'],
        notes=row['Notes'],
    )

print("Database populated successfully!")
