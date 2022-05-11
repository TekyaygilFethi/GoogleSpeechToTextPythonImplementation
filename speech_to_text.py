from google.cloud import speech_v1 as speech
import os
from google.oauth2 import service_account
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))


class SpeechToTextHelper:
    def __init__(self, config):

        self.credentials = service_account.Credentials.from_service_account_file(
            os.environ["JSON_NAME"]
        )
        self.client = speech.SpeechClient(credentials=self.credentials)
        self.config = config

    def speech_to_text(self, audio_file_path):
        response = self.client.recognize(config=self.config, audio=audio_file_path)
        self.print_sentences(response)

    def print_sentences(self, response):
        for result in response.results:
            best_alternative = result.alternatives[0]
            transcript = best_alternative.transcript
            confidence = best_alternative.confidence
            print("-" * 80)
            print(f"Transcript: {transcript}")
            print(f"Confidence: {confidence:.0%}")

    def speech_to_text_long(self, audio_file_path):
        operation = self.client.long_running_recognize(
            config=self.config, audio=audio_file_path
        )
        print("Waiting for operation to complete...")
        response = operation.result(timeout=90)
        self.print_sentences(response)

    def print_sentences_long(self, response):
        for result in response.results:
            print("Transcript: {}".format(result.alternatives[0].transcript))
            print("Confidence: {}".format(result.alternatives[0].confidence))
