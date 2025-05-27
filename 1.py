import re

# Sample text to work with
text = "My email is example123@gmail.com and my phone number is 987-654-3210. Visit https://example.com"

# 1. Search for an email address
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email_match = re.search(email_pattern, text)
if email_match:
    print("Email found:", email_match.group())
else:
    print("No email found.")

# 2. Find all phone numbers (format: xxx-xxx-xxxx)
phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
phones = re.findall(phone_pattern, text)
print("Phone numbers found:", phones)

# 3. Match a URL
url_pattern = r'https?://[^\s]+'
url_match = re.search(url_pattern, text)
if url_match:
    print("URL found:", url_match.group())

# 4. Replace email with a placeholder
clean_text = re.sub(email_pattern, "[EMAIL]", text)
print("Text after email redaction:", clean_text)

# 5. Check if the text starts with "My"
if re.match(r'^My', text):
    print("Text starts with 'My'")

# 6. Split text by spaces or punctuation
tokens = re.split(r'[,\s.]+', text)
print("Tokens:", tokens)
