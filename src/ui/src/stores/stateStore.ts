import { writable } from 'svelte/store';
import type { EventInformation } from '$lib/schema'; // Import the type from wherever you've defined it

export const eventStore = writable<EventInformation>({
	metadata: {
		eventStart: new Date().toDateString(),
		timeToNextEvent: '00:00',
		runningClock: 'HH:MM:SS'
	},
	state: {
		currentState: 'Pre Trial Start',
		delay: null
	},
	transcription: [],
	performanceMetrics: {
		timeToTranscribePerToken: {
			min: 0,
			max: 0,
			avg: 0
		},
		timeToInference: {
			min: 0,
			max: 0,
			avg: 0
		}
	}
});

export function updateEventStore(data: Partial<EventInformation>) {
	eventStore.update((currentState) => ({
		...currentState,
		...data
	}));
}
