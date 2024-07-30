const BASE_URL = 'https://api.uds.dev';

interface APIRequest<T> {
	method: 'GET' | 'POST' | 'PUT' | 'DELETE';
	path: string;
}

const headers = new Headers({
	'Content-Type': 'application/json',
	'Access-Control-Allow-Origin': '*'
});

export class HTTP {
	get<T>(path: string) {
		return this.request<T>({ method: 'GET', path });
	}

	private async request<T>(req: APIRequest<T>): Promise<T> {
		const url = BASE_URL + req.path;
		const payload: RequestInit = { method: req.method, headers, mode: 'no-cors' };
		console.log('HTTP request URL: ', url);

		try {
			const response = await fetch(url, payload);

			if (!response.ok) {
				throw new Error('HTTP request failed: ' + response.statusText);
			}

			return (await response.json()) as T;
		} catch (e) {
			console.error(e);
			return Promise.reject(e);
		}
	}
}
