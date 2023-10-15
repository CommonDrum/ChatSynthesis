import argparse
import os
from application import Application

parser = argparse.ArgumentParser(description='Set API keys or run the application')
parser.add_argument('--api_key_1', type=str, help='API key 1')
parser.add_argument('--api_key_2', type=str, help='API key 2')
parser.add_argument('--api_key_3', type=str, help='API key 3')
parser.add_argument('--prompt', type=str, help='Prompt to generate chat response')
args = parser.parse_args()

if args.api_key_1 and args.api_key_2 and args.api_key_3:
    os.environ['API_KEY_1'] = args.api_key_1
    os.environ['API_KEY_2'] = args.api_key_2
    os.environ['API_KEY_3'] = args.api_key_3
else:
    if args.prompt:
        app = Application(prompt=args.prompt)
    else:
        app = Application()
    app.run()
import os
from application import Application

parser = argparse.ArgumentParser(description='Set API keys or run the application')
parser.add_argument('--api_key_1', type=str, help='API key 1')
parser.add_argument('--api_key_2', type=str, help='API key 2')
parser.add_argument('--api_key_3', type=str, help='API key 3')
args = parser.parse_args()

if args.api_key_1 and args.api_key_2 and args.api_key_3:
    os.environ['API_KEY_1'] = args.api_key_1
    os.environ['API_KEY_2'] = args.api_key_2
    os.environ['API_KEY_3'] = args.api_key_3
else:
    app = Application()
    app.run()
