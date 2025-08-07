# Import necessary libraries
import re
# Define the Match class
class Match:
    def __init__(self, pattern, string):
        self.pattern = pattern
        self.string = string

    def find_match(self):
        match = re.search(self.pattern, self.string)
        if match:
            return match.group()
        return None
