import requests

class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://127.0.0.1:8000"  # Replace with your actual server URL

    def log_prediction(self, model_id, features, tags=None):
        url = f"{self.base_url}/log_prediction"
        headers = {'Authorization': self.api_key}
        data = {
            'model_id': model_id,
            'features': features,
            'tags': tags,
        }
        response = requests.post(url, headers=headers, json=data)
        return response

    def log_actual(self, model_id, actual_label, tags=None):
        url = f"{self.base_url}/log_actual"
        headers = {'Authorization': self.api_key}
        data = {
            'model_id': model_id,
            'actual_label': actual_label,
            'tags': tags,
        }
        response = requests.post(url, headers=headers, json=data)
        return response
