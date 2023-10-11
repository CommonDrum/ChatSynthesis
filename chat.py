import openai


class Chat:

    def __init__(self, api_key):
        openai.api_key = api_key

    def comp(PROMPT, MaxToken=3000, outputs=1): 
        response = openai.Completion.create( 
            model="text-davinci-003", 
            prompt=PROMPT, 
            max_tokens=MaxToken, 
            n=outputs,
            temperature=0.6
        ) 

        return response.cjhoices[0].text   
        