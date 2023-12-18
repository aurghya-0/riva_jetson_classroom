# Project Name: ClassNotesGenerator

## Overview
The ClassNotesGenerator is a project aimed at revolutionizing the way students take notes in class by automating the process of transcribing, summarizing, and organizing class lectures. It leverages cutting-edge technologies, including OpenAI Whisper for voice transcription and OpenAI GPT-4.0 or Google Gemini for language modeling, to create concise and informative class notes.

## Features
- **Voice Transcription:** Utilize OpenAI Whisper or Nvidia Riva for accurate and efficient transcription of teacher lectures recorded in voice format.
- **Language Modeling:** Leverage the power of OpenAI GPT-4.0 or Google Gemini to process the transcriptions, providing advanced language understanding and context-aware summarization.
- **Summarization:** Automatically generate summaries of class lectures, distilling key information and concepts for efficient review.
- **Topic Extraction:** Identify and extract important topics from the summarized content to create a collection of organized class notes.
- **User-Friendly Interface:** Develop an intuitive and user-friendly interface for easy interaction and customization.
- **MongoDB Integration:** Store and manage class notes data efficiently using MongoDB.

## Getting Started
Follow these steps to get started with the ClassNotesGenerator project:

### Prerequisites
- Python 3.9 or higher
- Pip package manager

### Installation
```bash
pip install -r requirements.txt
```

### Usage
1. Record a teacher's lecture in voice format (supported formats: MP3, WAV).
2. Run the transcription module:
   ```bash
   python main.py
   ```

## Done
- [x] Record audio
- [x] Transcribe
- [x] LLM Summarization
- [x] Class Note Generation
- [x] MongoDB Integration

## TODO
- [ ] NVIDIA Riva Integration
- [ ] Real-time transcription presentation
- [ ] Record audio more efficiently

## Contributing
We welcome contributions from the community to enhance and expand the capabilities of the ClassNotesGenerator. Feel free to open issues, submit pull requests, or provide feedback.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- The developers and contributors of OpenAI Whisper, GPT-4.0, and Google Gemini for their pioneering work in language processing technologies.

Happy learning with ClassNotesGenerator! 📚🤖