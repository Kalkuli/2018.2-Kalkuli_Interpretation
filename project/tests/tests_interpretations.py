import json
import unittest

from flask_testing import TestCase

from project import create_app


class TestInterpretation(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def test_extract_total_price(self):

        with self.client:
            response = self.client.post(
                '/interpret', 
                data = json.dumps({
                    "raw_text": "Valor Total R$ 234,21"
                }), 
                content_type = "application/json"
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertAlmostEqual(234.21, data['total_price'], 2)

    def test_date(self):
        
        with self.client:
            response = self.client.post(
                '/interpret', 
                data = json.dumps({
                    "raw_text": "Data da Autorização: 02/03/2143"
                }), 
                content_type = "application/json"
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('2143-03-02', data['date'])

    def test_cnpj(self):
    
        with self.client:
            response = self.client.post(
                '/interpret', 
                data = json.dumps({
                    "raw_text": "CNPJ - 00.000.000/0000-00"
                }), 
                content_type = "application/json"
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('00.000.000/0000-00', data['cnpj'])

    def test_all_fields(self):

        with self.client:
            response = self.client.post(
                '/interpret', 
                data = json.dumps({
                    "raw_text": "CNPJ - 00.000.000/0000-00, Data da Autorização: 02/03/2143\nValor Total R$ 234,21"
                }), 
                content_type = "application/json"
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertAlmostEqual(234.21, data['total_price'], 2)
            self.assertIn('2143-03-02', data['date'])
            self.assertIn('00.000.000/0000-00', data['cnpj'])

    def test_total_price_not_found(self):

        with self.client:
            response = self.client.post(
                '/interpret', 
                data = json.dumps({
                    "raw_text": ""
                }), 
                content_type = "application/json"
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('', data['total_price'])

    def test_date_not_found(self):
        
        with self.client:
            response = self.client.post(
                '/interpret', 
                data = json.dumps({
                    "raw_text": ""
                }), 
                content_type = "application/json"
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('', data['date'])

    def test_cnpj_not_found(self):
    
        with self.client:
            response = self.client.post(
                '/interpret', 
                data = json.dumps({
                    "raw_text": ""
                }), 
                content_type = "application/json"
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('', data['cnpj'])

    def test_empty_json(self):

        with self.client:
            response = self.client.post(
                '/interpret', 
                data = json.dumps({}), 
                content_type = "application/json"
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()