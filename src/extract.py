import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text

def clean_and_count_words(text):
    #remove punctuation & special chars
    words = re.findall(r'\b\w+\b', text.lower())
    return words, len(words)

if __name__ == "__main__":
    pdf_path = "resume.pdf"  # file inside data folder
    text = extract_text_from_pdf(pdf_path)
    words, word_count = clean_and_count_words(text)

    print("\n--- Extracted Resume Text ---\n")
    print(text)

    print("\n--- Word Stats ---")
    print(f"Total words: {word_count}")
    print(f"Unique words: {len(set(words))}")

    print("\n--- All Words ---")
    print(words)  # prints the full list of words
