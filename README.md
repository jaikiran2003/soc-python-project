🌐 [Português (BR)](README.pt_BR.md) | [Español](README.es.md)

# 🎲 Soc Ops

**The icebreaker game that actually works.** A social bingo experience designed to break the ice at mixers and events. Find people who match the prompts. Get 5 in a row. Build real connections.

---

## ✨ Why Soc Ops?

At every mixer, the same thing happens: people cluster in familiar groups, awkward silences kill the vibe, and genuine connections don't happen. **Soc Ops changes that.**

- **5×5 bingo boards** with social prompts—not boring starters
- **Center free space** gives everyone a fair shot  
- **Real conversation triggers** that bring out authentic stories
- **Built for teams**—no complex rules, just *go find people and talk*
- **Fast-paced & fun**—games wrap up in minutes

---

## 🎯 How It Works

1. **Load the board** — Open Soc Ops on your phone or laptop
2. **Read a prompt** — "Has been to 5+ countries" or "Codes in Python"
3. **Find someone** — Mingle and ask around. If they match, they sign your board
4. **Get 5 in a row** — Horizontal, vertical, diagonal—you win when you connect
5. **Repeat** — New board, new people, new conversations

That's it. No app fatigue. No complex rules. Just genuine human connection.

---

## 💻 Tech Stack

Built with modern tools for speed and simplicity:

- **Backend**: FastAPI + Python 3.13  
- **Frontend**: HTMX + Jinja2 (server-rendered for snappy interactions)  
- **Styling**: Custom CSS utilities (no external framework bloat)  
- **Sessions**: Signed cookies for lightweight state management  
- **Game Logic**: Pure functions, fully testable  

---

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- `uv` (universal Python package installer)

### Install & Run

```bash
# Install dependencies
uv sync

# Start the development server
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open your browser and navigate to `http://localhost:8000`

---

## 🧪 Development

### Linting & Tests

```bash
# Format and lint code
uv run ruff check .

# Run tests
uv run pytest

# Run with coverage
uv run pytest --cov=app
```

All checks are enforced:
- Type hints required (via Pyupgrade)
- Unused variables caught (via Flake8 + Ruff)
- Import ordering checked (via isort)
- Code style enforced (via Ruff)

---

## 📚 Learn & Build

This project started as a **GitHub Copilot Agent Lab** to showcase modern Python development with AI assistance.

### Workshop & Guides

Follow the **[Agent Lab](https://copilot-dev-days.github.io/agent-lab-python/)** for a structured learning path:

| Part | Focus |
|------|-------|
| [**00**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=00-overview) | Overview & Prerequisites |
| [**01**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=01-setup) | Setup & Context Engineering |
| [**02**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=02-design) | Design-First Frontend |
| [**03**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=03-quiz-master) | Custom Quiz Master Agent |
| [**04**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=04-multi-agent) | Multi-Agent Development |

📖 Offline guides available in [`workshop/`](workshop/) — perfect for offline learning or reference.

---

## 📁 Project Structure

```
app/
├── main.py          # FastAPI app entry point
├── models.py        # Data models (Pydantic)
├── game_logic.py    # Pure game functions
├── game_service.py  # Game state management
├── data.py          # Question prompts
├── static/          # CSS, assets
└── templates/       # Jinja2 templates

tests/               # Full test suite
workshop/            # Lab guides (markdown)
docs/                # Additional documentation
```

---

## 🎨 Design Philosophy

**Form follows function.** Every visual choice serves the experience:
- Minimal, readable typography for quick scanning
- Responsive design works on phones and desktops
- HTMX for lightning-fast interactions (no page reloads)
- Pure CSS—no bloated frameworks

---

## 🤝 Contributing

We welcome contributions! Check out [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

---

**Ready to break the ice?** Start with the [Quick Start](#-quick-start) above, or dive into the [Agent Lab](https://copilot-dev-days.github.io/agent-lab-python/) to learn as you build.
