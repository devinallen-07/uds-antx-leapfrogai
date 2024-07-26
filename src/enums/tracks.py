from enum import Enum

class Tracks(Enum):
    track1: str='Boat Operators'
    track2: str='Motorola Radios'
    track3: str='Test Director'
    track4: str='Patrol Craft Command Unit (PCCU)'

track_mapping = {
    Tracks.track1.name : Tracks.track1.value,
    Tracks.track2.name : Tracks.track2.value,
    Tracks.track3.name : Tracks.track3.value,
    Tracks.track4.name : Tracks.track4.value
}