    from transformers import MarianMTModel, MarianTokenizer

    # Initialize the model and tokenizer
    model_name = 'Helsinki-NLP/opus-mt-en-fr'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Translate function
    def translate_text(text):
        inputs = tokenizer(text, return_tensors="pt", padding=True)
        translated = model.generate(**inputs)
        return tokenizer.decode(translated[0], skip_special_tokens=True)

    # Example usage
    text = "To portray a man fighting for justice as a criminal, the criminals themselves must rewrite justice!"
    translated_text = translate_text(text)
    print(f"Original: {text}")
    print(f"Translated: {translated_text}")

