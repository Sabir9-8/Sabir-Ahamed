base_score = 100
commits = 28          # triggers penalty
build_time = 4.2      # triggers speed bonus

speed_bonus = 10 if build_time < 5 else 0
efficiency_penalty = -2 * max(0, commits - 20)

final_score = base_score + speed_bonus + efficiency_penalty

print("=== TEST CASE 1 ===")
print(f"Base Score: {base_score}")
print(f"Commits: {commits}")
print(f"Speed Bonus: {speed_bonus}")
print(f"Efficiency Penalty: {efficiency_penalty}")
print(f"Final Score: {final_score}")
