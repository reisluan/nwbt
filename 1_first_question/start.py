# Import libraries into the project
import requests
import json


# Function to consume API
def consume_api():
    request = requests.get('https://jsonplaceholder.typicode.com/comments')
    return json.loads(request.content)


# Function to display results
def print_mail(result_json):
    for item in result_json:
        tld = item['email'][-4:]
        if tld == '.org':
            print(item['email'])


# Run only if file is called directly
if __name__ == '__main__':
    result = consume_api()
    print_mail(result)

