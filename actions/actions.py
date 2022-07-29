from operator import ne
from typing import Any, Iterator, Text, Dict, List
from dateutil import parser

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from regex import I
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
            input_data3 = next(tracker.get_latest_entity_values("object"), "x")
            #print(input_data3)
            input_data4 = next(tracker.get_latest_entity_values("time"),".")
            # if input_data4 != ".":
            #     print(parser.parse(input_data4).month)
            input_data = input_data1 + "~"+ input_data2 +"~"+input_data3+"~"+input_data4
            print(input_data)
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
            input_data3 = next(iterator2,"x")
            input_data4 = next(iterator1,".")
            input_data5 = next(iterator2,"x")       
            #print(input_data3)
            input_data = input_data1 + "~"+ input_data2 +"~"+input_data3+"~"+input_data4+"~"+input_data5
            print(input_data)
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
            iterator = tracker.get_latest_entity_values("object")
            input_data1 = next(iterator,"x")
            input_data2 = next(tracker.get_latest_entity_values("predicate"),".")
            #print(input_data1)
            if input_data1 != "x":
                input_data3 = next(iterator,"x")
            else:
                input_data3 = "x"
            input_data = input_data1 + "~"+ input_data2 +"~" +input_data3 
            print(input_data)   
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
            iterator = tracker.get_latest_entity_values("object")
            input_data1 = next(iterator, "x")  
            if input_data1 != "x":
                input_data2 = next(iterator,"x")
            else:
                input_data2 = "x"
            input_data = input_data1+"~"+input_data2
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
            input_data = next(tracker.get_latest_entity_values("object"),"x") 
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
            iterator = tracker.get_latest_entity_values("object")
            input_data1 = next(iterator, "x")  
            if input_data1 != "x":
                input_data2 = next(iterator,"x")
            else:
                input_data2 = "x"
            input_data3 = next(tracker.get_latest_entity_values("predicate"),".")
            input_data = input_data1+"~"+input_data2+"~"+input_data3 
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
            input_data = next(tracker.get_latest_entity_values("object"), "x")
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
            input_data1 = next(tracker.get_latest_entity_values("object"), "x")      
            input_data2 = next(tracker.get_latest_entity_values("class"),".")  
            input_data = input_data1+"~"+input_data2   
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