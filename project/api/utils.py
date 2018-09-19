import re
import datetime

class Interpreter:
    def __init__(self, raw_text):
        self.raw_text = raw_text

    def find_total_price(self):
        price_regex = re.compile(r'valor total r\$ \d+[,.]\d{2}')
        list_prices = price_regex.findall(self.raw_text)

        price_text = list_prices[0]

        # the value is always going to be at the fourth position in the list
        price_value = price_text.split()[3]
        price_value = price_value.replace(',', '.')
        price_value = float(price_value)

        return price_value

    def find_date(self):
        date_regex = re.compile(r'\d{2}/\d{2}/\d{4}')
        list_date = date_regex.findall(self.raw_text)

        date_text = list_date[0]

        date = datetime.datetime.strptime(date_text, '%d/%m/%Y').date()

        return date

    def find_cnpj(self):
        cnpj_regex = re.compile(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}')
        list_cnpj = cnpj_regex.findall(self.raw_text)

        cnpj_text = list_cnpj[0]
        return cnpj_text

    def interpret_text(self):
        total_price = self.find_total_price()
        date = self.find_date()
        cnpj = self.find_cnpj()

        return {
            "total_price": total_price,
            "date": date.isoformat(),
            "cnpj": cnpj
        }