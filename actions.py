
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionSubscribe(Action):

     def name(self) -> Text:
         return "action_subscribe"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         image = requests.get('http://shibe.online/api/shibes?count=1').json()[0]

         dispatcher.utter_message("Congrats. You are now a subscriber. Check out this cute picture: {}".format(image))

         return []
