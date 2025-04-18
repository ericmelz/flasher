I am uploading a transcript of Chapter 3 of Learn Spanish.  This
transcript was created using otter.ai, which is a speech-to-text tool.
Many of the spellings rendered by the tool are not correct and need
correction.  This is particularly true for spanish.

For example:
* The spanish word "Qué" might be rendered in the transcription as "K".
* The spanish word "en" might be rendered in the transcription as "en".

Use your knowledge of spanish to generate correct pairs of (English, Spanish)
words.  In addition, render the third round of words in JSON format
resembling the example below.  Output empty strings ("") for the audio_url,
since you don't know them.  The section number should correspond to
the count of the round.  For example, the second round should be
represented as { ... "section": 2 } in the json.


Example JSON:
```

[
  {
    "question": "What is the English word for **Qué**?",
    "answers": [
      "who",
      "that"
    ],
    "audio_url": "https://otter.ai/s/OdM_-M9bRL-US3jFIDjExQ?snpt=true",
    "tags": {
      "language": "Spanish",
      "book": "Learning Spanish",
      "chapter": 3,
      "section": 1
    }
  },
  {
    "question": "¿Cómo se dice **that** en español??",
    "answers": [
      "qué"
    ],
    "audio_url": "https://otter.ai/s/OdM_-M9bRL-US3jFIDjExQ?snpt=true",
    "tags": {
      "language": "Spanish",
      "book": "Learning Spanish",
      "chapter": 3,
      "section": 1
    }
  },
  {
    "question": "¿Cómo se dice **who** en español??",
    "answers": [
      "qué"
    ],
    "audio_url": "https://otter.ai/s/OdM_-M9bRL-US3jFIDjExQ?snpt=true",
    "tags": {
      "language": "Spanish",
      "book": "Learning Spanish",
      "chapter": 3,
      "section": 1
    }
  },
  {
    "question": "What is the English word for **y**?",
    "answers": [
      "and"
    ],
    "audio_url": "https://otter.ai/s/QEgfZYJkRDaVmGkK2LSS_A?snpt=true",
    "tags": {
      "language": "Spanish",
      "book": "Learning Spanish",
      "chapter": 3,
      "section": 1
    }
  },
  {
    "question": "¿Cómo se dice **and** en español??",
    "answers": [
      "y"
    ],
    "audio_url": "https://otter.ai/s/QEgfZYJkRDaVmGkK2LSS_A?snpt=true",
    "tags": {
      "language": "Spanish",
      "book": "Learning Spanish",
      "chapter": 3,
      "section": 1
    }
  },
  {
    "question": "What is the English word for **o**?",
    "answers": [
      "or"
    ],
    "audio_url": "https://otter.ai/s/rHR7fmR7QpmJ9Zn8XKKD_g?snpt=true",
    "tags": {
      "language": "Spanish",
      "book": "Learning Spanish",
      "chapter": 3,
      "section": 1
    }
  }
]
```