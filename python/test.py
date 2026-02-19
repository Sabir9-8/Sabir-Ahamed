# Test inputs
base_score = 100
commits = 27          # > 20 → penalty should trigger
build_time = 3.5      # < 5 minutes → speed bonus applies

# Expected calculations
speed_bonus = 10 if build_time < 5 else 0
efficiency_penalty = -2 * max(0, commits - 20)

final_score = base_score + speed_bonus + efficiency_penalty

print("=== TEST CASE ===")
print(f"Base Score: {base_score}")
print(f"Commits: {commits}")
print(f"Build Time: {build_time} minutes")
print(f"Speed Bonus: {speed_bonus}")
print(f"Efficiency Penalty: {efficiency_penalty}")
print(f"Final Score: {final_score}")
