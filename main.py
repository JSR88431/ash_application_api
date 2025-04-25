import requests


url = 'https://apply-to-avantos.dev-sandbox.workload.avantos-ai.net'
data = {
    'email': 'josephsonreynoso@gmail.com'
    }

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/133.0.0.0 Safari/537.36'
}

response = requests.post(url, json=data)

print('Status Code:', response.status_code)