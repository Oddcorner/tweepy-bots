import requests
import os
import logging

logger = logging.getLogger()

def generate_picture(text):
    api_key = os.getenv("AI_KEY")
    
    logger.info("Sending post request to DeepAI text2img")
    r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': text,
    },
    headers={'api-key': api_key,}
    )

    if r.status_code >= 300:
        logger.error("Post request failed with status code: " + str(r.status_code))
        return None
    else:
        logger.info("Post request success.")
        return(r.json()['output_url'])
    
