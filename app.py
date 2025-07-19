from statistics import mean
from collections import defaultdict

# Judge data
judges_data = {
    "Liam": [
        {"name": "SnackerDavis", "score": 5.75}, {"name": "Ineedsleep", "score": 5.25},
        {"name": "CocoPommel", "score": 5.75}, {"name": "windawine", "score": 6.25},
        {"name": "CodeSprite", "score": 6.375}, {"name": "IncPuchay", "score": 5.25},
        {"name": "Van-Houston", "score": 2.75}, {"name": "Vicioustrex", "score": 5.0},
        {"name": "NL", "score": 7.25}, {"name": "Boazon", "score": 5.0},
        {"name": "Aarna", "score": 3.75}, {"name": "TheBehemoth", "score": 3.75},
        {"name": "FallingDragon", "score": 2.75}, {"name": "ArdenDragon", "score": 6.25},
        {"name": "RedRaven9", "score": 4.75}, {"name": "Lore", "score": 5.625}
    ],
    "Timothy": [
        {"name": "SNAKEY_11", "score": 2}, {"name": "Cookie", "score": 3.1},
        {"name": "live.sadat", "score": 4.8}, {"name": "Dragoncode8", "score": 1.8},
        {"name": "CocoPommel", "score": 7.9}, {"name": "LJE", "score": 8.3},
        {"name": "Aarna", "score": 2.9}, {"name": "Beans", "score": 3.75},
        {"name": "RadhaJiKoDaas", "score": 3.9}, {"name": "SonicTheHedgehog", "score": 3.6},
        {"name": "kiaantolia", "score": 6.6}, {"name": "SilverWolf", "score": 8.5},
        {"name": "lgcarnahan", "score": 1.0}, {"name": "JSCoder", "score": 2.375},
        {"name": "NonPlayerCharacter", "score": 8.8}, {"name": "CodeSprite", "score": 7.5},
        {"name": "Programmrr00", "score": 3.8}, {"name": "IncPuchay", "score": 4.8},
        {"name": "Fireball", "score": 7.8}, {"name": "RedRaven9", "score": 2.9},
        {"name": "VVhiteTiger", "score": 8.4}, {"name": "YokieBob", "score": 7.0},
        {"name": "s300080423", "score": 9.2}, {"name": "Vicioustrex", "score": 3.8},
        {"name": "Griffinjiun", "score": 4.8}, {"name": "Eyeinthesky", "score": 3.4}
    ],
    "Duke": [
        {"name": "NL", "score": 7.0}, {"name": "SnackerDavis", "score": 3.75},
        {"name": "Pinkcatsoda", "score": 1.875}, {"name": "Ineedsleep", "score": 3.0},
        {"name": "Boazon", "score": 3.5}, {"name": "windawine", "score": 5.0},
        {"name": "-A--I", "score": 3.625}, {"name": "TheBehemoth", "score": 4.25},
        {"name": "KarthikeyaK", "score": 3.125}, {"name": "LichenStudios", "score": 1.5},
        {"name": "JLE", "score": 4.875}, {"name": "FallingDragon", "score": 1.625},
        {"name": "DragonStudios", "score": 2.125}, {"name": "Fatima", "score": 2.0},
        {"name": "VetriR", "score": 4.375}, {"name": "ArdenDragon", "score": 5.25},
        {"name": "Coder2098", "score": 3.375}, {"name": "Javacrafter", "score": 4.2},
        {"name": "Cyan Spirit", "score": 6.75}, {"name": "emvalle10", "score": 1.375},
        {"name": "Bristlefrost", "score": 3.5}, {"name": "MatthewSvetlev", "score": 0.875},
        {"name": "Lore", "score": 4.75}, {"name": "AwesomeOrion", "score": 5.175},
        {"name": "aj", "score": 1.0}, {"name": "Familia de la Presa", "score": 0.6},
        {"name": "Van-Houston", "score": 1.4}
    ],
    "MindqueBlast": [
        {"name": "SNAKEY_11", "score": 1.75}, {"name": "Cookie", "score": 3},
        {"name": "LivesadatLS", "score": 3.25}, {"name": "Dragoncode8", "score": 2.25},
        {"name": "CocoPommel", "score": 5.875}, {"name": "LJE", "score": 7.5},
        {"name": "Aarna", "score": 3.125}, {"name": "Beans", "score": 2.875},
        {"name": "RadhaJiKoDaas", "score": 3.125}, {"name": "Kesidedav", "score": 0.625},
        {"name": "SonicTheHedgehog", "score": 6}, {"name": "kiaantolia", "score": 6.0625},
        {"name": "SilverWolf", "score": 6.3125}, {"name": "JSCoder", "score": 4.3125},
        {"name": "NonPlayerCharacter", "score": 8}, {"name": "CodeSprite", "score": 7.5},
        {"name": "Programmrr00", "score": 3.625}, {"name": "IncPuchay", "score": 5.125},
        {"name": "Fireball", "score": 6.5625}, {"name": "RedRaven9", "score": 5.25},
        {"name": "VVhiteTiger", "score": 7.625}, {"name": "YokieBob", "score": 7.8125},
        {"name": "s300080423", "score": 9.125}, {"name": "Vicioustrex", "score": 5.125},
        {"name": "Griffinjiun", "score": 3.875}, {"name": "Eyeinthesky", "score": 4.375}
    ],
    "Henry": [
        {"name": "SilverWolf", "score": 5.25}, {"name": "lgcarnahan", "score": 0.25},
        {"name": "JSCoder", "score": 4.875}, {"name": "NonPlayerCharacter", "score": 7.125},
        {"name": "CodeSprite", "score": 6}, {"name": "Programmrr00", "score": 3.75},
        {"name": "IncPuchay", "score": 4}, {"name": "Fireball", "score": 5.75},
        {"name": "RedRaven9", "score": 3.125}, {"name": "VVhiteTiger", "score": 6.625},
        {"name": "YokieBob", "score": 5}, {"name": "s300080423", "score": 7},
        {"name": "Vicioustrex", "score": 2.625}, {"name": "Griffinjiun", "score": 4.875},
        {"name": "Eyeinthesky", "score": 3.875}, {"name": "RadhaJiKoDaas", "score": 3},
        {"name": "Kesidedav", "score": 1.25}, {"name": "SonicTheHedgehog", "score": 5.5},
        {"name": "kiaantolia", "score": 4.75}
    ],
    "CodeEngineer": [
        {"name": "SNAKEY_11", "score": 4.25}, {"name": "Cookie", "score": 7.125},
        {"name": "LivesadatLS", "score": 5.25}, {"name": "Dragoncode8", "score": 3.875},
        {"name": "CocoPommel", "score": 7.625}, {"name": "LJE", "score": 8.25},
        {"name": "Aarna", "score": 4.125}, {"name": "Beans", "score": 3.5},
        {"name": "RadhaJiKoDaas", "score": 4.875}, {"name": "Kesidedav", "score": 1.25},
        {"name": "SonicTheHedgehog", "score": 6.5}, {"name": "kiaantolia", "score": 7.5},
        {"name": "SilverWolf", "score": 7.25}, {"name": "lgcarnahan", "score": 0.5},
        {"name": "JSCoder", "score": 6.125}, {"name": "CodeSprite", "score": 6.625},
        {"name": "Programmrr00", "score": 2}, {"name": "IncPuchay", "score": 4.875},
        {"name": "Fireball", "score": 6.375}, {"name": "RedRaven9", "score": 5.5},
        {"name": "NonPlayerCharacter", "score": 7.125}, {"name": "VVhiteTiger", "score": 7.5},
        {"name": "YokieBob", "score": 7.25}, {"name": "s300080423", "score": 8.5},
        {"name": "Vicioustrex", "score": 7}, {"name": "Griffinjiun", "score": 3.75},
        {"name": "Eyeinthesky", "score": 5.75}
    ],
    "TML": [
            {"name": "SNAKEY_11", "score": 3.75},
            {"name": "Cookie", "score": 4.75},
            {"name": "LivesadatLS", "score": 2.5},
            {"name": "Dragoncode8", "score": 3.5},
            {"name": "CocoPommel", "score": 7.0},
            {"name": "LJE", "score": 6.5},
            {"name": "Aarna", "score": 4.25},
            {"name": "Beans", "score": 3.75},
            {"name": "RadhaJiKoDaas", "score": 3.625},
            {"name": "SonicTheHedgehog", "score": 6.375},
            {"name": "kiaantolia", "score": 5.25},
            {"name": "SilverWolf", "score": 5.0},
            {"name": "lgcarnahan", "score": 1.0},
            {"name": "JSCoder", "score": 2.375},
            {"name": "NonPlayerCharacter", "score": 6.25},
            {"name": "CodeSprite", "score": 4.5},
            {"name": "Programmrr00", "score": 2.5},
            {"name": "IncPuchay", "score": 2.625},
            {"name": "Fireball", "score": 6.0},
            {"name": "RedRaven9", "score": 3.75},
            {"name": "VVhiteTiger", "score": 6.75},
            {"name": "YokieBob", "score": 7.0},
            {"name": "s300080423", "score": 7.5},
            {"name": "Vicioustrex", "score": 2.25},
            {"name": "Griffinjiun", "score": 5.0},
            {"name": "Eyeinthesky", "score": 3.75}
        ]
}

# Combine all scores
contestant_scores = defaultdict(list)
for judge_scores in judges_data.values():
    for entry in judge_scores:
        contestant_scores[entry["name"]].append(entry["score"])

# Calculate average score per contestant
averages = {name: round(mean(scores), 3) for name, scores in contestant_scores.items()}
sorted_averages = dict(sorted(averages.items(), key=lambda x: -x[1]))
for rank, (name, avg) in enumerate(sorted_averages.items(), start=1):
    print(f"{rank}. {name}: {avg:.3f}")
