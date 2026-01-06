import yaml
import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data_raw/yaml")
OUTPUT_PATH = Path("data_processed/csv")
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

matches = []
balls = []


for yaml_file in RAW_DATA_PATH.glob("*.yaml"):
    with open(yaml_file, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

        match_info = data["info"]

        match_id = yaml_file.stem
        match_date = match_info["dates"][0]
        teams = match_info["teams"]
        venue = match_info.get("venue", "Unknown")

        matches.append({
            "match_id": match_id,
            "date": match_date,
            "team_1": teams[0],
            "team_2": teams[1],
            "venue": venue
        })

        for innings in data["innings"]:
            for innings_name, innings_data in innings.items():
                batting_team = innings_data["team"]

                for delivery in innings_data["deliveries"]:
                    for ball_number, ball_data in delivery.items():

                        batter = ball_data["batter"]
                        bowler = ball_data["bowler"]

                        runs_batter = ball_data["runs"]["batter"]
                        runs_extras = ball_data["runs"]["extras"]
                        runs_total = ball_data["runs"]["total"]

                        wicket = ball_data.get("wickets", [])
                        is_wicket = 1 if wicket else 0

                        balls.append({
                            "match_id": match_id,
                            "innings": innings_name,
                            "ball": ball_number,
                            "batting_team": batting_team,
                            "batter": batter,
                            "bowler": bowler,
                            "runs_batter": runs_batter,
                            "runs_extras": runs_extras,
                            "runs_total": runs_total,
                            "is_wicket": is_wicket
                        })



df_matches = pd.DataFrame(matches)
df_balls = pd.DataFrame(balls)


df_matches.to_csv(OUTPUT_PATH / "matches_ipl_2025.csv", index=False)
df_balls.to_csv(OUTPUT_PATH / "balls_ipl_2025.csv", index=False)


print("IPL 2025 data extraction completed successfully.")


