# Paper Boy

> Customize your very own AI-powered newsletters delivered to your inbox on your schedule.

## What It Does

Paper Boy lets users subscribe to custom AI-generated newsletters on any topic they care about. Users pick their topics, set a delivery cadence (daily, weekly, bi-weekly, monthly), and Paper Boy handles the rest — scraping for relevant updates since the last delivery window, summarizing them with AI, and emailing a clean digest straight to the inbox.

## Architecture

```
paper-boy/
├── backend/          # Django REST API
│   ├── config/       # Settings, URLs, WSGI/ASGI
│   └── apps/
│       ├── users/        # Auth, profiles
│       ├── newsletters/  # Topics, subscriptions, digest models
│       └── delivery/     # Celery tasks, email rendering
└── frontend/         # Vue 3 SPA
    └── src/
        ├── views/        # Page-level components
        ├── components/   # Reusable UI
        ├── stores/       # Pinia state
        └── router/       # Vue Router
```

## Tech Stack

| Layer | Technology |
|---|---|
| Backend language | Python 3.12+ |
| Package manager | [uv](https://docs.astral.sh/uv/) |
| Web framework | Django 5 + Django REST Framework |
| Task queue | Celery + Redis |
| Database | PostgreSQL |
| Frontend | Vue 3 (Composition API) + Vite |
| State management | Pinia |
| HTTP client | Axios |
| Email | Django email + SMTP |
| AI | Anthropic Claude API |

## Getting Started

### Prerequisites

- Python 3.12+
- Node.js 20+
- Redis (for Celery)
- PostgreSQL

### Backend Setup

```bash
cd backend

# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv sync

# Copy env file and fill in your values
cp .env.example .env

# Run migrations
uv run python manage.py migrate

# Create a superuser
uv run python manage.py createsuperuser

# Start the dev server
uv run python manage.py runserver
```

### Celery Worker (for scheduled delivery)

```bash
cd backend
uv run celery -A config worker -l info
uv run celery -A config beat -l info
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The Vue dev server proxies `/api/` to `http://localhost:8000` automatically.

## Environment Variables

See `backend/.env.example` for all required variables. Key ones:

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DATABASE_URL` | PostgreSQL connection string |
| `REDIS_URL` | Redis connection string |
| `ANTHROPIC_API_KEY` | Claude API key for AI generation |
| `EMAIL_URL` | SMTP connection string |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts |
| `CORS_ALLOWED_ORIGINS` | Frontend origin(s) |

## Core Concepts

### Newsletter
A user-defined subscription with a topic query, delivery schedule, and list of recipients (just themselves for now). Each newsletter stores the timestamp of the last successful delivery so the AI knows what time window to scrape.

### Digest
The generated output for a given delivery run. Contains the raw scraped content, the AI-generated summary, and delivery status.

### Delivery Pipeline
1. Celery Beat fires a periodic task every hour
2. Task queries for newsletters due for delivery
3. For each newsletter, the AI scrapes for updates in the topic's time window
4. Claude summarizes the results into a formatted digest
5. Email is rendered and sent via Django's email backend
6. Digest record is saved with delivery timestamp

## Development Notes

- API is versioned under `/api/v1/`
- DRF token auth (swap for JWT in production)
- CORS is open to `localhost:5173` in development
- Vue Router uses history mode; configure your server to serve `index.html` for all non-API routes in production
