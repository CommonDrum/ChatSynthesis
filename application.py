import json
from chat import Chat
from synthezator import synthezator
import os
import openai


class Application:


    prompt_adjustment = "Generate text for speech synthesis for the following text:\n "

    



    def __init__(self):

       
        try:
            with open('config.json') as json_file:
                data = json.load(json_file)
                self.api_key = data['openai_api_key']
                self.access_key = data['aws_access_key']
                self.secret_key = data['aws_secret_key']
        except:
            print("Provide data for authentication: (Your data will be saved in config.json file)\n")
            self.api_key = input("OpenAI API key: ")
            self.access_key = input("AWS access key: ")
            self.secret_key = input("AWS secret key: ")
            data = {}
            data['openai_api_key'] = self.api_key
            data['aws_access_key'] = self.access_key
            data['aws_secret_key'] = self.secret_key
            with open('config.json', 'w') as outfile:
                json.dump(data, outfile)

        openai.api_key = self.api_key


    


        #self.chat = Chat(api_key)
        self.synthezator = synthezator(self.access_key, self.secret_key)

    def run(self):
        print("Hello, I'm a chatbot. Ask me anything!\n")
        while True:
            question = input("You: ")

            if question == "exit":
                break

            question = self.prompt_adjustment + question

            anwser = self.comp(question)

            self.synthezator.synthesize(anwser, "output.mp3")


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


