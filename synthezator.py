import boto3
from contextlib import closing
import os
from datetime import datetime


class Synthezator:

    poll_client = None
    voice_id = "Joanna"
    output_format = "mp3"

    
    def __init__(self, region = "us-east-1"):
        self.poll_client = boto3.Session(
            aws_access_key_id = os.environ["AWS_ACCESS_KEY"],
            aws_secret_access_key = os.environ["AWS_SECRET_KEY"],
            region_name=region).client('polly')
        
    def set_options(self, voice_id, output_format):
        self.voice_id = voice_id
        self.output_format = output_format

    def synthesize(self, text_to_say) -> str:

        output = "Prompts/" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".mp3"

        response = self.poll_client.synthesize_speech(Text=text_to_say, 
                                           OutputFormat=self.output_format, 
                                           VoiceId=self.voice_id)
        if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
                
                with open(output, "wb") as file:
                    file.write(stream.read())
            
            return output
            print("Text to Speech conversion complete!")
        else:
            print("Text to Speech conversion failed!")
       