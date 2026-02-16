def calculate_match_points(match_won, kills, deaths, rounds_won, rounds_lost):
    # Match win points
    match_win_points = 10 if match_won else 0

    # Kill/Death Ratio Points
    kdr = kills / max(1, deaths)
    kdr_points = min(5, round(2 * kdr))

    # Round Win Bonus
    round_win_bonus = (rounds_won - rounds_lost) * 0.5

    # Total points
    total_points = match_win_points + kdr_points + round_win_bonus
    return total_points


# Example usage for 3 matches
match_results = [
    {'match_won': False,  'kills': 63, 'deaths': 85, 'rounds_won': 7, 'rounds_lost': 13},
    {'match_won': False, 'kills': 45, 'deaths': 73, 'rounds_won': 4, 'rounds_lost': 13},
    # {'match_won': False,  'kills': 57, 'deaths': 71, 'rounds_won': 5, 'rounds_lost': 13}
]

total_series_points = 0
for i, match in enumerate(match_results, 1):
    points = calculate_match_points(**match)
    total_series_points += points
    print(f"Match {i} Points: {points:.2f}")

print(f"\nTotal Series Points: {total_series_points:.2f}")
