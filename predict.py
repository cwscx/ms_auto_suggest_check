from autoSuggestion import *

import ast

if __name__ == "__main__":
    ms_auto_suggestion = autoSuggestion("9811d7f7b99a441babfa6c4531a7a993")
    
    suggestionResponse = ms_auto_suggestion.getSuggestion("bill g")
    suggestions = suggestionResponse.get("suggestionGroups")[0].get("searchSuggestions")

    outcomes = [s.get("displayText") for s in suggestions]

    print outcomes
