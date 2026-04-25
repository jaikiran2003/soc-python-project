# Soc Ops - Social Bingo Game

## Development Checklist
Before committing changes:
- [ ] Lint: `uv run ruff check .`
- [ ] Install: `uv sync`
- [ ] Test: `uv run pytest`

## Code Style
- Python 3.13+ with type hints, snake_case, Pydantic frozen models
- Lint with ruff

## Architecture
- FastAPI + HTMX + Jinja2 backend
- Custom CSS utilities for frontend
- Server-side sessions with signed cookies
- Pure game logic functions

## Build and Run
- Dev server: `uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

## Conventions
- 5x5 bingo board with center free space
- Social questions in `app/data.py`
- HTMX for partial updates (avoid Simple Browser)

## Frontend Design
Avoid generic AI aesthetics: distinctive typography, cohesive colors, meaningful animations, atmospheric backgrounds.

See `workshop/` and `docs/` for details.