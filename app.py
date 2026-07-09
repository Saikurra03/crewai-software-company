import os
import litellm
from dotenv import load_dotenv

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

AGENTS = {
    "Project Manager": "You are an experienced IT Project Manager with 15+ years of experience. Convert client ideas into clear project plans with requirements, modules, workflow, and deliverables. Max 300 words.",
    "Software Architect": "You are a Senior Software Architect. Design complete software architecture including technology stack (frontend, backend, database, auth, deployment), folder structure, and explain technology choices.",
    "Full-Stack Developer": "You are a skilled Full-Stack Developer. Create detailed development plans covering database schema, REST API endpoints, authentication, frontend pages/components/routing, and step-by-step development.",
    "QA Engineer": "You are a Quality Assurance expert. Review the entire solution and provide strengths/weaknesses, security improvements, performance suggestions, testing strategy, deployment tips, and overall quality assessment.",
}

TASK_TEMPLATES = [
    "The client wants: {input}\n\nCreate a concise project plan covering:\n- Project goal and scope\n- Main modules/features\n- Functional and non-functional requirements\n- High-level workflow\n- Deliverables",
    "Based on the previous plan, design the software architecture. Include:\n- Technology stack (frontend, backend, database, auth, deployment)\n- Folder structure\n- Explanation of technology choices",
    "Based on the architecture, create a detailed development plan. Include:\n- Database tables/schema\n- REST API endpoints and business logic\n- Authentication mechanism\n- Frontend pages, components, routing, UI/UX\n- Development steps",
    "Review the entire solution (plan, architecture, development plan). Provide:\n- Strengths and weaknesses\n- Security and performance improvements\n- Testing strategy\n- Deployment suggestions\n- Overall quality assessment",
]


def run_crew(problem_statement: str, status_callback=None) -> str:
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    if not COHERE_API_KEY:
        raise ValueError("COHERE_API_KEY not found!")

    def log(msg):
        if status_callback:
            status_callback(msg)

    agent_names = list(AGENTS.keys())
    context = ""

    for i, (name, system_prompt) in enumerate(AGENTS.items()):
        log(f"[{i+1}/4] {name} is working...")

        task = TASK_TEMPLATES[i].format(input=problem_statement) if i == 0 else TASK_TEMPLATES[i]

        messages = [
            {"role": "system", "content": system_prompt},
        ]
        if context:
            messages.append({"role": "user", "content": f"Previous work:\n\n{context}\n\nNow complete this task:\n{task}"})
        else:
            messages.append({"role": "user", "content": task})

        response = litellm.completion(
            model="cohere/command-r-08-2024",
            api_key=COHERE_API_KEY,
            messages=messages,
            temperature=0.3,
        )

        context = response.choices[0].message.content

    log("[4/4] Done!")
    return context


if __name__ == "__main__":
    problem = input("\nEnter Project Idea:\n\n")
    print("\nExecuting...\n")
    try:
        output = run_crew(problem)
        print("\n" + "=" * 80)
        print("           AI SOFTWARE COMPANY (4 AGENTS)")
        print("=" * 80)
        print(output)
        print("\n" + "=" * 80)
    except Exception as e:
        print(f"\nFAILED: {e}")
