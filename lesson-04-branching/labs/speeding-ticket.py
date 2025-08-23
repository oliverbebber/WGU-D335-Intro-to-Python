# given two integers representing speed limit and driving speed (mph)
speed_limit = int(input())
driving_speed = int(input())

# driving 10mph under the speed limit = $50 ticket
if driving_speed <= speed_limit - 10:
    ticket_amount = 50
# driving 6-20mph over the speed limit = $75 ticket
elif speed_limit + 6 <= driving_speed <= speed_limit + 20:  # include the bottom range (+ 6) to ensure tickets aren't issued for driving 5mph over the limit
    ticket_amount = 75
# driving 21-40mph over the speed limit = $150 ticket
elif speed_limit + 21 <= driving_speed <= speed_limit + 40:
    ticket_amount = 150
# driving faster than 40mph over the speed limit = $300 ticket
elif driving_speed > speed_limit + 40:
    ticket_amount = 300
# otherwise, no ticket
else:
    ticket_amount = 0

# output the traffic ticket amount
print(ticket_amount)
