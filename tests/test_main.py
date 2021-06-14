from unittest import TestCase


class Test(TestCase):
    
    def test_login(self):
        response = client.post("/login", json={"rut": "0108124970", "password": "YWRtaW4wMQ=="})
        assert response.status_code == 200
        assert response.json() == {"code": "002", "name": "CRISTIAN PAVEZ GALVEZ", "rut": "0108124970", "token": "123"}
        self.fail()
