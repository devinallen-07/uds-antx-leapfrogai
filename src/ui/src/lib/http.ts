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
	get<T>(path: string): Promise<APIResponse<T>> {
		return this.request<T>({ method: 'GET', path });
	}

	private async request<T>(req: APIRequest<T>): Promise<APIResponse<T>> {
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
}
