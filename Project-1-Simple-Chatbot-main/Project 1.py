import random
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from difflib import get_close_matches

# Ensure necessary NLTK resources are available
def ensure_nltk_resources():
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('punkt')
        nltk.download('stopwords')

ensure_nltk_resources()

class SimpleChatbot:
    def __init__(self):
        self.context_history = []

    def greet(self):
        return "Hello! I'm your friendly chatbot. How can I assist you today?"

    def basic_questions(self, question):
        responses = {
            "how are you": ["I'm doing well, thank you!", "Feeling good, thanks for asking!"],
            "what's your name": ["I'm just a humble chatbot, no name needed!", "I'm your virtual assistant, no name required."],
            "what is your name": ["I'm just a humble chatbot, no name needed!", "I'm your virtual assistant, no name required."],
            "where are you from": ["I exist in the digital realm, so I'm everywhere and nowhere!", "I'm from the depths of the internet."],
            "what can you do": ["I can help answer your questions and assist you with simple tasks!", "I'm here to chat and provide information."],
            "who created you": ["I was created by a team of developers.", "My creators are brilliant minds from the tech world!"]
        }

        question_cleaned = re.sub(r'[^\w\s]', '', question.lower())  # Remove punctuation and convert to lowercase
        closest_match = get_close_matches(question_cleaned, responses.keys(), n=1, cutoff=0.5)
        if closest_match:
            return random.choice(responses[closest_match[0]])
        return "I'm sorry, I don't know how to respond to that."

    def farewell(self):
        return "Goodbye! Have a great day."

    def preprocess_input(self, user_input):
        # Remove punctuation and convert to lowercase
        user_input_cleaned = re.sub(r'[^\w\s]', '', user_input.lower())
        # Tokenize the input
        tokens = word_tokenize(user_input_cleaned)
        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words]
        return filtered_tokens, user_input_cleaned

    def handle_input(self, user_input):
        tokens, user_input_cleaned = self.preprocess_input(user_input)
        self.context_history.append(("User", user_input))

        if any(greeting in tokens for greeting in ['hello', 'hi', 'hey']):
            return self.greet()
        elif 'bye' in tokens:
            return self.farewell()
        elif any(q in user_input_cleaned for q in ["how are you", "what's your name", "what is your name", "where are you from", "what can you do", "who created you"]):
            response = self.basic_questions(user_input)
            self.context_history.append(("Bot", response))
            return response
        elif 'recall context' in user_input_cleaned:
            return self.recall_context()
        else:
            if 'name' in tokens and 'my' in tokens:
                name = user_input.split()[-1].capitalize()
                response = f"Nice to meet you, {name}!"
                self.context_history.append(("Bot", response))
                return response
            else:
                return "I'm sorry, I didn't quite understand that. Can you please rephrase?"

    def recall_context(self):
        context_str = "Here's what we talked about so far:\n"
        for entry in self.context_history:
            context_str += f"{entry[0]}: {entry[1]}\n"
        return context_str

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    print(chatbot.greet())
    while True:
        user_input = input().strip()
        if user_input.lower() == 'bye':
            print(chatbot.farewell())
            break
        else:
            print(chatbot.handle_input(user_input))
