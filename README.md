# Bet Engine - Football Analysis & Prediction

A Python script for football match analysis and betting predictions using statistical modeling and API data integration.

## ⚽ Features

- **API Integration** - Fetch live football fixtures from RapidAPI
- **Statistical Modeling** - Poisson distribution for goal predictions
- **Probability Calculations** - Over 2.5 goals probability
- **High Confidence Picks** - Filter matches with >70% probability
- **Error Handling** - Graceful fallback to sample data

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Libraries**: 
  - `requests` - API calls
  - `math` - Statistical calculations
- **API**: RapidAPI Football API
- **Data**: Live football fixtures or sample data

## 📁 Project Structure

```
bet-engine/
├── bet_engine.py      # Main analysis script
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## 🔧 Setup Instructions

### 1. Prerequisites
```bash
# Install Python 3.x
python --version

# Install required packages
pip install requests
```

### 2. API Configuration
1. Get a free API key from [RapidAPI Football API](https://rapidapi.com/api-sports/api/api-football)
2. Replace the API key in `bet_engine.py`:
```python
API_KEY = "YOUR_RAPIDAPI_KEY_HERE"
```

### 3. Running the Script
```bash
# Clone repository
git clone https://github.com/yourusername/bet-engine.git
cd bet-engine

# Run the analysis
python bet_engine.py
```

## 📊 How It Works

### 1. Data Fetching
- Connects to RapidAPI Football API
- Fetches upcoming fixtures for Premier League (league ID: 39)
- Falls back to sample data if API fails

### 2. Statistical Analysis
- Uses Poisson distribution to model goal scoring
- Calculates probability of Over 2.5 goals
- Formula: `P(goals > 2) = Σ Poisson(home_xg, h) * Poisson(away_xg, a)`

### 3. Filtering Criteria
- Only selects matches with >70% probability of Over 2.5 goals
- Returns "High Confidence Picks" with probability percentages

## 📈 Sample Output

```
🔥 HIGH CONFIDENCE PICKS 🔥

Manchester City vs Crystal Palace — Over 2.5 Goals (78%)
Liverpool vs Burnley — Over 2.5 Goals (82%)
Bayern Munich vs Mainz 05 — Over 2.5 Goals (85%)
```

## 🔍 Code Explanation

### Key Functions

1. **`poisson(lmbda, k)`** - Calculates Poisson probability
2. **`over25_probability(home_xg, away_xg)`** - Probability of >2.5 goals
3. **`get_fixtures()`** - Fetches match data from API
4. **`analyze()`** - Main analysis pipeline

### Expected Goals (xG)
Currently uses dummy xG values. For production:
- Integrate real xG data from Understat or other sources
- Use team form, injuries, and other factors
- Implement machine learning for better predictions

## 🚀 Extending the Project

### 1. Add More Leagues
```python
# League IDs
LEAGUES = {
    "premier_league": 39,
    "la_liga": 140,
    "serie_a": 135,
    "bundesliga": 78,
    "ligue_1": 61
}
```

### 2. Additional Bet Types
- Both Teams to Score (BTTS)
- Double Chance (1X, X2)
- Correct Score predictions
- Asian Handicap

### 3. Advanced Features
- Historical data analysis
- Machine learning models
- Real-time odds comparison
- Bankroll management

### 4. Visualization
- Probability charts
- Team form graphs
- Odds movement tracking

## 📋 Requirements File

Create `requirements.txt`:
```txt
requests>=2.28.0
pandas>=1.5.0  # For data analysis
numpy>=1.24.0  # For calculations
matplotlib>=3.6.0  # For visualizations
```

## 🧪 Testing

```bash
# Test with sample data (no API key needed)
python bet_engine.py

# Expected: "No strong bets today." or picks list
```

## ⚠️ Limitations & Notes

1. **Dummy Data**: Current xG values are placeholders
2. **API Limits**: RapidAPI has request limits on free tier
3. **Statistical Model**: Poisson distribution is basic; consider more advanced models
4. **Not Financial Advice**: For educational purposes only

## 🔒 Environment Variables (Recommended)

For security, use environment variables:
```bash
# Set in terminal
export RAPIDAPI_KEY="your_api_key_here"

# Or in Python
import os
API_KEY = os.getenv("RAPIDAPI_KEY")
```

## 🌐 API Alternatives

1. **football-data.org** - Free tier available
2. **Understat** - Advanced xG data
3. **SofaScore API** - Live match statistics
4. **Odds API** - Betting odds aggregation

## 📄 License

MIT License - free for personal and educational use.

## 🙏 Acknowledgments

- [RapidAPI](https://rapidapi.com) for API platform
- [API-Football](https://www.api-football.com) for football data
- Poisson distribution methodology from statistical sports analysis

## 📚 Learning Resources

- [Poisson Distribution in Sports Betting](https://www.pinnacle.com/en/betting-articles/betting-strategy/poisson-distribution-betting/6v2j2x9p2r5p7z8w)
- [Expected Goals (xG) Explained](https://theanalyst.com/na/2021/08/what-are-expected-goals-xg/)
- [API-Football Documentation](https://www.api-football.com/documentation)

---

**Disclaimer**: This tool is for educational purposes. Always gamble responsibly and within your means. Past performance does not guarantee future results.