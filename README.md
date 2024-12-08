# NLP from Medical Records Project

## Overview
This project aims to extract valuable insights from unstructured medical records using natural language processing (NLP) techniques. We will focus on named entity recognition (NER) to identify medical terms, conditions, and treatments.

## Dataset
- **Source**: MIMIC-III Clinical Database
- **Content**: Contains de-identified clinical notes and medical records.

## Project Structure
- `data/`: Directory to store the dataset.
- `preprocess.py`: Script to preprocess and clean the text data.
- `ner_model.py`: Script to train an NER model using spaCy.
- `requirements.txt`: List of project dependencies.

## Hugging Face Integration
- The project now uses the `transformers` library from Hugging Face for Named Entity Recognition (NER).
- Utilizes the `biobert-base-cased-v1.1` model for processing biomedical text.

## Setup Instructions
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Download the MIMIC-III Clinical Database and place it in the `data/` directory.
4. Run `preprocess.py` to clean and prepare the text data.
5. Use `ner_model.py` to perform NER on medical records using the Hugging Face model.

## Future Work
- Experiment with different NLP models like BERT or BioBERT.
- Implement additional NLP tasks such as sentiment analysis or text summarization.

These updates enhance the project's capability to process and analyze medical records effectively.
