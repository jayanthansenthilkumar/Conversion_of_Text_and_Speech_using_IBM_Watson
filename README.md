
# IBM Watson Tools

IBM Watson Tools is a Python package that provides easy-to-use functionality for **Text-to-Speech (TTS)** and **Speech-to-Text (STT)** using IBM Watson APIs. This package allows you to convert text into speech and transcribe audio files back to text.

---

## Features
- **Text-to-Speech:** Convert any given text into an audio file using IBM Watson's Text-to-Speech API.
- **Speech-to-Text:** Transcribe audio files into text using IBM Watson's Speech-to-Text API.
- Modular structure for easy integration and reusability.

---

## Prerequisites
- Python 3.7 or higher
- IBM Watson Text-to-Speech and Speech-to-Text services API keys and service URLs

---

## Installation

1. Clone the repository or download the code:
   ```bash
   git clone https://github.com/your-repository/ibm-watson-tools.git
   cd ibm-watson-tools
   ```

2. Install the required dependencies:
   ```bash
   pip install ibm-watson ibm-cloud-sdk-core
   ```

---

## Package Structure
```
ibm_watson_tools/
├── __init__.py           # Package initializer
├── api.py                # Integrating YOUR_API_KEY
├── text_to_speech.py     # Text-to-Speech functionality
├── speech_to_text.py     # Speech-to-Text functionality
├── main.py               # Main script for demonstration
├── README.md             # Documentation
```

---

## api.py
To avoid hardcoding sensitive API keys, consider using environment variables. You can set the API keys and service URLs like this:
```bash
export TTS_API_KEY="your-tts-api-key"
export TTS_SERVICE_URL="your-tts-service-url"
export STT_API_KEY="your-stt-api-key"
export STT_SERVICE_URL="your-stt-service-url"
```

Then, access them in your code:
```python
import os
TTS_API_KEY = os.getenv('TTS_API_KEY')
TTS_SERVICE_URL = os.getenv('TTS_SERVICE_URL')
```

---

## Dependencies
- [ibm-watson](https://pypi.org/project/ibm-watson/)
- [ibm-cloud-sdk-core](https://pypi.org/project/ibm-cloud-sdk-core/)

## Author
Jayanthan Senthilkumar

