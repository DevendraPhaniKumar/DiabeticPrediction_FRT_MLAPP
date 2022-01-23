import urllib.request
import json
import os
import ssl

print("Hi, We are going to predict the severe effects of Diabetic patient based on his past health history")
print("Please go through the MarK down readme files for the Dataset & ProjectDetails")
print(" ******  ")

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
data = {
    "Inputs": {
        "input1":
        [
            {
                'preg': input("Number of times pregnant :"),
                'plas': input("Plasma glucose concentration a 2 hours in an oral glucose tolerance test, Range 50-190 :"),
                'pres': input("Diastolic blood pressure in (mm Hg), Range 25-100 :"),
                'skin': input("Triceps skin fold thickness (mm) Range 5-70:"),
                'mass': input("Body mass index (weight in kg/(height in m)^2) Range 18-40 :"),
                'age': input("Age :"),
                'class': "1",
            },
        ],
    },
    "GlobalParameters": {
    }
}

body = str.encode(json.dumps(data))

url = 'http://0d2a3cc9-e80a-403d-a8bf-5ebdd0b89413.southcentralus.azurecontainer.io/score'
api_key = 'v835s6n4VBAn2D883NNXIkiJRGE7GpiM' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    
    json_result = json.loads(result)
    
    output = json_result["Results"]["WebServiceOutput0"][0]

    print('The Diabetic Prediction of Patient Aged : {} 3with a diabetic Prediction: {} where 1.0 means Diabetic else not with a Probability: {:.2f}'.format(output["age"],
                                                            output["Scored Labels"],
                                                            output["Scored Probabilities"]))
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
