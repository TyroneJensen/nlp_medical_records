import os
import pandas as pd
import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Define paths
DATA_DIR = 'data/'
PROCESSED_DIR = 'processed_data/'
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Function to preprocess text data
def preprocess_text(text):
    # Use spaCy to process the text
    doc = nlp(text)
    # Extract tokens and lemmatize
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(tokens)

# Load dataset
# Assuming the dataset is in CSV format with a 'text' column
file_path = os.path.join(DATA_DIR, 'clinical_notes.csv')
data = pd.read_csv(file_path)

# Preprocess the text data
processed_texts = data['text'].apply(preprocess_text)

# Save processed data
processed_data_path = os.path.join(PROCESSED_DIR, 'processed_clinical_notes.csv')
processed_texts.to_csv(processed_data_path, index=False)
