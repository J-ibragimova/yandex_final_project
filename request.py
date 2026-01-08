import configuration
import requests
import data

def create_order(order_body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)

print(create_order(data.order_body).status_code)

def get_order_info_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION + str(track_number))

track = create_order(data.order_body).json()['track']
print(get_order_info_by_track(track).status_code)