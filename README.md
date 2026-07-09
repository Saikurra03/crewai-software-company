# AI Software Company

An AI-powered software planning tool that uses **4 AI agents** to create complete project plans automatically.

## What Does This Do?

You type a project idea (like "build a food delivery app"), and 4 AI agents work together to create:
- Project goals and requirements
- Technology recommendations
- Database and API design
- Frontend layout
- Security and quality review

## Live Demo

**Try it now:** [Click here to use the app](https://your-app-name.streamlit.app)

## How It Works

```
Your Idea
    |
    v
[Project Manager]  --> Creates project plan & requirements
    |
    v
[Software Architect] --> Designs tech stack & system structure
    |
    v
[Full-Stack Developer] --> Plans APIs, database, frontend
    |
    v
[QA Engineer] --> Reviews & improves the entire plan
    |
    v
Complete Project Plan
```

## Quick Start

### Run Locally (5 minutes)

1. **Get free API key** from [cohere.com](https://cohere.com)

2. **Clone and run:**
```bash
git clone https://github.com/Saikurra03/crewai-software-company.git
cd crewai-software-company
pip install -r requirements.txt
```

3. **Create `.env` file:**
```
COHERE_API_KEY=your_key_here
```

4. **Start the app:**
```bash
streamlit run frontend/app.py
```

### Deploy Online (Free)

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign up with GitHub
3. Click "New app" and select this repository
4. Add your API key in Settings > Secrets
5. Done! Share the URL with anyone.

**Full instructions:** See [SETUP_GUIDE.md](SETUP_GUIDE.md)

## Features

- **4 AI Agents** working as a team
- **Web Interface** with progress tracking
- **CLI Interface** for terminal users
- **Download** plans as Markdown files

## Tech Stack

- Python, CrewAI, Cohere, Streamlit, LangChain

## Project Structure

```
crewai-software-company/
├── app.py              # Backend logic
├── frontend/
│   └── app.py          # Web interface
├── requirements.txt    # Dependencies
├── SETUP_GUIDE.md      # Beginner guide
├── .gitignore
└── README.md
```

## Example

**Input:** "Build an e-commerce website for handmade crafts"

**Output:** Complete plan with React, Node.js, MongoDB, Docker stack, API endpoints, database schema, and security recommendations.

## License

MIT License
