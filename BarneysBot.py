import requests, json, time

class BnyBot :

    def t(self):
        return time.strftime('%H:%M:%S', time.localtime())

    def checkout(self, name):

        sesh = requests.Session()

        print ('[{}] : {} - started checkout'.format(self.t(), name))


        addHeaders = {
            'Host':             'www.barneys.com',
            'Content-Type':     'application/json; charset=utf-8',
            'Connection':       'keep-alive ',
            'x-oc-client-id':   'FRIRgVKHoj1zkFoOqkwncsKE5Fc6ku2C',
            'Accept':           '*/*',
            'User-Agent':       'Barneys/24 (iPhone; iOS 10.1.1; Scale/2.00)',
            'Accept-Language':  'en-US, en-us;q=0.8',
            'Authorization':    'Basic c3RvcmVmcm9udDpiYXJuZXlz',
            'Accept-Encoding':  'gzip, deflate'
        }
        addData = {
            "catalogRefIds": "00505050462773",
            "productId": "505046272",
            "quantity": "1",
            "siteId": "BNY"
        }


        add = sesh.post('https://www.barneys.com/rest/model/atg/commerce/order/purchase/BNYCartModifierActor/addItemToOrder', data = json.dumps(addData), headers = addHeaders)

        addyData = {
            "address1": "3372 Brenner Road",
            "city": "Barberton",
            "country": "US",
            "firstName": "Lyle",
            "giftMessageFlag": "false",
            "giftWrap": "false",
            "lastName": "Londraville",
            "phoneNumber": "(330) 603-1362",
            "postalCode": "44203",
            "saveShippingAddress": False,
            "state": "OH"
        }

        addy = sesh.post('https://www.barneys.com/rest/model/barneys/userprofiling/BNYCheckoutShippingActor/shipToNewAddress', data = json.dumps(addyData), headers = addHeaders)

        shipData = {
            "shippingMethod": "Ground"
        }

        ship = sesh.post('https://www.barneys.com/rest/model/barneys/userprofiling/BNYCheckoutShippingActor/updateShippingMethod', data = json.dumps(shipData), headers = addHeaders)


b = BnyBot()

data = {
    'email' : 'Kixify1140@gmail.com',
    'first' : 'Lyle',
    'last' : 'Londraville',
    'addy' : '3372 Brenner road',
    'city' : 'norton',
    'zip' : '44203',
    'state' : 'OH',
    'phone' : '(330) 603-1362',

    'card' : '4270829038257603',
    'month' : '9',
    'year' : '2020',
    'cvv' : '124'

}
#b.checkout('Bny 1')

tempStr = ''

o = open('BNYxml.txt', 'r')


for i in o:

    string = i

    string.replace('FIRST NAME HERE', data['first'])
    string.replace('LAST NAME HERE', data['last'])
    string.replace('ADDRESS HERE', data['addy'])
    string.replace('CITY HERE', data['city'])
    string.replace('STATE INITALS HERE', data['state'])
    string.replace('ZIP CODE HERE', data['zip'])
    string.replace('PHONE HERE', data['phone'])
    string.replace('EMAIL HERE', data['email'])

    string.replace('CARD NUMBER HERE', data['card'])
    string.replace('EXPERATION MONTH HERE', data['month'])
    string.replace('EXPERATION YEAR HERE', data['year'])
    string.replace('CVV HERE', data['cvv'])

    tempStr += string

print (tempStr)



o.close()