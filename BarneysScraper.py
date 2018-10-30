import requests, json, time, urllib 


def Bscrape(pidlist):
	
	headers = {
			'Host': 'www.barneys.com' ,                              
			'Connection': 'keep-alive'  ,                                                                              
			'x-oc-client-id': 'FRIRgVKHoj1zkFoOqkwncsKE5Fc6ku2C' ,                                                        
			'Accept': '*/*' ,                                                                                     
			'User-Agent': 'Barneys/26 (iPhone; iOS 10.1.1; Scale/2.00)' ,                                              
			'Accept-Language': 'en-US, en-us;q=0.8' ,                                                                   
			'Authorization': 'Basic c3RvcmVmcm9udDpiYXJuZXlz' ,                                                          
			'Accept-Encoding': 'gzip, deflate' ,   
	}

	sizeIDlist = []
	stockList = []


	for PID in pidlist :

		sizeIDlist[:] = []
		stockList[:] = []

		string = ''

		r = requests.get('https://www.barneys.com/rest/model/barneys/commerce/catalog/BNYProductDetailDisplayActor/getProductDetailsPageInfo?productId=%s' % PID , headers = headers)

		data = json.loads(r.text)

		inventoryData = json.loads(json.dumps(data['inventoryDetails']))
		skuInventoryData = json.loads(json.dumps(inventoryData['skuInventoryStatus']))

		prodData = json.loads(json.dumps(data['productDetails']))
		prodData2 = json.loads(json.dumps(prodData[0]))
		atrData = json.loads(json.dumps(prodData2['attributes']))

		category = str(atrData['parentCategory.displayName'][0])
		skuData = json.loads(json.dumps(skuInventoryData['skuInventoryATP']))
		images = atrData['product.auxImageURLS']
		creationDate = str(time.ctime(int(str(atrData['product.creationDate'][0]))))
		dateAvalable = str(time.ctime(int(str(atrData['product.dateAvailable'][0]))))
		designer = atrData["product.designer"][0]
		name = atrData['product.displayName'][0]
		price = atrData['product.maxPrice'][0]
		url = 'http://www.barneys.com/' + str(atrData['product.productDetailPageUrl'][0])
		respID = atrData['product.repositoryId'][0]
		sizes = atrData['sku.realSize']

		string = ('Name : %s\nBrand : %s\nCategory : %s\nPrice : $%s0\nCreated at %sAvalable at %sURL : %s\nRespitory ID : %s\n\n' % (name, designer, category, price, creationDate, dateAvalable, url, respID))
		string += 'Images :\n'
		
		for i in images :
			string += ('\t' + i[16:len(i)] + '\n')

		string += '\n'

		for sizeID, stock in skuData.iteritems():
			sizeIDlist.append(sizeID)
			stockList.append(stock)
		
		string += 'Sizes : \n'
		for sz, szID, stk in zip(sizes, sizeIDlist, stockList) :
			string += ('\tSize : %s - PID : %s - Stock : %s\n ' % (sz, szID, stk))

		txtName = str(respID) + '.txt'
		
		txt = open(txtName, 'w')
		txt.write(string)
		txt.close()


def bImageScrape(start, stop):
	while start <= stop :
		r = requests.get('https://product-images.barneys.com/is/image/Barneys/%s' % start)
		
		if r.status_code == 200 :
			resource = urllib.urlopen('https://product-images.barneys.com/is/image/Barneys/%s' % start)
			output = open(('%s.jpg' % start ),"wb")
			output.write(resource.read())
			output.close()
		else :
			pass 

		start += 1

bImageScrape(504742690, 504742691)














