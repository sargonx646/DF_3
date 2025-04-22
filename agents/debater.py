def run_debate(extracted):
    stakeholders = extracted.get("stakeholders", ["Finance", "Policy", "HR"])
    debate = []

    for i, agent in enumerate(stakeholders):
        message = f"As {agent}, I believe the most important factor is..."
        debate.append({"agent": agent, "message": message})

    return debate