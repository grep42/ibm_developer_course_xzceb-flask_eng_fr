"""
This module translates English text to French and French text to English
using IBM Watson Language Translator API.
"""

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

def setup_language_translator(api_key, url):
    """
    Set up the Language Translator with the provided API key and service URL.
    """
    authenticator = IAMAuthenticator(api_key)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)


    return language_translator

LANGUAGE_TRANSLATOR = setup_language_translator(API_KEY, URL)

def english_to_french(english_text=None):
    """
    Translate English text to French using IBM Watson Language Translator.
    """
    if english_text is None:
        english_text = input("Enter the English text to be translated: ")


    if not english_text:
        return None


    source_language = 'en'
    target_language = 'fr'


    translation = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        source=source_language,
        target=target_language).get_result()


    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text=None):
    """
    Translate French text to English using IBM Watson Language Translator.
    """
    if french_text is None:
        french_text = input("Enter the French text to be translated: ")


    if not french_text:
        return None


    source_language = 'fr'
    target_language = 'en'


    translation = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        source=source_language,
        target=target_language).get_result()


    english_text = translation['translations'][0]['translation']
    return english_text

def run_prompts():
    """
    Run the prompts for English to French and French to English translation.
    """
    english_text = input("Enter the English text to be translated: ")
    french_text = english_to_french(english_text)
    print(french_text)


    french_text = input("Enter the French text to be translated: ")
    english_text = french_to_english(french_text)
    print(english_text)




if __name__ == "__main__":
    run_prompts()
   