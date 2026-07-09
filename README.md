# AI Software Company

An AI-powered software planning tool that uses **4 AI agents** to create complete project plans automatically. Enter a project idea and get a professional plan covering architecture, development, and QA review.

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

## Features

- **4 AI Agents** working as a team (Manager, Architect, Developer, QA)
- **Web Interface** built with Streamlit
- **CLI Interface** for terminal users
- **Download** your plan as a Markdown file
- **Real-time progress** tracking

## Tech Stack

- **Python** - Core language
- **CrewAI** - AI agent framework
- **Cohere** - Language model (Command R)
- **Streamlit** - Web UI
- **LangChain** - LLM integration

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Saikurra03/crewai-software-company.git
cd crewai-software-company
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up API key**

Create a `.env` file in the root folder:
```
COHERE_API_KEY=your_api_key_here
```

Get a free API key at [cohere.com](https://cohere.com)

## Usage

### Web Interface
```bash
streamlit run frontend/app.py
```

### CLI Interface
```bash
python app.py
```

## Project Structure

```
crewai-software-company/
├── app.py              # Main backend logic
├── frontend/
│   └── app.py          # Streamlit web interface
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Example

**Input:**
> Build an e-commerce website for selling handmade crafts

**Output:**
- Project plan with goals and scope
- Tech stack: React, Node.js, MongoDB, Docker
- Database schema and API endpoints
- Frontend components and routing
- QA review with security suggestions

## License

MIT License
