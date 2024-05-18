# Simple Chatbot

## Introduction
This project implements a simple chatbot using Python. The chatbot is capable of engaging in conversations with users by responding to greetings, answering basic questions, recalling previous interactions, and handling user inputs gracefully.

## Project Requirements
The project fulfills the following requirements:
1. **Basic Functionality:**
    - Implements a simple greeting function for the chatbot.
    - Allows the chatbot to respond to at least five basic questions.
    - Includes a farewell message.
2. **Previous Context:**
    - Implements a basic mechanism for the chatbot to remember previous interactions.
    - Ensures the chatbot can recall and reference the context of the conversation.
3. **User Interaction:**
    - Creates a flow where the chatbot asks the user at least three questions.
    - Allows the user to provide responses, and has the chatbot react accordingly.
4. **Error Handling:**
    - Implements basic error handling to address scenarios where the chatbot does not understand the user's input.
    - Provides a friendly response in such cases.

## Usage
To run the chatbot, execute the `SimpleChatbot.py` file. Follow the on-screen instructions to interact with the chatbot. You can input text and receive responses from the chatbot until you type "bye" to exit.

## Dependencies
The project requires the following dependencies:
- `nltk`: Natural Language Toolkit for text preprocessing.
- `difflib`: Library for comparing sequences.

## How It Works
The chatbot employs basic natural language processing techniques to tokenize and preprocess user input. It maintains a context history to recall previous interactions. Responses to user inputs are generated based on predefined patterns and closest matches to basic questions. Error handling is implemented to gracefully handle unknown inputs.

## Future Improvements
Possible enhancements for the chatbot include:
- Integration with external APIs for more advanced question answering.
- Implementing sentiment analysis for more nuanced responses.
- Adding support for multi-turn conversations and maintaining longer context histories.

## License
This project is licensed under the [MIT License](LICENSE).
