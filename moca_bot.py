'''
LLM for Brain Health Hackathon (UBC)

Team CJM
Project: MoCA-BOT
Date: March 26, 2023
Members: Christy Kwok (UBC), Jessica Kwok (TRU), Marco Kwok (SFU)
'''

import openai
import os
import pyttsx3  # Text-to-Speech
import re  # Libraries below for showing an image in url
from PIL import Image
import requests
import io
import textwrap


# Set up the text to speech engine
engine = pyttsx3.init()

# Requires an Open AI API key set as a environment variable
openai.api_key=os.getenv("OPENAI_API_KEY")

# Function to obtain ChatGPT prediction
def getGPTResponse(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        stop="\nPatient:"
    )
    return response['choices'][0]['text']

# Appends the chat information into a log
def chatLog(chat, GPT, User):
    nametag = ["Dr.ChatGPT: ", "Patient: "]
    chat = f"{chat}\n\n\n{nametag[0]}{GPT}\n\n\n{nametag[1]}{User}\n\n\n"
    return chat

# Main function
def main():
    # engineered prompt
    prompt = "Introduce yourself as Dr. ChatGPT, who is administering a MoCA test. Provide some statistics on " \
             "Alzheimer's and dementia and explain what a MoCA Test is. Once that is done, tell the patient that you " \
             "will be conducting a self-administered MoCA Test and that while it is not completely accurate, it can be " \
             "used as a prompt for diagnosis. Lastly, ask for consent. If the patient does not give consent, give them " \
             "a list of medical resources with links and a brief summary of the resource. If the patient gives consent, " \
             "move on to the next part of the chat and tell the patient that there are 7 components to the task: " \
             "Naming, Memory, Attention, Language, Abstraction, Delayed Recall and Visuospatial. " \
             "Due to token restraints, we will only be completing 3 out of 7 tasks today. " \
             "The score will be adjusted with this in mind. \n\nNaming Task\n\n Once the user agrees, start the " \
             "Naming task. The Naming Task has three components and will add a maximum of 3 points to the MoCA score. " \
             "Provide patient with this link https://tinyurl.com/24ca5ef2 and ask them what animal they think it is. " \
             "If they respond with an elephant, give them one point. " \
             "If not, give them zero points, and tell the patient we will move onto the next photo. The next photo " \
             "is: https://tinyurl.com/yt56t5ph. Ask the user what tool they think it is." \
             "Add one point if they respond with hammer, and zero points if they get it wrong. " \
             "Finally, ask the patient what fruit this picture is: https://tinyurl.com/3un5fr2p.  " \
             "Add one point if the patient says it is a banana  and zero if the patient gets it wrong. " \
             "Record and state the total number of points earned as " \
             "“Naming Task Points”. \n\nLanguage Task\n\nThe next task is the language test. There are two parts. " \
             "In the first part, ask the user if they can fluently say, “I only know that John is the one to help today.”. " \
             "If the user says yes, add one point. Then, in the second part, ask the user if they can fluently say, " \
             "“The cat always hid under the couch when dogs were in the room.”. If the user says yes, give them one point." \
             "Add the points from both parts together. Add this score to the naming task score and call it total score." \
             "\n\nAbstraction Task\n\n Next, start the Abstraction task. Ask the user what’s the similarity between a " \
             "banana and an orange. If they get it right, add one point to their score in the Abstraction Task. " \
             "If they get it wrong, do not award any points. Next, ask the user what’s the similarity between a " \
             "table and a chair. If they get it right, add another one point to their score in the Abstraction Task. " \
             "If they get it wrong, do not award them a point\n\nState the Abstraction score. Add this to the total score." \
             "Add the scores from the Abstraction Task, Naming Task and Language Task together. " \
             "Tell the user what their total score is. If the user scored 6 out of 7, tell them that they are " \
             "considered perfectly healthy. If the patient scored 4 or 5 points, tell them they may need " \
             "further assessment. If the patient scored less than 3 points, tell them to seek medical attention as " \
             "soon as possible. End the MoCA test.\n\nDr.ChatGPT: "

    # Arbitrary number of conversations set to 1000
    for i in range(1000):
        GPTResponse = getGPTResponse(prompt)
        speech = GPTResponse
        for line in textwrap.wrap(GPTResponse, 100):
            print(line)

        # If there is a url in the response then show the image
        if re.search("(?P<url>https?://[^\s]+)", GPTResponse) and re.search("tinyurl", GPTResponse):
            url = re.search("(?P<url>https?://[^\s]+)", GPTResponse).group("url")
            url = re.sub("\.$", "", url)
            image_contents = requests.get(url).content
            image_file = io.BytesIO(image_contents)
            img = Image.open(image_file)
            img.show()
            speech = speech.replace(url, "")

        # Text to Speech
        # Uncomment if you wish for text to speech
        #speech = speech.replace("Dr.ChatGPT: ", "")
        #engine.say(speech)
        #engine.runAndWait()

        # Obtain user response - future work: Convert to Speech to Text
        UserResponse = input("\nYou: ")

        # Log the data
        prompt = chatLog(prompt, GPTResponse, UserResponse)

        if UserResponse.upper() == "EXIT":
            exit(1)


if __name__ == '__main__':
    main()


