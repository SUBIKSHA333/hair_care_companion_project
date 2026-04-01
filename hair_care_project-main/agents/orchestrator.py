from .predictor_agent import predict_hair_fall
from .recommender_agent import recommend_products
from .chatbot_agent import hair_chatbot
from .vision_agent import analyze_hair_density

class HairCareOrchestrator:
    def run(self, user_data, image=None, query=None):
        result = {}

        # Prediction
        risk = predict_hair_fall(user_data)
        result["risk"] = risk

        # Recommendation
        recommendations = recommend_products(risk)
        result["recommendations"] = recommendations

        # Image Analysis
        if image is not None:
            density, ratio = analyze_hair_density(image)
            result["density"] = density
            result["density_ratio"] = ratio

        # Chatbot
        if query:
            response = hair_chatbot(query)
            result["chatbot_response"] = response

        return result