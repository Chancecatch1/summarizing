import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

def summarize_korean_text(text, model, tokenizer, max_length=150):
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True, padding="max_length")
    input_ids = inputs["input_ids"].to(device)
    attention_mask = inputs["attention_mask"].to(device)

    outputs = model.generate(input_ids, attention_mask=attention_mask, max_length=max_length, num_return_sequences=1)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return summary

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def split_text(text, chunk_size=1000):
    words = text.split()
    chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load the pre-trained Pegasus-XSUM model and tokenizer
    model_name = "google/pegasus-xsum"
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    model = PegasusForConditionalGeneration.from_pretrained(model_name)
    model.to(device)

    input_file_path = "marco_job_abroad.txt"  # Replace with your input file path
    output_file_path = "output_marco_job_abroad.txt"  # Replace with your desired output file path

    long_text = read_file(input_file_path)

    # Split the long text into smaller chunks
    chunks = split_text(long_text, chunk_size=1000)

    summarized_chunks = []
    for chunk in chunks:
        summary = summarize_korean_text(chunk, model, tokenizer)
        summarized_chunks.append(summary)

    # Combine the summarized chunks
    full_summary = " ".join(summarized_chunks)

    write_file(output_file_path, full_summary)

    print("Original Text:\n", long_text)
    print("\nSummarized Text:\n", full_summary)
