from speech_to_text import SpeechToTextHelper

if __name__ == "__main__":
    config = dict(
        language_code="tr-TR",
        encoding="LINEAR16",
        sample_rate_hertz=44100,
        audio_channel_count=2,
        enable_automatic_punctuation=True,
    )

    speech_to_text_helper_obj = SpeechToTextHelper(config)

    audio = dict(uri="gs://diarizationuv/uzuntrim.wav")

    speech_to_text_helper_obj.speech_to_text_long(audio)
