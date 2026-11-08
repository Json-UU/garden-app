"""Give simple gardening advice for a chosen season and plant type."""

SEASON_ADVICE = {
    "spring": "Prepare the soil and start sowing suitable seeds.",
    "summer": "Water your plants regularly and provide some shade.",
    "autumn": "Add mulch and clear fallen leaves from garden beds.",
    "winter": "Protect your plants from frost with covers.",
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}


def get_advice(season, plant_type):
    """Return two lines of advice; reject unsupported seasons or plant types."""
    season = season.strip().lower()
    plant_type = plant_type.strip().lower()
    if season not in SEASON_ADVICE:
        raise ValueError("Unsupported season. Choose spring, summer, autumn or winter.")
    if plant_type not in PLANT_ADVICE:
        raise ValueError("Unsupported plant type. Choose flower or vegetable.")
    return f"{SEASON_ADVICE[season]}\n{PLANT_ADVICE[plant_type]}"


def read_choice(label, choices):
    """Prompt until the user enters a supported choice, ignoring case and spaces."""
    options = "/".join(choices)
    while True:
        choice = input(f"Enter the {label} ({options}): ").strip().lower()
        if choice in choices:
            return choice
        print(f"Please choose one of: {', '.join(choices)}.")


def main():
    """Collect the user's choices and print the matching gardening advice."""
    try:
        season = read_choice("season", SEASON_ADVICE)
        plant_type = read_choice("plant type", PLANT_ADVICE)
    except (EOFError, KeyboardInterrupt):
        print("\nGardening advice cancelled.")
        return
    print(get_advice(season, plant_type))


if __name__ == "__main__":
    main()
