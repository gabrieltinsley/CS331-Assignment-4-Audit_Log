# Team #2 Audit Log for Part 2 of Assignment 4
# Authors: Gabriel Tinsley, Sariah Bjornn, Eben Meyer, Chase Stombaugh

# Allow privileged users to write events while preventing unauthorized access and handling errors
# Input parameters:
#   user_id: String object that specifies the username
#   event_id: Dictionary that specifies the event data
# Exceptions: If user_id is NOT a string or event_data is NOT a dictionary
# Security checks: Returns true if user can write events
#                  Returns false if user can NOT write events
# def add_log_event(user_id: str, event_data: dict) -> bool:
    # return


# Team #2 Audit Log for Part 2 of Assignment 4
# Authors: Gabriel Tinsley, Sariah Bjornn, Eben Meyer, Chase Stombaugh

# User roles
admin_users = ["admin1", "admin2"]

# Allow privileged users to write events while preventing unauthorized access and handling errors
# Input parameters:
#   user_id: String object that specifies the username
#   event_id: Dictionary that specifies the event data
# Exceptions: If user_id is NOT a string or event_data is NOT a dictionary
# Security checks: Returns true if user can write events and it is logged
#                  Returns false if user can NOT write events, input is invalid, or an error occurs
def add_log_event(user_id: str, event_data: dict) -> bool:
    #input validation
    if not isinstance(user_id, str) or not isinstance(event_data, dict):
        print("Invalid input type")
        return False
    
    # Security check to only allow admins
    if user_id not in admin_users:
        print("User does not have permission to log events")
        return False
    
    # appending the security event to a log file
    try: 
        with open("audit_log.txt", "a") as log_file:
            log_file.write(f"{user_id}: {event_data}\n")
        return True
    except Exception as e: 
        print(f"There was an error while writing to log: {e}")
        return False
