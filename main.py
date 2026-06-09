from data import MEDICATIONS
from dosing import calculate_dose
from safety import check_safe
from pills import pill_instructions

def main():
    print("=" * 40)
    print("Medication Dosage Calculator")
    print("=" * 40)
    print("NOT FOR REAL MEDICAL USE")
    print("=" * 40)

    symptom = input("Symptom (pain/fever/inflammation/allergies/itch/runny nose): ").lower().strip()
    age = int(input("Age (years): "))
    weight_lb = float(input("Weight (pounds): "))

    conditions_input = input("Any conditions? (comma-separated, or 'none'): ").lower().strip()
    if conditions_input in ["none", ""]:
        conditions = []
    else:
        conditions = [c.strip() for c in conditions_input.split(",")]

    matches = []
    for name, info in MEDICATIONS.items():
        if symptom in info["symptoms"]:
            matches.append((name, info))

    if not matches:
        print(f"\nNo medications found for symptom: '{symptom}'")
        input("\nPress Enter to exit...")
        return

    for med_name, med_info in matches:
        print(f"\n{'-' * 40}")
        print(f"Medication: {med_name.title()}")
        print(f"Examples: {', '.join(med_info['examples'])}")
        print(f"Drug Class: {med_info['drug_class']}")

        is_safe, msg = check_safe(med_name, med_info, age, conditions)
        if not is_safe:
            print(f"SAFETY ALERT: {msg}")
            continue

        single, max_daily = calculate_dose(med_name, med_info, age, weight_lb)
        interval = med_info["dose_interval_hours"]
        max_doses = med_info["max_doses_per_day"]

        print(f"\nDose: {single} mg every {interval} hours")
        print(f"Max daily: {max_daily} mg (up to {max_doses} doses/day)")
        print(f"Pill guide:\n{pill_instructions(single, med_info, age)}")
        print(f"Warnings: {'; '.join(med_info['warnings'])}")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()