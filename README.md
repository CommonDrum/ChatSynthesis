# ChatSynthesis

Hi since I have some trouble focusing on reading sometimes. And many times I need a quick fix or ask a question when in commandile.
I decided to create a little program to use AWS Polly and OpenAI API to help me focus a little bit during learning.
The project is not serious and I am mostly clueless in what I am doing but if you have helpful advice don't hesitate to contact me :)

## Use

1. Run the "ChatSynthesis.py" script without any arguments:

		  python ./ChatSynthesis.py

2. You will be prompted for your API keys and AWS IAM keys. They will be stored as environmental variables on your machine. Don't forget to reload the terminal so the variables can be read.
3. Run the "ChatSynthesis.py" with your question like this:

		python ./ChatSynthesis.py <prompt>
4. If you want to remove the keys from your environment you can do it manually or use ```--delete``` flag

		  python ./ChatSynthesis.py --delete
