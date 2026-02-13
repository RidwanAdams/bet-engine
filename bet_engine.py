import requests
import math

API_KEY = "3999369b6bmsh7e8d27826d53224p18d9d1jsn6e598e89ba32"
HEADERS = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
}

def poisson(lmbda, k):
    return (lmbda ** k * math.exp(-lmbda)) / math.factorial(k)

def over25_probability(home_xg, away_xg):
    prob = 0
    for h in range(6):
        for a in range(6):
            if h + a > 2:
                prob += poisson(home_xg, h) * poisson(away_xg, a)
    return prob

def get_fixtures():
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season=2025&next=5"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    print(data)  # ADD THIS
    return data


def analyze():
    fixtures = get_fixtures()
    picks = []

    for match in fixtures["response"]:
        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]

        # Dummy expected goals (replace with real stats later)
        home_xg = 1.6
        away_xg = 1.1

        over25 = over25_probability(home_xg, away_xg)

        if over25 > 0.70:
            picks.append(f"{home} vs {away} — Over 2.5 Goals ({round(over25*100)}%)")

    return picks

if __name__ == "__main__":
    results = analyze()
    if results:
        print("🔥 HIGH CONFIDENCE PICKS 🔥\n")
        for r in results:
            print(r)
    else:
        print("No strong bets today.")
if __name__ == "__main__":
    try:
        results = analyze()

        if results:
            message = "🔥 HIGH CONFIDENCE PICKS 🔥\n\n"
            for r in results:
                message += r + "\n"
        else:
            message = "No strong bets today."

        print(message)

    except Exception as e:
        print("ERROR:", str(e))
