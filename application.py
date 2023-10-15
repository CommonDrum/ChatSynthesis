import json
from chat import Chat
from synthezator import synthezator
import os
import openai


class Application:


    prompt_adjustment = "Generate text for speech synthesis for the following text:\n "

    def __init__(self):
        self.synthezator = synthezator(self.access_key, self.secret_key)

    def run(self, prompt):
        
        prompt = self.prompt_adjustment + prompt
        anwser = Chat.comp(prompt)
        self.synthezator.synthesize(anwser)
        file = "output.mp3"
        os.system("afplay " + file)
        print("Bot: " + anwser)


    def comp(PROMPT, MaxToken=3000, outputs=1): 
        response = openai.Completion.create( 
            model="text-davinci-003", 
            prompt=PROMPT, 
            max_tokens=MaxToken, 
            n=outputs,
            temperature=0.6
        ) 

        return response.choices[0].text  


if __name__ == "__main__":
    app = Application()
    app.run()


