import random

teams = input("enter the name of the teams by space: ").split()
n = len(teams)

if n % 2 != 0:                                                # اگر تعداد تیم‌ها فرد بود یک rest اضافه میکنیم
    teams.append("REST")
    n += 1

weeks_needed = n - 1

choices = {}                                                  # برای هر تیم یک لیست ساخته میشود و حریف تمام هفته هایش به ترتیب مشخص میشود
for t in teams:
    opponents = [x for x in teams if x != t]
    random.shuffle(opponents)
    choices[t] = opponents

weeks = []

for week in range(weeks_needed):

    busy_teams = set()
    games = []

    for team in teams:

        if team in busy_teams:
            continue

        candidate = choices[team][week]                        # انتخاب حریف تصادفی
                                                         
        if candidate in busy_teams:                            # اگر حریف پیشنهادی مشغول بود دنبال حریف آزاد بگرد
            found = False
            for c in choices[team]:
                if c not in busy_teams:
                    candidate = c
                    found = True
                    break
            if not found:
                games = None
                break

        if candidate in busy_teams:                            # اگر هنوز حریف مشغول بود هفته خراب است
            games = None
            break

        games.append((team, candidate))
        busy_teams.add(team)
        busy_teams.add(candidate)

    if games is None or len(games) != n // 2:                  # اگر جفت پیدا نشد یا تعداد بازی ها ناقص بود هفته خراب است و به هفته بعد منتقل میشود
        print("Week", week + 1, "invalid => recreate later")
        continue

    weeks.append(games)                                        # هفته جدید معتبر اضافه شود

weeks_return = []
for games in weeks:
    reverse_games = [(b, a) for a, b in games]
    weeks_return.append(reverse_games)



print("games list:")
print("going games:")
for w, games in enumerate(weeks, start=1):
    print(f"Week {w}:")
    for a, b in games:
        if a == "REST":
            print(f"{b}: rest this week")
        elif b == "REST":
            print(f"{a}: rest this week")
        else:
            print(f"{a} vs {b}")
    print()
print("turning game:")
for w, games in enumerate(weeks_return, start=weeks_needed+1):
    print(f"Week {w}:")
    for a, b in games:
        if a == "REST":
            print(f"{b}: rest this week")
        elif b == "REST":
            print(f"{a}: rest this week")
        else:
            print(f"{a} vs {b}")
    print()