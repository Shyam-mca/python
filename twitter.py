import re
import nltk
nltk.download('twitter')
def remove_username_handles(text):
    pattern = r'@\w+'
    cleaned_text = re.sub(pattern, '',text)
    return cleaned_text
text = "hii im @shyam devi..."
cleaned_text = remove_username_handles(text)
print("Original Text:",text)
print("\nCleaned Text:",cleaned_text)

