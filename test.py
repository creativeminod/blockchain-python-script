from blockchain import createwallet

wallet = createwallet.create_wallet('1234password', '58ck39ajuiw', 'http://localhost:3000/', label = 'Test wallet')
print ("WALLET", wallet)