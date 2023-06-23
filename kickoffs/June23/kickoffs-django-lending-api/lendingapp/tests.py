from django.test import TestCase
    
class AppTest(TestCase):
    
    def test_1_get_borrower_0_success(self):
        res=self.client.get('/lends/borrower/')
        print(res.json()) 
        assert b'[]' in res.content
        assert 200==res.status_code

    def test_1_post_borrower_0_success(self):
        payload=[{'name':'john','email':'john@gmail.com'},{'name':'doe','email':'doe@gmail.com'}]
        for i in payload:
            res=self.client.post('/lends/borrower/',data=i)   
            print(res.json()) 
            assert res.json()['name']==i['name']
            assert res.json()['email']==i['email']
            assert 201==res.status_code

    def test_1_post_borrower_1_success(self):
        
        
        res=self.client.post('/lends/borrower/',data={'name':'john','email':'john@gmail.com'}) 
        res1=self.client.post('/lends/borrower/',data={'name':'doe','email':'john@gmail.com'})  
        print(res1.json()) 
        assert b'borrower with this email already exists' in res1.content
        assert 400==res1.status_code

    def test_1_get_borrower_1_success(self):
        res=self.client.post('/lends/borrower/',data={'name':'john','email':'john@gmail.com'})
        res1=self.client.get('/lends/borrower/')
        print(res1.json()) 
        assert 'john'==res1.json()[0]['name']
        assert 200==res1.status_code
            
    def test_1_update_borrower_1_success(self):
        res=self.client.post('/lends/borrower/',data={'name':'john','email':'john@gmail.com'})
        res1=self.client.put('/lends/borrower/1/',content_type='application/json',data={'name':'john','email':'123@gmail.com'})
        assert '123@gmail.com' ==res1.json()['email']
        assert 200==res1.status_code

    def test_1_delete_borrower_1_success(self):
        res=self.client.post('/lends/borrower/',data={'name':'john','email':'john@gmail.com'})
        res=self.client.delete('/lends/borrower/1/',content_type='application/json')
        assert 204==res.status_code

    def test_1_get_loan_0_success(self):
        res=self.client.get('/lends/loan/')
        print(res.json()) 
        assert b'[]' in res.content
        assert 200==res.status_code

    def test_1_post_loan_0_success(self):
        res=self.client.post('/lends/borrower/',data={'name':'john','email':'john@gmail.com'})        
        res1=self.client.post('/lends/loan/',data={'amount':2000.0,'interest_rate':2.0,'borrower_id':1})   
        print(res1.json()) 
        assert 2000.0==res1.json()['amount']
        assert 201==res1.status_code

    def test_1_get_loan_1_success(self):
        res=self.client.post('/lends/borrower/',data={'name':'john','email':'john@gmail.com'})
        res1=self.client.post('/lends/loan/',data={'amount':2000.0,'interest_rate':2.0,'borrower_id':1})
        res2=self.client.get('/lends/loan/')
        print(res2.json()) 
        assert 2.0==res2.json()[0]['interest_rate']
        assert 200==res2.status_code

    def test_1_update_loan_1_success(self):
        res=self.client.post('/lends/borrower/',data={'name':'john','email':'john@gmail.com'})
        res1=self.client.post('/lends/loan/',data={'amount':2000.0,'interest_rate':2.0,'borrower_id':1})
        res2=self.client.put('/lends/loan/1/',content_type='application/json',data={'amount':35000.0,'interest_rate':2.0,'borrower_id':1})
        print(res2.json()) 
        assert 35000.0==res2.json()['amount']
        assert 200==res2.status_code

    def test_1_delete_loan_1_success(self):
        res=self.client.post('/lends/borrower/',data={'name':'john','email':'john@gmail.com'})
        res1=self.client.post('/lends/loan/',data={'amount':2000.0,'interest_rate':2.0,'borrower_id':1})
        res2=self.client.delete('/lends/loan/1/',content_type='application/json')
        assert 204==res2.status_code

    def test_1_get_payment_0_success(self):
        res=self.client.get('/lends/payment/')
        print(res.json()) 
        assert b'[]' in res.content
        assert 200==res.status_code
    
    def test_1_get_payment_0_success(self):
        res=self.client.get('/lends/payment/1')
        print(res.status_code) 
        assert 301==res.status_code

    def test_1_post_payment_0_success(self):
        res=self.client.post('/lends/borrower/',data={'name':'john','email':'john@gmail.com'})        
        res1=self.client.post('/lends/loan/',data={'amount':2000.0,'interest_rate':2.0,'borrower_id':1})  
        res2=self.client.post('/lends/payment/',data={'amount':1500.0,'loan_id':1})  
        print(res2.json()) 
        assert 1500.0==res2.json()['amount']
        assert b'date' in res2.content
        assert 201==res2.status_code

    def test_1_update_payment_1_success(self):
        res=self.client.post('/lends/borrower/',data={'name':'john','email':'john@gmail.com'})        
        res1=self.client.post('/lends/loan/',data={'amount':2000.0,'interest_rate':2.0,'borrower_id':1})
        res2=self.client.post('/lends/payment/',data={'amount':1500.0,'loan_id':1})  
        res3=self.client.put('/lends/payment/1/',content_type='application/json',data={'amount':1000.0,'loan_id':1})
        print(res3.json()) 
        assert 1000.0==res3.json()['amount']
        assert b'loan_id' in res2.content
        assert 200==res3.status_code

    def test_1_delete_payment_1_success(self):
        res=self.client.post('/lends/borrower/',data={'name':'john','email':'john@gmail.com'})        
        res1=self.client.post('/lends/loan/',data={'amount':2000.0,'interest_rate':2.0,'borrower_id':1})
        res2=self.client.post('/lends/payment/',data={'amount':1500.0,'loan_id':1})  
        res3=self.client.delete('/lends/payment/1/',content_type='application/json')
        assert 204==res3.status_code
    