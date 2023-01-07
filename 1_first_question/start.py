import requests

def consumirApi():
    result = requests.get('https://jsonplaceholder.typicode.com/comments')
    print(result.content)

if __name__ == '__main__':
    consumirApi()
