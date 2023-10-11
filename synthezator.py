import boto3
from contextlib import closing
import os


class synthezator:

    poll_client = None
    voice_id = "Joanna"
    output_format = "mp3"

    
    def __init__(self, region = "us-east-1"):
        self.poll_client = boto3.Session(
            aws_access_key_id = os.environ["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"],
            region_name=region).client('polly')
        
    def set_options(self, voice_id, output_format):
        self.voice_id = voice_id
        self.output_format = output_format

    def synthesize(self, text_to_say, output):

        response = self.poll_client.synthesize_speech(Text=text_to_say, 
                                           OutputFormat=self.output_format, 
                                           VoiceId=self.voice_id)
        # Check if the synthesis is successful
        if "AudioStream" in response:
            # Open a file for writing the output as Binary stream
            with closing(response["AudioStream"]) as stream:
                
                # Write the stream content to a file
                with open(output, "wb") as file:
                    file.write(stream.read())
                    
            print("Text to Speech conversion complete!")
        else:
            # The synthesis failed, output error message
            print("Text to Speech conversion failed!")
       