# Team #2 Audit Log for Part 2 of Assignment 4
# Authors: Gabriel Tinsley, Sariah Bjornn, Eben Meyer, Chase Stombaugh

# Allow privileged users to write events while preventing unauthorized access and handling errors
# Input parameters:
#   user_id: String object that specifies the username
#   event_id: Dictionary that specifies the event data
# Exceptions: If user_id is NOT a string or event_data is NOT a dictionary
# Security checks: Returns true if user can write events
#                  Returns false if user can NOT write events
def add_log_event(user_id: str, event_data: dict) -> bool:
    return

