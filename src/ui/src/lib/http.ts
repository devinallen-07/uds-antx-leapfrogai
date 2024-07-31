const BASE_URL = 'http://localhost:8000';

interface APIRequest<T> {
	method: 'GET' | 'POST' | 'PUT' | 'DELETE';
	path: string;
}

interface APIResponse<T> {
	data: T | null;
	error: string | null;
}

export class HTTP {
	private useTestData: boolean = false; // Gud code practice idiot... shut up man. I'll set up tests later loser mean face

	get<T>(path: string): Promise<APIResponse<T>> {
		return this.request<T>({ method: 'GET', path });
	}

	private async request<T>(req: APIRequest<T>): Promise<APIResponse<T>> {
		if (this.useTestData) {
			return this.getTestData<T>(req.path);
		}

		const url = BASE_URL + req.path;
		const headers = new Headers();

		if (req.method !== 'GET') {
			headers.append('Content-Type', 'application/json');
		}

		const payload: RequestInit = { method: req.method, headers };
		console.log('HTTP request URL: ', url);

		try {
			const response = await fetch(url, payload);

			if (!response.ok) {
				console.log(response);
				return {
					data: null,
					error: `HTTP request failed: ${response.status} ${response.statusText}`
				};
			}

			const data = (await response.json()) as T;
			return { data, error: null };
		} catch (e) {
			console.error(e);
			return {
				data: null,
				error: e instanceof Error ? e.message : 'Unknown error occurred'
			};
		}
	}

	private getTestData<T>(path: string): Promise<APIResponse<T>> {
		const testData = {
			metadata: {
				eventStart: '2024-07-31T10:37:50',
				timeToNextEvent: '01:15',
				runningClock: '32:28'
			},
			state: {
				currentState: 'Trial Start',
				delay: null
			},
			transcription: {
				speechToText: [
					'2024-07-31T10:37:50: ICOM: ',
					'2024-07-31T10:37:50: TD: ',
					'2024-07-31T10:37:50: CG: ',
					'2024-07-31T10:37:50: CG: words are here copy'
				]
			},
			performanceMetrics: {
				timeToTranscribePerToken: {
					min: 0.0,
					max: 0.0,
					avg: 0.0
				},
				timeToInference: {
					min: 0.0,
					max: 0.0,
					avg: 0.0
				}
			}
		};

		// Simulate a delay to mimic network request
		return new Promise((resolve) => {
			setTimeout(() => {
				resolve({ data: testData as T, error: null });
			}, 100);
		});
	}
}
