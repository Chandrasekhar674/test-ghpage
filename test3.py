import requests
res = requests.get('https://api.github.com/repos/chandrasekhar674/test-ghpage/branches/main/protection', auth=('chandrasekhar674', '$Chandra@1667'))
print (res.status_code)
print (res.headers['content-type'])
print(res.content.decode('utf-8'))