import random

def player(prev_play, opponent_history=[], play_history=[]):
    if not prev_play:
        opponent_history.clear()
        play_history.clear()
        guess = "R"
    else:
        opponent_history.append(prev_play)

    n = 3  # Look at the last 3 moves to predict the next move
    guess = "R"  # Default guess

    if len(opponent_history) > n:
        pattern = "".join(opponent_history[-n:])

        # Collect all patterns of length n+1
        pattern_freq = {}
        for i in range(len(opponent_history)-n):
            key = "".join(opponent_history[i:i+n+1])
            if key in pattern_freq:
                pattern_freq[key] += 1
            else:
                pattern_freq[key] = 1

        # Find the most frequent pattern that starts with the current pattern
        possible_patterns = [pattern + move for move in "RPS"]
        pattern_guess = max(possible_patterns, key=lambda x: pattern_freq.get(x, 0))

        # Predict the next move based on the pattern
        guess = pattern_guess[-1]

    # Use a simple counter strategy based on the guess
    counter_strategy = {'P': 'S', 'R': 'P', 'S': 'R'}
    guess = counter_strategy[guess]
    play_history.append(guess)

    return guess
