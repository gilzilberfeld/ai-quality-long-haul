from DatabaseLogger import DatabaseLogger


def test_for_sudden_quality_regression():
    logger = DatabaseLogger()
    results = logger.load_results()

    assert len(results) >= 4, "Not enough historical data to detect a sudden regression."

    latest_result = results[-1] # Most recent result
    latest_score = latest_result['quality_score']

    # Calculate the average of the 3 results *before* the latest one
    previous_results = results[-4:-1]
    previous_scores = [r['quality_score'] for r in previous_results]
    average_previous_score = sum(previous_scores) / len(previous_scores)

    # Define our failure threshold (e.g., a drop of more than 10%)
    threshold = 0.10
    score_drop_percentage = (average_previous_score - latest_score) / average_previous_score

    assert score_drop_percentage <= threshold, \
        f"Sudden quality regression detected! Score dropped from an average of {average_previous_score:.2f} to {latest_score} (a {score_drop_percentage:.2%} drop)."


def test_for_gradual_quality_decay():
    logger = DatabaseLogger()
    results = logger.load_results()

    # We need enough data for two batches of comparison (e.g., 3 runs each)
    assert len(results) >= 6, "Not enough historical data to detect a gradual drift."

    # Get the last 3 results for our "recent" batch
    recent_results = results[-3:]
    recent_scores = [r['quality_score'] for r in recent_results]
    recent_average = sum(recent_scores) / len(recent_scores)

    # Get the 3 results *before* the recent batch for our "older" batch
    older_results = results[-6:-3]
    older_scores = [r['quality_score'] for r in older_results]
    older_average = sum(older_scores) / len(older_scores)

    assert recent_average >= older_average, \
        f"Gradual quality decay detected! The average score has dropped from {older_average:.2f} to {recent_average:.2f} over the last 6 runs."
