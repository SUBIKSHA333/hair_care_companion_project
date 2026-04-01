def recommend_products(risk):
    if risk == "Low":
        return {
            "shampoo": "Mild Herbal Shampoo",
            "oil": "Coconut Oil",
            "tips": "Maintain your routine and eat healthy."
        }

    elif risk == "Medium":
        return {
            "shampoo": "Anti-Hair Fall Shampoo",
            "oil": "Castor Oil",
            "tips": "Reduce stress and improve diet."
        }

    else:
        return {
            "shampoo": "Clinical Strength Shampoo",
            "oil": "Onion Oil",
            "tips": "Consult a doctor and follow strict care."
        }