import requests
import json
import os
import urllib3
urllib3.disable_warnings()

ROCK_API_KEY = os.environ.get('ROCK_API_KEY')
HANDLES = [
  'CoryBooker',
  'PeteButtigieg',
  'JulianCastro',
  'JohnDelaney',
  'TulsiGabbard',
  'SenGillibrand',
  'KamalaHarris',
  'Hickenlooper',
  'jayinslee',
  'amyklobuchar',
  'BernieSanders',
  'SenWarren',
  'AndrewYangVFA',
  'marwilliamson',
  'BetoORourke',
  'JoeBiden',
  'AndrewGillum',
  'BilldeBlasio'
]

for handle in HANDLES:
  r = requests.get('https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names=%s' % handle)
  res = json.loads(r.text)[0]
  doc = {
    'handle': str(res['screen_name']),
    'followers': res['followers_count']
  }

  requests.post(
    'https://api.rs2.usw2.rockset.com/v1/orgs/self/ws/yang/collections/twitter_followers/docs',
    headers={'Authorization': 'ApiKey %s' % ROCK_API_KEY, 'Content-Type': 'application/json'},
    data=json.dumps({'data': [doc]})
  )

