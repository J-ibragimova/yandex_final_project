#Ибрагимова Юлия, 39 когорта- Финальный проект. Инжинер по тестированию плюс
# Импортируем модуль request
import request
# Импортируем модуль data
import data

def test_get_order_info_by_track():
    track = request.create_order(data.order_body).json()['track']
    response = request.get_order_info_by_track(track)
    assert response.status_code == 200

test_get_order_info_by_track()