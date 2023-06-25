import configuration
import requests
import data
'''
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count":5})

response_log = get_logs()
print(response_log.status_code)
print(response_log.headers)
print(response_log.text)
'''
'''
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response_tab = get_users_table()
print (response_tab.status_code)
print (response_tab.text)
'''
'''
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # здесь заголовки

user_token = post_new_user(data.user_body); #ответ можно назвать как хочешь
print(user_token.status_code)
print(user_token.json())
print(user_token.text)
'''
# А МОЖНО И ТАК НО НЕЛЬЗЯ
# def post_new_user():
#     return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
#                          json=data.user_body,
#                          headers=data.headers)
# respone_token = post_new_user()
# print(respone_token.text)
'''
def post_products_kits(product_ids):
    return requests.post (configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                          json=product_ids,
                          headers=data.headers)
response_ids=post_products_kits(data.product_ids)
print(response_ids.status_code)
print(response_ids.json())
'''
