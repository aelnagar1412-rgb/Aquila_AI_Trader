def ai_decision(signals):
    calls = signals.count("CALL")
    puts = signals.count("PUT")

    if calls >= 2:
        return "CALL", calls * 33
    if puts >= 2:
        return "PUT", puts * 33

    return None, 0
