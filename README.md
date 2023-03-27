# MoCA-BOT
AI-Powered Self-Administered Cognitive Assessment
*Please note this program is for educational purposes only and should not be treated as a medical diagnostic tool.*


## LLM for Brain Health 2023 Hackathon

Team CJM:

Christy Kwok (University of British Columbia)

Jessica Kwok (Thompson Rivers University)

Marco Kwok (Simon Fraser University)

## Inspiration
The global population is aging. From 2015 to 2050, the proportion of the world's population over 60 years of age is expected to double from 12% to 22%. Our current acute healthcare model is expected to transition, and there will be a growing need and demand for more robust chronic problems, like monitoring of cognitive decline. Unfortunately, access to healthcare resources for chronic problems are not always easily available, and it can be difficult for aging populations to access. 

AI tools have shown considerable success in practical applications, but often require multi-disciplinary collaboration, which can be difficult due to the difference in specialty. There are often barriers in communication due to jargon and difficulties with idea translation. We are a multi-disciplinary team, so we acknowledge the tremendous difficulties surrounding multi-disciplinary research. 

The recent emergence of large language models (LLMs) has shown significant computation power, and allows for prompt engineering, which involves the process of designing and creating user-inputted prompts for training AI models to perform specific tasks. These models already possess immense computational power, and do not require extensive programming knowledge to highlight the extent of their abilities. Prompt engineering removes barriers involving technological knowledge and understanding, allowing greater use cases of pre-trained models for healthcare professions. Many studies have shown success in the development and application of tools for various healthcare issues. Furthermore, LLMs, like ChatGPT-3, provide a user-friendly interface for the end user that may also be more ideal for less technologically-advanced individuals.  

Our inspiration comes from a desire to develop a novel, unique and original approach to tackling language program barriers and creating research tools and healthcare resources with minimal coding experience. We believe that the tools developed from these techniques will allow patients to communicate changes in their brain health remotely, reduce costs by improving outcomes through persistent remote monitoring, lower costs and time-commitment involved with patient travel, and lower sub-specialty care barriers for remote communities. 

## What it does
MoCA-BOT is a chatbot capable of administering selective portions of the Montreal Cognitive Assessment (MoCA), like the Language Task, Memory and Delayed Recall Task, Abstraction Task, Naming Task, Attention Task and Orientation Task. It scores the user based on their responses, evaluates the final score against the grading rubric and recommends additional medical interventions and resources for substandard scores. 

## How we built it
We utilized prompt engineering with OpenAI-ChatGPT-3 and a Python interface, as well as the basic structure of existing MoCA.

## Challenges we ran into
We ran into difficulties with the ChatGPT-3 interface in the beginning, and had to experiment with various optimal temperature, top P, frequency penalty and presence penalty settings. In addition, we face difficulties due to the non-deterministic nature of the replies from ChatGPT - ie, it is possible to get a different response each time the code is run. Other challenges also include ensuring the logical structure of our prompts are valid as well as carefully selecting clear and concise word choices. 

## Accomplishments that we're proud of
Upon conducting a preliminary literature review, we believe that we have utilized LLMs to develop a novel healthcare tool that may be useful in removing barriers that prevent access to healthcare resources. We also feel that we have demonstrated a proof-of-concept (PoC) for healthcare professionals with minimal coding experience. As an undergraduate multi-disciplinary team, we are proud that we have combined our respective specializations. 

## What we learned
From the creation of MoCA-BOT, our team learned a lot about the dynamic nature of chatgpt-3, and how to use prompt engineering, or use of user-generated input prompts, to solve logic structures and to achieve expected outputs. We also gained first-hand knowledge of the interactive nature of LLMs and their ability to explain healthcare ideas in layman’s terms to the end user; thus, making healthcare more accessible for everyone. 

## What's next for MoCA-BOT: AI-Powered Self-Administered Cognitive Assessment
While MoCA-BOT is capable of completing many aspects of MoCA, there are some limitations that we believe can be improved in the future. For example, long inputs are difficult due to the token maximum set by OpenAI. We would need to use additional programming or other solutions to bypass this token limitation.

Other steps we plan to take include:

1. Using ChatGPT-4 or more robust LLMs with larger power
2. Fine-tuning and training on "ideal" chat datasets 
3. Incorporating other AI models technologies for the Visuospatial and Executive Tasks
4. Recording the chat logs and extracting data for research purposes
5. Incorporating speech-to-text abilities for user input





