'''
unit tests for English to French translator and French to English
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


# Add code to create an instance of the IBM Watson Language translator
def translator_instance():
    """
    Creating an instance of the IBM Watson Language
    """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2022-11-18',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)
    return language_translator


# Add function englishToFrench
# to translate the text input in English
# to French and return the French text.
def english_to_french(english_text):
    """
    Receives a text in English and returns its French translation.
    """
    french_translation = translator_instance().translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    french_text = french_translation.get("translations")[0].get("translation")
    return french_text


# Add function frenchToEnglish
# to translate the text input in French
# to English and return the English text.
def french_to_english(french_text):
    """
    Receives a text in French and returns its English translation.
    """
    english_translation = translator_instance().translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    english_text = english_translation.get("translations")[0].get("translation")
    return english_text
