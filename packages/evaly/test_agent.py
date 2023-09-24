from evaly import Client

# Initialize the client
client = Client(api_key="evk-467e7458-7bda-4673-97ad-951a87b9eda8")

# Log a prediction
response = client.log_prediction(
    model_id='sample-model-1',
    features={
        'feature1': 'value1',
        'feature2': 'value2',
    },
    tags={
        'tag1': 'value1',
        'tag2': 'value2',
    }
)

# Log an actual
response = client.log_actual(
    model_id='sample-model-1',
    actual_label='True',
    tags={
        'tag1': 'value1',
        'tag2': 'value2',
    }
)
