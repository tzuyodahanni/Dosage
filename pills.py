def _find_pill_match(dose_mg, strengths):
    best = None
    
    for strength in strengths:
        pills = dose_mg / strength
        
        if pills == int(pills) and pills > 0:
            return f"{int(pills)} x {strength}mg = {int(pills) * strength}mg"
        
        if pills * 2 == int(pills * 2) and pills >= 0.5:
            whole = int(pills)
            total = int(pills * strength)
            if whole == 0:
                return f"half a {strength}mg = {total}mg"
            else:
                return f"{whole} and a half {strength}mg = {total}mg"
        
        whole_pills = int(pills)
        if whole_pills > 0:
            actual = whole_pills * strength
            gap = dose_mg - actual
            if best is None or gap < best[2]:
                best = (whole_pills, strength, gap, actual)
    
    if best:
        whole_pills, strength, gap, actual = best
        return f"{whole_pills} x {strength}mg = {actual}mg (under by {gap}mg)"
    
    return None


def _find_liquid_match(dose_mg, mg_per_ml, allowed_ml):
    if mg_per_ml <= 0:
        return None
    
    best = None
    
    for ml in allowed_ml:
        actual_mg = ml * mg_per_ml
        if actual_mg > dose_mg:
            continue
        
        gap = dose_mg - actual_mg
        if best is None or gap < best[2]:
            best = (ml, actual_mg, gap)
    
    if best:
        ml, actual_mg, gap = best
        if gap == 0:
            return f"{ml}mL = {actual_mg}mg"
        else:
            return f"{ml}mL = {actual_mg}mg (under by {gap}mg)"
    
    return None


def pill_instructions(dose_mg, med_info, age):
    lines = []
    is_child = age <= med_info.get("child_age_max", 11)
    
    if is_child and "child_pill_strengths" in med_info:
        child_match = _find_pill_match(dose_mg, med_info["child_pill_strengths"])
        if child_match:
            lines.append(f"  Chewable: {child_match}")
    
    if "adult_pill_strengths" in med_info:
        adult_match = _find_pill_match(dose_mg, med_info["adult_pill_strengths"])
        if adult_match:
            lines.append(f"  Pill: {adult_match}")
    
    if "liquid_mg_per_ml" in med_info and "liquid_doses_ml" in med_info:
        liquid_match = _find_liquid_match(
            dose_mg, 
            med_info["liquid_mg_per_ml"], 
            med_info["liquid_doses_ml"]
        )
        if liquid_match:
            lines.append(f"  Liquid: {liquid_match}")
    
    if not lines:
        return "  Consult pharmacist for dosing"
    
    return "\n".join(lines)