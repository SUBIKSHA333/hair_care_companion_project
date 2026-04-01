def predict_hair_fall(user_data):
    score = 0

    if user_data["stress"] > 7:
        score += 2
    if user_data["sleep"] < 6:
        score += 2
    if user_data["diet_quality"] in ["Poor", "Average"]:
        score += 2
    if user_data["water_type"] == "Hard":
        score += 1

    if score <= 2:
        return "Low"
    elif score <= 4:
        return "Medium"
    else:
        return "High"