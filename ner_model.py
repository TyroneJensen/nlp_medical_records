from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Load pre-trained model and tokenizer
model_name = "dmis-lab/biobert-base-cased-v1.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Create NER pipeline
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)

# Define training data
# Example format: text
TRAIN_DATA = [
    "Patient has diabetes and hypertension.",
    "Prescribed metformin for diabetes.",
    # Add more training examples here
]

# Example text for NER
example_text = "Patient has diabetes and hypertension. Prescribed metformin for diabetes."

# Perform NER
ner_results = ner_pipeline(example_text)

# Print results
for entity in ner_results:
    print(f"Entity: {entity['word']}, Label: {entity['entity']}")
