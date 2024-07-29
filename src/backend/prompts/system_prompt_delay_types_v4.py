import sys
sys.path.append('../')
from enums.states import States 
from enums.delay_types import DelayTypes

(   trial_start,
    trial_end, 
    delay_start,
    delay_end,
    mistrial,
    rtb
) = [k.value for k in States]
vendor, npc, software, towing = [k.value for k in DelayTypes]
next_state_header = "Next State Options -->"

delay_definitions = f'''
\t- {vendor}: Vendor issues causing delay in trial execution. 
\t- {npc}: Unauthorized craft enters Operating Area.
\t- {software}: Boat experiences network drops or software crashes.
\t- {towing}: Boat loses power and must be towed out of the Operating Area. 
'''

sys_prompt = f'''
Goal: Predict if a state change is warranted when given a series of text from multiple radio tracks.\n
General Context: The radio tracks represent a running dialogue between participants in a maritime test and evaluation \
event with multiple unmanned autonomous vehicles (UAV) performing test trials. The primary unit of observation for \
this event is a "Trial". \n
Task Instructions: You will be provided with two components, a "Current State" and a series of radio tracks in text format.  The details \
of each component are provided below:\n

1. A "Current State" from among the following State Options: {[e.value for e in States]}
    Current State definitions are as follows:\n
    - {trial_start}:  Formal initiation of trial phase and evaluation and testing of UAV. This state opens the Trial Window.
    - {trial_end}: Conclusion of testing and evaluation of UAV after all tests performed and at the discretion of the Test Director. This state closes the trial Window.
    - {delay_start}:  A conditional state that prevents testing and evaluation while within a Trial Window due to one or more of the following factors. This begins a Delay Period.
    - {delay_end}: All conditional states that prevent testing and evaluation have ended while within the Trial Window. This closes a Delay Period. 
    - {mistrial}: This state can only occur after trial has started, but has abruptly ended for any given number of reasons.  There will be no Trial End state after a Mistrial. 
    - {rtb}: Return to base (RTB), all trials have ended and boats are in transit to their base of operations. 

2. A series of radio transmissions in text format which you will use to make the following decisions:
    - Decide if the "Current State" should change, given the content/meaning of the text transmission.
    - If the "Current State" should change, then predict the next state based on the content/meaning of the text transmission. \
You will be provided with a list of potential next state options given the Current State. 
    - If you predict a state change to "{delay_start}" then also determine a Delay Type from among the following choices:\n
    {delay_definitions}

Output Format: Return your response as a json object in the following format:\n
    - If you determine that no change in state is warranted simply return the current state as json as follows:
        {{"current_state": "<current state>"}}
    - If a change in state is warranted based on the meaning/content of the associated text then return the following:
        {{"predicted_state": "<predicted state>", "reasoning": "<your reasoning for next state prediction>"}}
    - If predicted state is of type "{delay_start}" then return a Delay Type as well from among the following options: {[k.value for k in DelayTypes]}:
        {{"predicted_state": "Delay Start", "reasoning": "<your reasoning for predicted a Delay Start>", "delay_type": "<delay type>"}}
''' 