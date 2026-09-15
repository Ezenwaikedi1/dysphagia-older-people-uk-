"""
Dysphagia Analysis in Older People (UK)
This script demonstrates how dysphagia risk factors can be represented,
analysed, and flagged using simple Python logic.

This is NOT clinical software. It is an educational demonstration.
"""

# Example patient dataset
patients = [
    {"name": "John", "age": 82, "stroke_history": True, "dementia": False, "weight_loss": True, "coughing_meals": True},
    {"name": "Mary", "age": 90, "stroke_history": False, "dementia": True, "weight_loss": False, "coughing_meals": True},
    {"name": "Peter", "age": 76, "stroke_history": False, "dementia": False, "weight_loss": False, "coughing_meals": False},
]

def assess_dysphagia_risk(person):
    """
    Simple risk scoring based on known dysphagia indicators:
    - Age > 75
    - History of stroke
    - Dementia
    - Unexplained weight loss
    - Coughing during meals
    """
    score = 0

    if person["age"] > 75:
        score += 1
    if person["stroke_history"]:
        score += 2
    if person["dementia"]:
        score += 2
    if person["weight_loss"]:
        score += 1
    if person["coughing_meals"]:
        score += 2

    return score

def flag_high_risk(score):
    """
    Categorise risk level.
    """
    if score >= 5:
        return "High risk – urgent SLT referral recommended"
    elif score >= 3:
        return "Moderate risk – monitor and consider SLT referral"
    else:
        return "Low risk – continue routine observation"

# Run analysis
for p in patients:
    risk_score = assess_dysphagia_risk(p)
    status = flag_high_risk(risk_score)
    print(f"{p['name']} – Score: {risk_score} – {status}")
