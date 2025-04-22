import time
def simulate_debate(personas, chat_log):
    new_log = []
    for i in range(3):  # 3 rounds
        for persona in personas:
            msg = f"As {persona['name']}, I believe we must consider {persona['goals'][0].lower()}."
            chat_log.append({"agent": persona["name"], "message": msg})
            new_log.append({"agent": persona["name"], "message": msg})
            time.sleep(0.2)
    return chat_log