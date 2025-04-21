# Flasher

A streamlined interactive flashcard application designed for language learning and knowledge retention.

## Overview

Flasher is a web-based flashcard application built with Streamlit that helps users learn vocabulary and concepts through interactive cards. While the current implementation focuses on language learning (particularly Spanish), the application is designed to be flexible for any type of flashcard content.

## Features

- Interactive flashcard interface with immediate feedback
- Support for multiple acceptable answers per question
- Visual rewards for correct answers
- Audio pronunciation links where available
- Tag-based organization system (language, book, chapter, section)
- Simple and intuitive user interface

## Installation

### Prerequisites

- Python 3.9+
- pip (Python package manager)

### Local Setup

1. Clone the repository:
   ```
   git clone https://github.com/ericmelz/flasher.git
   cd flasher
   ```

2. Set up a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   cd src
   streamlit run Home.py
   ```

### Docker Setup

Alternatively, you can run the application using Docker:

1. Build the Docker image:
   ```
   docker build -t flasher .
   ```

2. Run the container:
   ```
   docker run -p 9999:9999 flasher
   ```

3. Access the application at http://localhost:9999

## Usage

1. Open the application in your web browser
2. Read the question displayed on the screen
3. Type your answer in the input field
4. Click "Submit" to check your answer
5. Review feedback and the correct answer if needed
6. Click "Next" to proceed to the next flashcard

## Data Structure

Flashcards are stored in `data/flashcards.json` with the following structure:

```json
{
  "question": "What is the English word for 'palabra'?",
  "answers": ["word"],
  "audio_url": "https://example.com/audio/palabra.mp3",
  "tags": {
    "language": "Spanish",
    "book": "Learning Spanish",
    "chapter": 1,
    "section": 2
  }
}
```

## Customization

You can add your own flashcards by editing the `data/flashcards.json` file or by implementing a new data provider in the application.

## License

This project is licensed under the terms of the license included in the repository.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
