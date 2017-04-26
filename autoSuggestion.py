import httplib
import urllib
import base64
import ast

class autoSuggestion():

    def __init__(self, key):
        if type(key) is str:
            self.headers = {
                'Ocp-Apim-Subscription-Key': key,
            }
        else:
            print("[Error: the key should be of type str.")


    def getSuggestion(self, string):
        if type(string) is str:
            params = urllib.urlencode({
                # Request parameters
                'q': string,
            })

            try:
                conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
                conn.request("GET", "/bing/v5.0/suggestions/?%s" % params, "{body}", self.headers)
                response = conn.getresponse()
                data = response.read()
                conn.close()

                # Parse the string into the dictionary
                return ast.literal_eval(data)
            except Exception as e:
                print("[Errno {0}] {1}".format(e.errno, e.strerror))
        else:
            print("The requested string should be of type str.")
