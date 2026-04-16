# AgriTriage — Agriculture Support Intelligence Agent

Production-grade reactive triage agent for Agriculture communications.  
Built with **FastAPI** + **LangChain** + **Groq LLM** + **Vanilla HTML/CSS/JS**.
- 🐳 **Docker Ready**: Easy deployment with Docker and Docker Compose.
---

## 🏗️ Project Architecture

```
agri_triage/
├── backend/
│   ├── __init__.py
│   ├── main.py        # FastAPI app + CORS
│   ├── routes.py      # POST /api/triage, GET /api/health
│   ├── agent.py       # LangChain chains (classify → NER → draft → summary)
│   └── models.py      # Pydantic schemas
├── frontend/
│   ├── index.html       # Clean, reactive dashboard UI
│   ├── style.css        # Premium dark industrial aesthetic
│   └── app.js           # Client-side logic & API integration
├── Dockerfile           # Multi-stage build for production
├── docker-compose.yml   # Orchestration for local development
├── run.py               # Uvicorn helper script
└── pyproject.toml       # uv / pip dependency configuration
```

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.11+](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv) (Recommended) or `pip`
- [Docker](https://www.docker.com/) (Optional, for containerized setup)
- **Groq API Key**: Get one for free at [console.groq.com](https://console.groq.com)

### Installation

1. **Clone the repository** (or download the source):
   ```bash
   git clone https://github.com/your-username/agri-triage.git
   cd agri-triage
   ```

2. **Configure Environment Variables**:
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=gsk_your_key_here
   ```

### Option 1: Running with Docker (Recommended)

The easiest way to get started is using Docker Compose:

```bash
docker-compose up --build
```
The application will be available at `http://localhost:8000`.

### Option 2: Running Locally with `uv`

If you prefer a local Python environment:

```bash
# Install dependencies
uv sync

# Run the backend
uv run python run.py
```

The server will start at `http://localhost:8000`. You can access the UI directly in your browser.

---

## Agent Pipeline

```
Incoming Message
       │
       ▼
┌─────────────────────┐
│  Classification     │  → urgency (HIGH/MEDIUM/LOW), urgency_score (1-10), intent
│  (Groq LLM)         │
└─────────────────────┘
       │
       ▼
┌─────────────────────┐
│  Named Entity       │  → farmer_id, crop_type, location, dates[], issue_keywords[]
│  Recognition (NER)  │
└─────────────────────┘
       │
       ▼
┌─────────────────────┐
│  Draft Response     │  → contextually accurate reply
│  Generator          │
└─────────────────────┘
       │
       ▼
┌─────────────────────┐
│  Summary            │  → 1-sentence dashboard summary
└─────────────────────┘
       │
       ▼
  JSON Response to Frontend
```

---

## API Reference

### `POST /api/triage`

**Request body:**

```json
{
  "message": "My wheat crop is showing yellow patches...",
  "sender_name": "Ramesh Kumar",
  "sender_email": "ramesh@example.com"
}
```

**Response:**

```json
{
  "urgency": "HIGH",
  "urgency_score": 8,
  "intent": "Crop Disease",
  "entities": {
    "farmer_id": "F-2847",
    "crop_type": "wheat",
    "location": "Vidisha district",
    "dates": ["last Tuesday"],
    "issue_keywords": ["yellow patches", "disease"]
  },
  "draft_response": "Dear Ramesh, we have received your urgent report...",
  "summary": "Farmer reports yellow patches on wheat in Vidisha since last Tuesday.",
  "processing_time_ms": 1842
}
```

### `GET /api/health`

Returns `{"status": "ok"}`

---

## Model Used

- **Groq**: `llama3-8b-8192` (fast inference, free tier available)
- Swap to `mixtral-8x7b-32768` or `llama3-70b-8192` in `backend/agent.py` for better accuracy.
