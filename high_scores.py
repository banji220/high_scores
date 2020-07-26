def latest(scores):
    latest_number = scores.pop()
    return latest_number

def personal_best(scores):
    highest_scores = max(scores)
    return highest_scores

def personal_top_three(scores):
    personal_best_score = sorted(scores, reverse=True)
    three_highest_scores = personal_best_score[:3]
    return three_highest_scores
    

