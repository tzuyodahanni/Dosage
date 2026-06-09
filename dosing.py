def calculate_dose(med_name, med_info, age, weight_lb):
    """Returns single dose in mg and max daily in mg."""

    if med_info["dose_rule"] == "weight_based":
        single_dose = med_info["mg_per_lb"] * weight_lb
        max_daily_by_weight = med_info["max_daily_mg_per_lb"] * weight_lb
        max_daily = min(max_daily_by_weight, med_info["hard_max_daily_mg"])

    elif med_info["dose_rule"] == "fixed":
        if age <= med_info["child_age_max"]:
            single_dose = med_info["child_dose_mg"]
        else:
            single_dose = med_info["adult_dose_mg"]
        max_daily = single_dose * med_info["max_doses_per_day"]

    return round(single_dose, 1), round(max_daily, 1)