# 15 / 15 score submission
score = 5
foul = -3
gold_rating = 40

players = int(input())
star_players = 0
for i in range(players):
    scores = int(input())
    fouls = int(input())
    if scores * score + fouls * foul > 40:
        star_players += 1

print(f"{star_players}{star_players == players and '+' or ''}")
