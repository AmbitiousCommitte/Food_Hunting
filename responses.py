from random import choice, randint
from typing import List, Dict
from get_food_event import check_login, open_food_page, find_events
def get_response(user_input : str) -> str:
    lowered: str = user_input.lower()
    if lowered[0] != "!":
        return None
    lowered = lowered[1:]
    if lowered == '':
        return 'Well, you\'re silent...'
    elif lowered.startswith('hello'):
        return 'Hello there!'
    elif lowered.startswith('good?'):
        return 'Good, thanks!'
    elif lowered.startswith('bye'):
        return 'See you!'
    elif lowered.startswith('dice'):
        return f'You rolled: {randint(1,6)}'
    elif lowered.startswith('events'):
        data = get_data()
        names=[]
        events = []
        for name,event_list in data.items():
            for event in event_list:
                events.append(event)
                names.append(name)
        formatted_events = []
        for i in range(len(events[:10])):
            one_event = f"Event {i+1}: {names[i]} \nLocation: {events[i]['location']} \nTime: {events[i]['time']}\n"
            formatted_events.append(one_event)
        return '\n'.join(formatted_events)
    elif lowered.startswith('help'):
        return """!hello: Say hello to users \n good?: My feeling now \n !bye: Say goodbye to Bot \n !dice: How lucky are you today \n !events: List of food events today \n !help: Showing this lists"""
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that?'])
    

#def generate_data(name, time, location, URL):
    ##   'name': name,
     #   'time': time,
     #   'location': location,
     #   'URL': URL
   # }


def get_data() -> Dict[str, List[Dict[str, str]]]:
    check_login()
    open_food_page()
    events = find_events()
    data = {}
    for event in events:
        event_name = event['name']
        data[event_name] = [{
            "id": event['id'],
            "tags": event['tags'],
            "date": event['date'],
            "time": event['time'],
            "location": event['location']
        }]
    return data

if __name__ == "__main__":
    cmd='!events'
    output=get_response(cmd)
    print(output)
    
