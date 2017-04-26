from autoSuggestion import *

import sys

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("Error: number of input is not correct")
		print("\t 1:The Microsoft key")
		print("\t 2:The word want to get auto suggestion")
		sys.exit(-1)

	ms_auto_suggestion = autoSuggestion(sys.argv[1])

	suggestionResponse = ms_auto_suggestion.getSuggestion(sys.argv[2])
	suggestions = suggestionResponse.get("suggestionGroups")[0].get("searchSuggestions")
	outcomes = [s.get("displayText") for s in suggestions]

	for s in outcomes:
		print s
