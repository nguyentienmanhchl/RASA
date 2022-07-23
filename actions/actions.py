from typing import Any, Iterator, Text, Dict, List
from dateutil import parser

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import UserUtteranceReverted

    
class ActionOneCondition(Action):
    def name(self) -> Text:
        return "action_one_condition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            input_data1 = next(tracker.get_latest_entity_values("class"), ".")
            input_data2 = next(tracker.get_latest_entity_values("predicate"), ".")
            input_data3 = next(tracker.get_latest_entity_values("object"), None)
            print(input_data3)
            input_data4 = next(tracker.get_latest_entity_values("time"),".")
            # if input_data4 != ".":
            #     print(parser.parse(input_data4).month)
            input_data = input_data1 + "~"+ input_data2 +"~"+input_data3+"~"+input_data4
            r = requests.get("http://localhost:8080/one_condition",data=input_data.encode('utf-8'))
       
            dispatcher.utter_message(
                text="{}".format(r.content.decode()))
        except:
            dispatcher.utter_message(
                text = "Tôi không biết.")
        return []    
class ActionTwoConditions(Action):
    def name(self) -> Text:
        return "action_two_conditions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            input_data1 = next(tracker.get_latest_entity_values("class"), ".")
            iterator1 = tracker.get_latest_entity_values("predicate")
            iterator2 = tracker.get_latest_entity_values("object")
            input_data2 = next(iterator1,".")
            input_data3 = next(iterator2,None)
            input_data4 = next(iterator1,".")
            input_data5 = next(iterator2,None)       
            print(input_data3)
            input_data = input_data1 + "~"+ input_data2 +"~"+input_data3+"~"+input_data4+"~"+input_data5
            r = requests.get("http://localhost:8080/two_conditions",data=input_data.encode('utf-8'))
       
            dispatcher.utter_message(
                text="{}".format(r.content.decode()))
        except:
            dispatcher.utter_message(
                text = "Tôi không biết.")

        return []           

class ActionAskOneProperty(Action):
    def name(self) -> Text:
        return  "action_ask_one_property"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            input_data1 = next(tracker.get_latest_entity_values("object"), None)
            input_data2 = next(tracker.get_latest_entity_values("predicate"),".")
            print(input_data1)

            input_data = input_data1 + "~"+ input_data2 

            r = requests.get("http://localhost:8080/ask_one_property",data=input_data.encode('utf-8'))
       
            dispatcher.utter_message(
                text="{}".format(r.content.decode()))
        except:
            dispatcher.utter_message(
                text = "Tôi không biết.")
        return []          

class ActionAskAll(Action):
    def name(self) -> Text:
        return  "action_all"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            input_data = next(tracker.get_latest_entity_values("object"), None)  
            print(input_data)         
            r = requests.get("http://localhost:8080/all",data=input_data.encode('utf-8'))       
            dispatcher.utter_message(
                text="{}".format(r.content.decode()))
        except:
            dispatcher.utter_message(
                text = "Tôi không biết.")
        return []     



class ActionAskDenChua(Action):
    def name(self) -> Text:
        return  "action_ask_den_chua"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            input_data = next(tracker.get_latest_entity_values("object"), None) 
            print(input_data)          
            r = requests.get("http://localhost:8080/ask_den_chua",data=input_data.encode('utf-8'))       
            dispatcher.utter_message(
                text="{}".format(r.content.decode()))
        except:
            dispatcher.utter_message(
                text = "Tôi không biết.")
        return []   

class ActionAskAboutArea(Action):
    def name(self) -> Text:
        return  "action_ask_about_area"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            input_data = next(tracker.get_latest_entity_values("object"), None)   
            print(input_data)        
            r = requests.get("http://localhost:8080/ask_about_area",data=input_data.encode('utf-8'))       
            dispatcher.utter_message(
                text="{}".format(r.content.decode()))
        except:
            dispatcher.utter_message(
                text = "Tôi không biết.")
        return [] 

class ActionAskArea(Action):
    def name(self) -> Text:
        return  "action_ask_area"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            input_data = next(tracker.get_latest_entity_values("object"), None)
            print(input_data)          
            r = requests.get("http://localhost:8080/ask_area",data=input_data.encode('utf-8'))       
            dispatcher.utter_message(
                text="{}".format(r.content.decode()))
        except:
            dispatcher.utter_message(
                text = "Tôi không biết.")
        return []   

class ActionAskRelate(Action):
    def name(self) -> Text:
        return  "action_ask_relate"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            input_data = next(tracker.get_latest_entity_values("object"), None)           
            print(input_data)
            r = requests.get("http://localhost:8080/ask_relate",data=input_data.encode('utf-8'))       
            dispatcher.utter_message(
                text="{}".format(r.content.decode()))
        except:
            dispatcher.utter_message(
                text = "Tôi không biết.")
        return []                   

# class ActionFallback(Action):
#     def name(self) -> Text:
#         return  "utter_please_rephrase"


#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         input_data = next(tracker.get_latest_entity_values("object"), None)           
#         print(input_data)
           
        
#         dispatcher.utter_message(
#             text = "Xin lỗi mình không hiểu câu hỏi, bạn diễn đạt lại được không?")
#         return [UserUtteranceReverted()]    