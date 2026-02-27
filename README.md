# Multilingual Translation Platform - PPT Content

## Title and Academic Details

- **Institution:** SRM Institute of Science & Technology, Deemed to be University u/s 3 of UGC Act, 1956
- **School/Department:** School of Computing, Department of Networking and Communications
- **Project Code:** 21CSP401L – Major Project / 21CSP402L + 21CSP403L – Major Project + Internship
- **Project Title:** Multilingual Translation Platform with Speech, OCR, and Government Scheme Integration
- **Guide:** Dr. Subha K. J (Assistant Professor, Department of NWC)
- **Batch ID:** 21
- **Students:**

---

## Abstract

This project presents a web-based multilingual translation platform that supports 13 Indian languages and English. The system accepts text, image, and audio as input, and performs translation using the Facebook NLLB-200 distilled model. For image input, OCR is used to extract text, and for audio input, speech-to-text is used before translation. The platform also provides text-to-speech output for translated content in supported languages. In addition, it includes multilingual government scheme information access to improve public service usability. All translation activity is logged into an SQLite database for history tracking and analysis. The overall system is designed to reduce language barriers, improve accessibility, and provide a practical AI-powered tool for real-world users.

---

## Objectives

- Build an end-to-end multilingual translation system for text, image, and audio inputs.
- Support Indian regional languages and English using the NLLB translation model.
- Integrate OCR for extracting text from uploaded images.
- Integrate speech-to-text for handling voice/audio-based input.
- Provide text-to-speech output for translated results.
- Include multilingual government scheme information retrieval.
- Store translation history and metadata for analysis using SQLite.
- Provide a simple and user-friendly web interface.

---

## Introduction

Language diversity in India creates communication challenges in digital platforms, especially for users accessing services in non-English languages. Most existing translation tools focus mainly on text and provide limited support for Indian regional languages, image-based text, and audio-based queries. This project addresses these gaps by building a unified multilingual translation platform. The system uses NLLB for neural machine translation, OCR for image text extraction, and speech recognition for audio input processing. It also offers text-to-speech output and multilingual government scheme access. By combining these modules in a single workflow, the platform improves accessibility, inclusivity, and ease of information access.

---

## Literature Survey

| Ref | Title | Contribution | Relevance | Gap |
|---|---|---|---|---|
| [1] | NLLB: No Language Left Behind (Meta AI, 2022) | Large-scale multilingual translation model | Strong base for Indian language translation | Does not provide full multimodal pipeline |
| [2] | OCR for Indian Scripts (Elsevier/IEEE papers) | Script-aware OCR approaches for Indic text | Supports image input translation | Accuracy varies by image quality/script complexity |
| [3] | Speech Recognition for Low-Resource Indian Languages | Improves STT for regional languages | Enables audio-based translation | Noise robustness and accent handling remain issues |
| [4] | gTTS / Multilingual TTS systems | Text-to-speech generation across languages | Useful for accessibility and output playback | Not all Indian languages equally supported |
| [5] | End-to-end AI Translation Platforms (industry studies) | Unified user-facing translation solutions | Validates integrated architecture need | Often cloud-locked, costly, and less customizable |

---

## Problem Statement

- Existing tools often do not provide complete support for Indian regional languages.
- Most systems handle only text and do not support seamless image/audio translation in one interface.
- Government information is often unavailable in user-preferred language, reducing accessibility.
- Users need a low-cost, practical system that integrates translation, OCR, STT, TTS, and history logging.

---

## Proposed Methodology

### 1. User Input Layer
- User submits text, image, or audio through a web interface.

### 2. Preprocessing Layer
- Text input: direct pipeline.
- Image input: OCR extracts text.
- Audio input: speech-to-text converts voice to text.

### 3. Language Detection & Translation
- Source language is identified.
- NLLB model translates source text into selected target language.

### 4. Output Generation
- Translated text is displayed to user.
- Optional text-to-speech converts output text to audio.

### 5. Government Schemes Module
- Scheme data is fetched and translated for multilingual accessibility.

### 6. Logging & Storage
- Translation requests/results and metadata are stored in SQLite for history and analytics.

---

## Software and Tools Used

- **Python 3.10** - Core development language
- **Flask** - Backend web framework
- **Flask-SQLAlchemy** - ORM for database operations
- **SQLite** - Primary database for translation logs/history
- **Transformers (Hugging Face)** - NLLB model loading and inference
- **facebook/nllb-200-distilled-600M** - Translation model
- **Tesseract OCR / EasyOCR** - Image text extraction
- **SpeechRecognition / Whisper (as configured)** - Audio-to-text
- **gTTS** - Text-to-speech output
- **OpenCV / Pillow** - Image handling utilities
- **GitHub** - Version control and collaboration

---

## Architecture / Block Diagram Content

- **Client Layer:** Browser UI for entering text/uploading image/audio and selecting target language.
- **Application Layer (Flask):** Handles routes, request validation, translation orchestration, and response building.
- **AI Processing Layer:** OCR module, STT module, NLLB translation engine, and TTS module.
- **Data Layer:** SQLite database stores translation logs and history.
- **Information Layer:** Government schemes module provides multilingual scheme content.
- **End-to-End Flow:** User Input -> Preprocessing (OCR/STT) -> Translation (NLLB) -> Optional TTS -> Response + Log Storage.

---

## Project Timeline (Agile Phases)

### Phase 1: Planning & Requirement Analysis
- Define use cases, language scope, and architecture.
- Finalize tools, model, and database setup.

### Phase 2: Development Sprint
- Build Flask UI and backend routes.
- Integrate translation, OCR, STT, and TTS modules.
- Add scheme APIs and language mapping.

### Phase 3: Testing & Validation
- Unit testing for core functions.
- Integration testing for complete pipeline.
- Functional testing for multilingual outputs and edge cases.

### Phase 4: Review & Deployment
- Bug fixes and UI refinements.
- Documentation and project demo.
- Final report and presentation preparation.

---

## Results / Expected Outcomes

- Successful multilingual translation for text, image, and audio inputs.
- Improved accessibility through speech output and local-language support.
- Better public information reach through multilingual scheme module.
- Reliable history tracking using SQLite logs.
- Practical, modular architecture suitable for future scaling.

---

## Future Enhancements

- Add more Indian and foreign language pairs.
- Improve STT/OCR robustness for noisy real-world inputs.
- Add user login and personalized translation history.
- Migrate to scalable cloud database if required.
- Add mobile-friendly UI and offline inference options.

---

## Conclusion

The project demonstrates a practical AI-powered multilingual translation platform that combines translation, OCR, speech recognition, text-to-speech, and government scheme accessibility in one system. By using NLLB and a modular Flask architecture with SQLite logging, it provides an effective and user-centric solution for reducing language barriers. The system is extensible and can be further enhanced for broader deployment and real-world impact.

---

## References

1. NLLB Team (Meta AI), *No Language Left Behind: Scaling Human-Centered Machine Translation*, 2022.
2. Hugging Face Transformers Documentation, model inference and tokenization references.
3. Flask Documentation, web framework and routing.
4. SQLAlchemy Documentation, ORM and SQLite integration.
5. Tesseract OCR Documentation.
6. SpeechRecognition / Whisper documentation for speech-to-text systems.
7. gTTS Documentation, multilingual text-to-speech.
8. Recent IEEE/Elsevier papers on Indic OCR and low-resource multilingual NLP.

---

## Download Model Weights

This repository requires a large model file that cannot be stored on GitHub.

1. Download `pytorch_model.bin` from [Google Drive link here](https://drive.google.com/file/d/1gYF0sLhNv7_9P4hpzPPli0tANkmmQl9I/view?usp=sharing).
2. Place it in the folder: `models/facebook/nllb-200-distilled-600M/`.

### Optional: Download Automatically with gdown

If you have [gdown](https://github.com/wkentaro/gdown) installed, run:

```sh
gdown --id 1gYF0sLhNv7_9P4hpzPPli0tANkmmQl9I -O models/facebook/nllb-200-distilled-600M/pytorch_model.bin
```

If you don't have gdown:

```sh
pip install gdown
```

**Note:** Ensure `models/facebook/nllb-200-distilled-600M/pytorch_model.bin` is listed in `.gitignore` so it is not tracked by git.