import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the saved model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("t5-large")
tokenizer = T5Tokenizer.from_pretrained("t5-large")

def abstractive_summarization(text):
    # Tokenize the input text
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    l=len(text)
    # Generate summary
    summary_ids = model.generate(inputs, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    # Decode summary tokens back to text
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# example_text = "In continuation with the centennial celebrations of Admiral RL Pereira, PVSM, AVSM (1923-1993), the Indian Navy and St Joseph’s School (North Point), Darjeeling jointly conducted commemorative events at the school campus on 15 March 24.  Admiral Pereira, fondly known as ‘Ronnie P’, rose to become the 9th Chief of the Naval Staff in 1979, was an alumnus of the School between 1932-37. The school celebrated the Admiral’s memory by conducting Football tournament and essay writing competition. The occasion was marked with festivities at the school and a team of officers from Naval Headquarters joined the celebrations. Cdr Anup Thomas spoke about the life and times of Admiral Pereira and Cdr Gurbir Singh provided an overview of the maritime history of India and exciting career opportunities in the Navy to a gathering of over 800 students. The visiting officers also interacted with the students & faculty and answered their queries about career avenues in Indian Navy. On this occasion, the Indian Navy also instituted a ‘Rolling Sports Trophy’ and scholarship in memory of the Admiral by presenting a cheque of Rs 2.5 lakhs to the school. The visiting officers and the faculty also planted a tree in memory of Admiral RL Pereira. Father Stanley Varghese, Principal and Rector of the school felicitated the visiting Naval officers.In continuation with the centennial celebrations of Admiral RL Pereira, PVSM, AVSM (1923-1993), the Indian Navy and St Joseph’s School (North Point), Darjeeling jointly conducted commemorative events at the school campus on 15 March 24.  Admiral Pereira, fondly known as ‘Ronnie P’, rose to become the 9th Chief of the Naval Staff in 1979, was an alumnus of the School between 1932-37. The school celebrated the Admiral’s memory by conducting Football tournament and essay writing competition. The occasion was marked with festivities at the school and a team of officers from Naval Headquarters joined the celebrations. Cdr Anup Thomas spoke about the life and times of Admiral Pereira and Cdr Gurbir Singh provided an overview of the maritime history of India and exciting career opportunities in the Navy to a gathering of over 800 students. The visiting officers also interacted with the students & faculty and answered their queries about career avenues in Indian Navy. On this occasion, the Indian Navy also instituted a ‘Rolling Sports Trophy’ and scholarship in memory of the Admiral by presenting a cheque of Rs 2.5 lakhs to the school. The visiting officers and the faculty also planted a tree in memory of Admiral RL Pereira. Father Stanley Varghese, Principal and Rector of the school felicitated the visiting Naval officers."

# # Generate summary
# summary = abstractive_summarization(example_text)
# print("Original Text:\n", example_text)
# print("\nAbstractive Summary:\n", summary)
