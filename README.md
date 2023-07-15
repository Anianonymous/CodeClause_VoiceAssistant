# Voice Assistant using Python
## Introduction
This is a Python-based personal voice assistant application. 
It allows users to interact with their computer using voice commands for various tasks such as web searching, opening websites, 
retrieving the date and time, and searching Wikipedia and more.

## Requirements
The following packages are required to run the Voice Assistant:

* speech_recognition
* pyttsx3
* webbrowser
* wikipedia

You can install these packages using the following command:

```python 
pip install speech_recognition pyttsx3 webbrowser wikipedia
```

## Usage

1. Install the required Python libraries mentioned above using pip or conda.
2. Clone the repository or download the project files.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command to start the Streamlit app:
```python
streamlit run VoiceAssistant.py
```
6. The Streamlit app will launch in your default web browser.
7. Click the "Start Listening" button to activate the voice recognition feature.
8. Say a command or ask a question aloud, and the app will convert your speech into text.
9. Depending on the command or question, the app will perform the corresponding action, such as web searching, opening a website, retrieving 
   the date and time, or searching Wikipedia.
10. Additional features can be accessed by expanding the "Additional Features" section within the app interface.

## Features
Speech recognition: Converts spoken words into text using the speech_recognition library.
Text-to-speech: Utilizes the pyttsx3 library to convert text into speech for auditory feedback.
Web searching: Searches the web using the pywhatkit library based on user input.
Website opening: Opens websites in the default web browser using the webbrowser library.
Date and time retrieval: Retrieves the current date and time using the datetime library.
Wikipedia search: Searches Wikipedia and displays a summary using the wikipedia library.

## Requirements
Python 3.7 or higher
Required Python libraries: speech_recognition, streamlit, pywhatkit, pyttsx3, os, webbrowser, datetime, wikipedia

## Conclusion
This Voice Assistant is a simple example of how to build a voice-controlled application using Python. You can extend the functionality of the Voice Assistant as per your requirements. Feel free to customize the code in your python file to add more features or modify the existing ones according to your requirements. You can explore the functions within the VoiceAssistant.py file to understand the implementation details and make necessary changes.


https://github.com/Anianonymous/CodeClause_VoiceAssistant/assets/105560839/88fe854d-eac6-4e5a-a3eb-bbcc3aab5045


