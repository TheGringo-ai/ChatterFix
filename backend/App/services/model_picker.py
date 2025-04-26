def pick_model(task_type: str, priority: str = "balanced") -> str:
    if task_type == "summarize":
        return "gpt-4.1-mini" if priority != "max" else "gpt-4o"
    elif task_type == "review":
        return "gpt-4o" if priority == "max" else "gpt-4.1"
    elif task_type == "generate":
        return "gpt-4o"
    else:
        return "gpt-3.5-turbo"