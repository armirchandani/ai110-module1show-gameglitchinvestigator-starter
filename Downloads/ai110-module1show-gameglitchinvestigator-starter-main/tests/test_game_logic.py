from logic_utils import check_guess, attempt_limit_map


# --- Attempt limit ---

def test_normal_attempt_limit_is_8():
    assert attempt_limit_map["Normal"] == 8

def test_easy_attempt_limit_is_6():
    assert attempt_limit_map["Easy"] == 6

def test_hard_attempt_limit_is_5():
    assert attempt_limit_map["Hard"] == 5


# --- Correct guess ---

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_winning_guess_at_lower_boundary():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

def test_winning_guess_at_upper_boundary():
    outcome, _ = check_guess(100, 100)
    assert outcome == "Win"


# --- Hints: go higher / go lower ---

def test_guess_too_high_returns_outcome():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_high_returns_go_higher_message():
    _, message = check_guess(60, 50)
    assert "HIGHER" in message

def test_guess_too_low_returns_outcome():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_too_low_returns_go_lower_message():
    _, message = check_guess(40, 50)
    assert "LOWER" in message

def test_hint_one_below_secret():
    outcome, message = check_guess(49, 50)
    assert outcome == "Too Low"
    assert "LOWER" in message

def test_hint_one_above_secret():
    outcome, message = check_guess(51, 50)
    assert outcome == "Too High"
    assert "HIGHER" in message
