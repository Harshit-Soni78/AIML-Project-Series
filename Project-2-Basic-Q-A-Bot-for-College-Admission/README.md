# Basic Q & A Bot for College Admission

## Project Overview

This project is a Basic Q & A Bot specifically designed to assist with college admission-related queries. The chatbot can answer questions regarding admission procedures, requirements, and deadlines, and it engages users in conversations to provide detailed and contextual responses. 

## Project Level

**Medium**

## Project Requirements

1. **Admission-Related Q&A**:
   - Develop a chatbot designed to answer questions related to college admission.
   - Include responses to queries about admission procedures, requirements, and deadlines.

2. **User Interaction**:
   - Create a flow where the chatbot engages the user in a conversation about their admission queries.
   - Allow the user to ask multiple questions in a single session.

3. **Contextual Understanding**:
   - Enhance the chatbot's ability to understand context by remembering information from previous interactions.
   - Implement a mechanism for the chatbot to provide more personalized responses.

4. **Connection to Backend (Optional)**:
   - Integrate the chatbot with a backend system to fetch real-time admission-related information.
   - Ensure the chatbot responses are up-to-date and accurate.

5. **Error Handling and Feedback**:
   - Implement robust error handling for cases where the chatbot encounters queries it cannot answer.
   - Provide users with helpful feedback when their queries cannot be addressed.


## Installation and Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Step-by-Step Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/AIML-Project-Series.git
   cd AIML-Project-Series

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows, use `venv\Scripts\activate`

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt

4. **Download NLTK data**:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')


### Running the Chatbot

1. **Train the model**:
   ```bash
   python train_bot.py

2. **Start the chat GUI**:
   ```bash
   python chatgui.py


## Project Structure

1. **train_bot.py**:
   - Script to train the chatbot model.

2. **chatgui.py**:
   - Script to run the chatbot GUI.

3. **admission_data.json**:
   - JSON file containing intents and responses.

4. **words.pkl**:
   - Pickle file storing the words for the model.

5. **classes.pkl**:
   - Pickle file storing the classes for the model.

6. **chatbot_model.h5**:
   - Trained chatbot model.


.
├── admission_data.json        # Dataset for training the chatbot
├── train_bot.py               # Script to train the chatbot model
├── chatgui.py                 # Script to run the chatbot GUI
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── model                      # Directory to save the trained model and related files
│   ├── chatbot_model.h5       # Trained chatbot model
│   ├── classes.pkl            # Pickled classes
│   ├── words.pkl              # Pickled words
└──────────────────────────────────────────────────────────────────────── 



## Features

1. **Interactive UI**:
   - A user-friendly interface built using Tkinter for chatting with the bot.

2. **Contextual Responses**:
   - The chatbot remembers the context of the conversation to provide relevant answers.

3. **Error Handling**:
   - Provides helpful feedback when queries cannot be addressed.


## Future Improvements

1. **Backend Integration**:
   - Connect the chatbot to a real-time database to fetch up-to-date admission information.

2. **Advanced NLP Techniques**:
   - Incorporate more sophisticated natural language processing techniques for better understanding and responses.

3. **Multi-turn Conversations**:
   - Improve the bot's ability to handle multi-turn conversations for more complex queries.


## Contact

**For any queries or issues, please contact harshit11664@gmail.com.**

