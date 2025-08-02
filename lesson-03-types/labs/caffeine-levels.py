caffeine_mg = float(input())

# Caffeine half life is about 6 hours
after_six_hours = caffeine_mg / 2
after_twelve_hours = after_six_hours / 2
after_twentyfour_hours = after_twelve_hours / 4  # 2 more halves: 12 -> 18 -> 24

# Output caffeine level after 6, 12, and 24 hours
print(f'After 6 hours: {after_six_hours:.2f} mg')
print(f'After 12 hours: {after_twelve_hours:.2f} mg')
print(f'After 24 hours: {after_twentyfour_hours:.2f} mg')
