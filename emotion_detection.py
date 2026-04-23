def emotion_detector(text_to_analyse): 
    # Define a function named sentiment_analyzer that takes a string input (text_to_analyse) 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    # URL of the sentiment analysis service 
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Create a dictionary with the text to be analyzed 

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Set the headers required for the API request 
    response = requests.post(url, json = myobj, headers=header) 

    # Parsing the JSON response from the API 
    formatted_response = json.loads(response.text)

    # Extracting sentiment label and score from the response 
    label = formatted_response['documentSentiment']['label'] 
    score = formatted_response['documentSentiment']['score']

    
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        score = None
    # For any other unexpected status codes, set label and score to None
    else:
        label = None
        score = None

    # Return the label and score in a dictionary
    return {'label': label, 'score': score}
    