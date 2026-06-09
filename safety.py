def check_safe(med_name, med_info, age, has_conditions=None):
    """Returns (is_safe: bool, message: str)"""

    if has_conditions is None:
        has_conditions = []

    if age < med_info["min_age_years"]:
        return False, f"Minimum age for {med_name} is {med_info['min_age_years']} years. Consult a doctor."

    for condition in has_conditions:
        if condition.lower() in [c.lower() for c in med_info["contraindications"]]:
            return False, f"Avoid {med_name} with {condition}. Consult a doctor."

    return True, "OK"