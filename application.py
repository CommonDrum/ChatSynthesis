import json
from chat import Chat
from synthezator import synthezator
import os
import openai





class Application:


    prompt_adjustment = "Generate text for speech synthesis for the following text:\n "

    



    def __init__(self):

       
        # check environment variables

        if "OPENAI_API_KEY" not in os.environ:
            openapi_key = input("OpenAI API key: ")
            os.environ["OPENAI_API_KEY"] = openapi_key
        if "AWS_ACCESS_KEY_ID" not in os.environ:
            aws_access_key = input("AWS access key: ")
            os.environ["AWS_ACCESS_KEY_ID"] = aws_access_key
        if "AWS_SECRET_ACCESS_KEY" not in os.environ:
            aws_secret_key = input("AWS secret key: ")
            os.environ["AWS_SECRET_ACCESS_KEY"] = aws_secret_key       


    


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





    def comp(PROMPT, MaxToken=4000, outputs=1): 
        # using OpenAI's Completion module that helps execute  
        # any tasks involving text  
        response = openai.Completion.create( 
            # model name used here is text-davinci-003 
            # there are many other models available under the  
            # umbrella of GPT-3 
            model="text-davinci-003", 
            # passing the user input  
            prompt=PROMPT, 
            # generated output can have "max_tokens" number of tokens  
            max_tokens=MaxToken, 
            # number of outputs generated in one call 
            n=outputs,

            temperature=0.6
        ) 
    
        
        return response.choices[0].text



if __name__ == "__main__":
    app = Application()
    openai.api_key = os.environ["OPENAI_API_KEY"]
    app.run()


