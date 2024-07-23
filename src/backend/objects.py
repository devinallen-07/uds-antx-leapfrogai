from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class CurrentState(Enum):
   pre_trial_start = "Pre Trial Start"
   trial_start = "Trial Start"
   trial_end = "Trial End"
   delay_start = "Delay Start"
   delay_end = "Delay End"
   in_transit = "In Transit"
   mistrial = "Mistrial"
   rtb = "RTB"

class DelayReason(Enum):
   vendor = "Vendor"
   npc = "NPC"
   software = "Software"
   towing = "Towing"

class EventMetaData(BaseModel):
   eventStart: str = Field(description = "YYYY-MM-DDTHH:MM:SS datetime format", examples=['2024-04-01T17:32:47'])
   timeToNextEvent: str = Field(description = "HH:MM:SS format for eplased time", examples=['00:5:12'])
   runningClock: str = Field(description = "HH:MM:SS format for elapsed time", examples=['00:11:47'])

class Delay(BaseModel):
   reason: DelayReason
   predictedResolutionTime: str = Field(description="YYYY-MM-DDTHH:MM:SS datetime format", examples=['2024-04-01T17:32:47'])

class State(BaseModel):
   currentState: CurrentState
   delay: Optional[Delay] = None

#TODO: Flesh out the transcription schema
class Transcription(BaseModel):
   speechToText: List[str]

class Metric(BaseModel):
   min: float
   max: float
   avg: float

class PerformanceMetrics(BaseModel):
   timeToTranscribePerToken: Metric
   timeToInference: Metric

class Update(BaseModel):
   metadata: EventMetaData
   state: State = Field(description="The current state")
   transcription: Transcription = Field(description="List of transcriptions?")
   performanceMetrics: PerformanceMetrics

class LastUpdate(BaseModel):
   updateTime: str = Field(description = "YYYY-MM-DDTHH:MM:SS datetime format", examples=['2024-04-01T17:32:47'])
   lastState: State = Field(description="The current state")