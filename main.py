import requests


url = 'https://apply-to-avantos.dev-sandbox.workload.avantos-ai.net'
data = {
    'email': 'josephsonreynoso@gmail.com'
    }

response = requests.post(url, json=data)

print('Status Code:', response.status_code)