def hair_chatbot(query):
    query = query.lower()

    if "hair fall" in query:
        return "Hair fall can be due to stress, poor diet, or hormonal issues."

    elif "dandruff" in query:
        return "Use anti-dandruff shampoo and keep scalp clean."

    elif "dry hair" in query:
        return "Use conditioner regularly and apply oil weekly."

    else:
        return "Maintain a healthy diet and proper hair care routine."