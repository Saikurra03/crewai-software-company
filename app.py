import os
import sys
import types
from unittest.mock import MagicMock

for mod_name in [
    "chromadb", "chromadb.api", "chromadb.api.client",
    "chromadb.config", "chromadb.api.types",
]:
    sys.modules[mod_name] = MagicMock()

import litellm
from dotenv import load_dotenv
from crewai import Agent, LLM, Task, Crew, Process

load_dotenv()

_original_completion = litellm.completion

def _patched_completion(*args, **kwargs):
    messages = kwargs.get("messages") or (args[1] if len(args) > 1 else None)
    if messages:
        for msg in messages:
            if isinstance(msg, dict):
                msg.pop("cache_breakpoint", None)
    return _original_completion(*args, **kwargs)

litellm.completion = _patched_completion


def run_crew(problem_statement: str, status_callback=None) -> str:
    """Run the CrewAI pipeline and return the result."""

    def log(msg):
        if status_callback:
            status_callback(msg)
        else:
            print(msg, flush=True)

    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    if not COHERE_API_KEY:
        raise ValueError("COHERE_API_KEY not found in .env file!")

    log("[1/4] Initializing AI agents...")

    llm = LLM(
        model="cohere/command-r-08-2024",
        api_key=COHERE_API_KEY,
        temperature=0.3
    )

    project_manager = Agent(
        role="Project Manager",
        goal="Manage the software project, gather requirements, create a plan, and prepare final documentation.",
        backstory="You are an experienced IT Project Manager with 15+ years of experience.",
        llm=llm,
        allow_delegation=False,
        memory=False,
        verbose=True
    )

    software_architect = Agent(
        role="Software Architect",
        goal="Design the complete software architecture, select technologies, and define system structure.",
        backstory="You are a Senior Software Architect.",
        llm=llm,
        allow_delegation=False,
        memory=False,
        verbose=True
    )

    developer = Agent(
        role="Full-Stack Developer",
        goal="Build both the backend and frontend of the application.",
        backstory="You are a skilled Full-Stack Developer.",
        llm=llm,
        allow_delegation=False,
        memory=False,
        verbose=True
    )

    qa_engineer = Agent(
        role="QA Engineer",
        goal="Review the entire solution, identify issues, and suggest improvements.",
        backstory="You are a Quality Assurance expert.",
        llm=llm,
        allow_delegation=False,
        memory=False,
        verbose=True
    )

    log("[2/4] Creating tasks...")

    planning_task = Task(
        description=f"""
        The client wants: {problem_statement}
        Create a concise project plan (max 300 words) covering:
        - Project goal and scope
        - Main modules / features
        - Functional and non-functional requirements
        - High-level workflow
        - Deliverables
        """,
        expected_output="A professional software project plan with clear requirements.",
        agent=project_manager
    )

    architecture_task = Task(
        description="""
        Based on the project plan provided, design the software architecture.
        Include:
        - Technology stack (frontend, backend, database, auth, deployment)
        - Folder structure
        - Explanation of technology choices
        """,
        expected_output="Complete architecture document with technology stack and structure.",
        agent=software_architect,
        context=[planning_task]
    )

    development_task = Task(
        description="""
        Based on the architecture document, create a detailed development plan covering both backend and frontend.
        Include:
        - Database tables / schema
        - REST API endpoints and business logic
        - Authentication mechanism
        - Frontend pages, components, routing, and UI/UX
        - Development steps
        """,
        expected_output="Detailed development plan covering backend and frontend.",
        agent=developer,
        context=[architecture_task]
    )

    qa_task = Task(
        description="""
        Review the entire solution (plan, architecture, development plan).
        Provide:
        - Strengths and weaknesses
        - Security and performance improvements
        - Testing strategy
        - Deployment suggestions
        - Overall quality assessment
        """,
        expected_output="Professional QA review report with actionable feedback.",
        agent=qa_engineer,
        context=[planning_task, architecture_task, development_task]
    )

    log("[3/4] Running 4 AI agents (this takes 1-2 minutes)...")

    software_company = Crew(
        agents=[project_manager, software_architect, developer, qa_engineer],
        tasks=[planning_task, architecture_task, development_task, qa_task],
        process=Process.sequential,
        verbose=True,
        memory=False
    )

    try:
        result = software_company.kickoff()
        log("[4/4] Done!")
        return result.raw
    except Exception as e:
        error_msg = f"ERROR: {type(e).__name__}: {str(e)}"
        log(error_msg)
        raise


if __name__ == "__main__":
    problem = input("\nEnter Project Idea:\n\n")
    print("\nExecuting Crew...\n")
    try:
        output = run_crew(problem)
        print("\n" + "=" * 80)
        print("           AI SOFTWARE COMPANY (4 AGENTS)")
        print("=" * 80)
        print(output)
        print("\n" + "=" * 80)
        print("PROJECT COMPLETED SUCCESSFULLY")
        print("=" * 80)
    except Exception as e:
        print(f"\nFAILED: {e}")
