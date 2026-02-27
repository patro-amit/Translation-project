# Architecture Content

## A. Application

### 1. Microservices
- Microservices split the system into independent services such as `Translation Service`, `OCR Service`, `STT Service`, `TTS Service`, `Schemes Service`, and `History Service`.
- Each service can be developed, deployed, and scaled independently.
- Best suited when request volume is high, multiple teams work in parallel, and separate scaling is required.
- Trade-offs: higher operational complexity (API gateway, service discovery, distributed logging, monitoring, retries, circuit breakers).

**Suitability for this project**
- Good as a future evolution path.
- Not the best immediate choice for current academic scope because the workflow is tightly coupled and synchronous.

### 2. Event-Driven
- Event-driven architecture uses events and asynchronous communication between producers and consumers.
- Typical events: `FileUploaded`, `TextExtracted`, `TranslationCompleted`, `TTSCreated`, `LogWritten`.
- Improves decoupling and resilience for long-running/background tasks.
- Useful for non-blocking pipelines and high-throughput processing.

**Suitability for this project**
- Good for future enhancement (batch translation, retries, analytics pipelines).
- Not ideal as first architecture because it adds broker setup, event contracts, ordering/idempotency, and debugging complexity.

### 3. Serverless
- Serverless runs logic as functions (for example, API functions for translate, OCR, history).
- Benefits: automatic scaling, low idle cost, fast initial deployment.
- Limitations for AI workloads: cold starts, model loading overhead, memory/runtime constraints, vendor dependency.

**Suitability for this project**
- Useful for lightweight endpoints (history, schemes).
- Less suitable for heavy inference paths (NLLB/OCR/STT) unless using specialized managed AI endpoints.

**Recommended application choice (current phase)**
- A modular monolithic web app is the most practical now.
- It offers lower complexity, easier demo/testing, and better control of in-process AI workflow.

---

## B. Database

### 1. ER Diagram (content)
- Entity: `TranslationLog`
  - `id` (Primary Key, Integer)
  - `timestamp` (DateTime)
  - `input_type` (String: `text` | `ocr` | `audio`)
  - `source_language` (String)
  - `target_language` (String)
  - `original_text` (Text)
  - `translated_text` (Text)
  - `error_message` (Text, Nullable)

**Relationships**
- Current design has a single core entity for logging translation activity.
- Future extension can add `Device`, `User`, and `TranslationRequest` entities with one-to-many relationships.

### 2. Schema Design
- Table: `translation_log`
- Key design choices:
  - Keep `input_type`, `source_language`, `target_language` non-null for analytics.
  - Keep text fields flexible (`TEXT`) to support varying lengths.
  - Keep `error_message` nullable to store failure details without breaking flow.
- Suggested indexes:
  - `timestamp DESC` for recent-history queries.
  - `(source_language, target_language)` for language-pair analysis.
  - `input_type` for feature usage analytics.

---

## C. Data Exchange Contract

### 1. Frequency of data exchanges
- Translation requests: real-time, per user action.
- TTS generation: on-demand, per playback click/request.
- History retrieval: on page load or user refresh.
- Schemes retrieval: on-demand, optionally cached at client side.
- File processing (image/audio): per file upload event.

### 2. Data Sets
- Request metadata: `device_id` (if used), timestamp, input type.
- Translation input:
  - Text input directly, or extracted text from image/audio.
  - Source language (detected/provided), target language (selected).
- Translation output:
  - `translated_text`, status flags, error details if failed.
- TTS output:
  - Language code and generated audio stream.
- Log dataset:
  - input type, source/target language, original text, translated text, timestamp, error.

### 3. Mode of Exchanges (API, File, Queue etc.)
- **API (REST/JSON):** primary mode for instant translation, schemes, and history endpoints.
- **File exchange (multipart/form-data):** image/audio uploads for OCR/STT pipeline.
- **Binary stream:** audio response for TTS playback.
- **Database exchange (SQL/ORM):** persistent log storage and query.
- **Queue (optional future):** for async OCR/STT/translation jobs and retry workflows if scaling needs increase.
