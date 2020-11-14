
response = self.app.get('/login', base_url='https://localhost')
assert(response.status_code == 200)


self.Card1 = Card.objects.create( data = "test", prod = 1, fp = "test", amount = 1000, user="test")
