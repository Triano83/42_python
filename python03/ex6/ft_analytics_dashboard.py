def ft_analytics_dashboard() -> None:
    data = [
        {"name": "alice", "score": 2300, "achievements": ["kill", "level_10"],
         "region": "north"},
        {"name": "bob", "score": 1800, "achievements": ["kill"],
         "region": "central"},
        {"name": "charlie", "score": 2150,
         "achievements": ["level_10", "boss"], "region": "north"},
        {"name": "diana", "score": 2050, "achievements": ["kill", "boss"],
         "region": "east"}
    ]
    total_players = len(data)

    print("=== Game Analytics Dashboard ===")

    high_scorers = [p["name"] for p in data if p["score"] > 2000]
    doubled = [p["score"] * 2 for p in data]
    players_name = [player["name"] for player in data]

    print("\n=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {doubled}")
    print(f"Active players: {players_name[:3]}")

    player_scores = {p["name"]: p["score"] for p in data}
    ach_counts = {p["name"]: len(p["achievements"]) for p in data}

    all_cats = [
        "high" if p["score"] > 2100 else "medium" if p["score"] >= 1900
        else "low" for p in data
    ]
    score_categories = {c: all_cats.count(c) for c in set(all_cats)}

    print("\n=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {ach_counts}")

    unique_regions = {p["region"] for p in data}
    all_ach = {a for p in data for a in p["achievements"]}

    print("\n=== Set Comprehension Examples ===")
    print(f"Unique players: {set(players_name)}")
    print(f"Unique achievements: {all_ach}")
    print(f"Active regions: {unique_regions}")

    avg_score = sum([p["score"] for p in data]) / total_players
    total_unique_ach = len(all_ach)

    top_p = max(data, key=lambda x: x["score"])

    print("\n=== Combined Analysis ===")
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_ach}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: {top_p['name']} ({top_p['score']} points, "
          f"{len(top_p['achievements'])} achievements)")


if __name__ == "__main__":
    ft_analytics_dashboard()
