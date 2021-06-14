from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login():
    response = client.post("/login", json={	"rut" : "0108124970", "password": "YWRtaW4wMQ=="})
    assert response.status_code == 200
    assert response.json() == {  "code": "002",  "name": "CRISTIAN PAVEZ GALVEZ",  "rut": "0108124970",  "token": "123" }

def test_read_routes():
    pass

def test_read_sellers():
    pass

def test_read_seller_by_rut():
    pass

def test_get_sell_conditions():
    pass

def test_read_clients_of_seller_and_route():
    pass

def test_read_client_by_rut():
    pass

def test_read_client_by_rut_and_code():
    pass

def test_read_pieces_by_code():
    pass

def test_delete_pieces_by_correlative():
    pass

def test_read_products():
    pass

def test_read_fast_products():
    pass

def test_read_product_by_code():
    pass

def test_read_fast_product_by_code():
    pass

def test_read_header_of_sales_of_client():
    pass

def test_read_detail_of_sales_of_client():
    pass

def test_register_item_temporal_sale():
    pass

def test_delete_register_item_temporal_sale():
    pass

def test_delete_register_item_temporal_sale():
    pass

def test_register_sales_by_sale():
    pass

def test_list_sales():
    pass

def test_list_sales_by_sale():
    pass


def test_list_sale_by_sale_by_rut_by_date():
    pass

def test_list_one_sale_by_sale_by_rut_by_date():
    pass

def test_list_sale_by_sale_by_rut_by_date():
    pass

def test_get_configuration():
    pass

def test_list_last_positions():
    pass

def test_positions():
    pass

def test_message_stream():
    pass

def test_registers_log():
    pass

def test_registers_log_vendedor():
    pass

def test_registers_log_fecha():
    pass

def test_registers_log_code_fecha():
    pass





