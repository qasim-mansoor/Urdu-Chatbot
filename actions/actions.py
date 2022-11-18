# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action


def get_restaurants(restaurant=None, cuisine=None):
    restaurants = [
        {
            "id": 0,
            "name": "سپائس بازار",
            "cuisine": "دیسی",
            "price-range": "mid-range"
        },
        {
            "id": 1,
            "name": "دی لکھنوی",
            "cuisine": "دیسی",
            "price-range": "cheap"
        },
        {
            "id": 2,
            "name": "انداز ریسٹورنٹ",
            "cuisine": "English",
            "price-range": "mid-range"
        },
        {
            "id": 3,
            "name": "آر کیڈین کیفے",
            "cuisine": "اٹالین",
            "price-range": "cheap"
        },
        {
            "id": 4,
            "name": "پاستا لا وستا",
            "cuisine": "اٹالین",
            "price-range": "mid-range"
        },
        {
            "id": 5,
            "name": "لاہور چٹخارہ",
            "cuisine": "دیسی",
            "price-range": "mid-range"
        },
        {
            "id": 6,
            "name": "واسابی",
            "cuisine": "English",
            "price-range": "cheap"
        }
    ]
    if cuisine:
        return [restaurant for restaurant in restaurants if
                restaurant['cuisine'] == cuisine], "یہ ہیں کچھ مشہور {} ریسٹورنٹس".format(cuisine)
    else:
        return restaurants, "یہ ہیں کچھ مشہور ریسٹورنٹس"


def get_hotels():
    hotels = [
        {
            "id": 0,
            "name": "پی سی ہوٹل",
            "price-range": "expensive",
            "city": "Lahore",
            "star-rating": 5,

        },
        {
            "id": 1,
            "name": "دی نشاط ہوٹل",
            "price-range": "expensive",
            "city": "Lahore",
            "star-rating": 4,
        },
        {
            "id": 2,
            "name": "فیملی ہوٹل",
            "price-range": "mid-range",
            "city": "Lahore",
            "star-rating": 4,
        },
        {
            "id": 3,
            "name": "سٹپ ان ہوٹل",
            "price-range": "mid-range",
            "city": "Lahore",
            "star-rating": 4,
        },
        {
            "id": 4,
            "name": "لاہور پیلس ہوٹل",
            "price-range": "expensive",
            "city": "Lahore",
            "star-rating": 4,
        }
    ]
    return hotels, "یہ ہیں کچھ مشہور ہوٹلز"


class ActionQueryDatabase(Action):
    def name(self):
        return "action_query_database"

    def run(self, dispatcher, tracker, domain):
        restaurant = tracker.get_slot("restaurant")
        hotel = tracker.get_slot("hotel")
        cuisine = tracker.get_slot("cuisine")
        results = [{"name": "دی لکھنوی"}]
        message = ""
        if restaurant or cuisine:
            results, message = get_restaurants(restaurant=restaurant, cuisine=cuisine)
        elif hotel:
            results, message = get_hotels()
        dispatcher.utter_message(message)
        # limit to top 5 queries
        for i, obj in enumerate(results[:5]):
            dispatcher.utter_message(str(i + 1) + " - " + obj['name'])
        return []