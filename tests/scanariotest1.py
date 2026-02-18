from src.core.scenario.scenario import Scenario

s = Scenario(
    name="Discount Campaign",
    domain="customer",
    environment={"channel": "mobile_app"},
    population={"age_group": "18-30"},
    metrics=["conversion_rate"]
)

print(s.describe())
