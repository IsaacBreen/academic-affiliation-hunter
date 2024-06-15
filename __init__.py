import gzip
import json
import os
from collections import defaultdict

import pandas as pd

# Define the path to the JSON files and the target institutions
data_path = './[Sample Dataset] April 2024 Public Data File from Crossref'
with open('target_institutions.txt', 'r') as f:
    target_institutions = f.read().splitlines()

# Initialize a dictionary to keep track of Australian academics and their scores
academic_scores = defaultdict(lambda: {'affiliation': '', 'score': 0})


# Function to check if an affiliation is an Australian institution
def is_australian_institution(affiliation_name):
    return 'Australia' in affiliation_name


# Loop through each file in the directory
for filename in os.listdir(data_path):
    if filename.endswith('.json.gz'):
        filepath = os.path.join(data_path, filename)
        with gzip.open(filepath, 'rt', encoding='utf-8') as file:
            data = json.load(file)
            for item in data.get('items', []):
                authors = item.get('author', [])

                for author in authors:
                    affiliations = author.get('affiliation', [])
                    for affiliation in affiliations:
                        affil_name = affiliation.get('name', '')
                        if is_australian_institution(affil_name):
                            full_name = f"{author['given']} {author['family']}"
                            academic_scores[full_name]['affiliation'] = affil_name
                            break

                for author in authors:
                    affiliations = author.get('affiliation', [])
                    for affiliation in affiliations:
                        affil_name = affiliation.get('name', '')
                        if any(target_institution in affil_name for target_institution in target_institutions):
                            for au_author in authors:
                                au_affiliations = au_author.get('affiliation', [])
                                for au_affiliation in au_affiliations:
                                    if is_australian_institution(au_affiliation.get('name', '')):
                                        full_name = f"{au_author['given']} {au_author['family']}"
                                        academic_scores[full_name]['score'] += 1
                                        break

# Convert the academic_scores dictionary to a pandas DataFrame
df = pd.DataFrame(
    [{'name': name, 'affiliation': info['affiliation'], 'score': info['score']}
     for name, info in academic_scores.items()]
    )

# Remove academics with score 0
df = df[df['score'] > 0]

# Sort the DataFrame by score in descending order
df = df.sort_values(by='score', ascending=False).reset_index(drop=True)

# Save the DataFrame to a CSV file
df.to_csv('australian_academics_scores.csv', index=False)

print("Done! The scores have been saved to 'australian_academics_scores.csv'.")
