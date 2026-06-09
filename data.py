MEDICATIONS = {
    "acetaminophen": {
        "symptoms": ["pain", "fever"],
        "drug_class": "Analgesic / Antipyretic",
        "examples": ["Tylenol"],
        "dose_rule": "weight_based",
        "mg_per_lb": 4.5,
        "max_daily_mg_per_lb": 34,
        "hard_max_daily_mg": 3000,
        "dose_interval_hours": 4,
        "max_doses_per_day": 6,
        "child_age_max": 11,
        "adult_pill_strengths": [325, 500, 650],
        "child_pill_strengths": [80, 160],
        "liquid_mg_per_ml": 32,
        "liquid_doses_ml": [5, 7.5, 10, 12.5, 15],
        "warnings": [
            "Liver damage if overdosed",
            "Avoid alcohol"
        ],
        "min_age_years": 2,
        "contraindications": ["liver disease", "heavy alcohol use"]
    },

    "ibuprofen": {
        "symptoms": ["pain", "fever", "inflammation"],
        "drug_class": "NSAID",
        "examples": ["Advil", "Motrin"],
        "dose_rule": "weight_based",
        "mg_per_lb": 2.3,
        "max_daily_mg_per_lb": 18,
        "hard_max_daily_mg": 1200,
        "dose_interval_hours": 6,
        "max_doses_per_day": 4,
        "child_age_max": 11,
        "adult_pill_strengths": [200, 400, 600],
        "child_pill_strengths": [50, 100],
        "liquid_mg_per_ml": 20,
        "liquid_doses_ml": [5, 7.5, 10, 12.5, 15],
        "warnings": [
            "Stomach ulcers, GI bleeding",
            "Kidney strain",
            "Avoid in 3rd trimester pregnancy"
        ],
        "min_age_years": 6,
        "contraindications": ["pregnancy 3rd trimester", "blood thinners", "kidney disease"]
    },

    "loratadine": {
        "symptoms": ["allergies", "itch", "runny nose"],
        "drug_class": "2nd-Gen Antihistamine",
        "examples": ["Claritin"],
        "dose_rule": "fixed",
        "child_age_max": 5,
        "child_dose_mg": 5,
        "adult_dose_mg": 10,
        "dose_interval_hours": 24,
        "max_doses_per_day": 1,
        "adult_pill_strengths": [10],
        "child_pill_strengths": [5],
        "liquid_mg_per_ml": 1,
        "liquid_doses_ml": [5, 10],
        "warnings": [
            "Minimal drowsiness",
            "May cause dry mouth"
        ],
        "min_age_years": 2,
        "contraindications": ["severe liver disease"]
    }
}