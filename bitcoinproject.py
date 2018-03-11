import requests
bitcoin_url ='https://api.coinmarketcap.com/v1/ticker/bitcoin/'
#response_ans= requests.get(bitcoin_url)
#response_json=response_ans.json()
#print(response_json)
ifttt_webhooker= 'https://maker.ifttt.com/trigger/test_event/with/key/mfrV2_Gx1O5iFlHvYbyvdKa39zrp8avC40xKXEH5Wcg'
resp=requests.post(ifttt_webhooker)
print(resp)
