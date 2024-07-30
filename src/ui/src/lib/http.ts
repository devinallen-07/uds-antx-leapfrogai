const BASE_URL = 'http://localhost:8000';

interface APIRequest<T> {
    method: 'GET' | 'POST' | 'PUT' | 'DELETE';
    path: string;
}

export class HTTP {
    get<T>(path: string) {
        return this.request<T>({ method: 'GET', path });
    }

    private async request<T>(req: APIRequest<T>): Promise<T> {
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
                throw new Error('HTTP request failed: ' + response.statusText);
            }
            return await response.json() as T;
        } catch (e) {
            console.error(e);
            return Promise.reject(e);
        }
    }
}