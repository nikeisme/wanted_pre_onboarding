# from django.test import TestCase,Client,TransactionTestCase
# from bs4 import BeautifulSoup
# from .models import Notification,Company


# unit Test 구현 시도했지만 실패
# class setUp(TransactionTestCase):

#     def setUp(self):
#         self.client=Client()

#     def tearDown(self) :
#         Notification.objects.all().delete()




#     def test_post_list (self) : 

#     # 채용 공고 목록 페이지를 가져온다.
#      response = self.client.get('/recruit/')

#     # 정상적으로 페이지가 로드된다. 
#      self.assertEqual(response.status_code,200)
     
#      soup = BeautifulSoup(response.content,'html.parser')

#     # 채용공고가 하나도 없다면
#      self.assertEqual(Notification.objects.count(),0)
#      main_area = soup.find('table',attrs={"class": "table"}) 
#      self.assertIn('채용 공고가 없습니다.', main_area.text)
#      company = Company.objects.get(co_id='카카오')
#      post_001 = Notification.objects.create(
#                                                 no_id = 'kakao notification 3',
#                                                 country = '한국',
#                                                 region = ' 강원도',
#                                                 position = '백엔드 주니어 개발자',
#                                                 reward = 1000000,
#                                                 content='카카오에서 백엔드 주니어 개발자를 채용합니다. 채용 요건은...',
#                                                 technique='JAVA',
#                                                 company_id = company
                                                
#                                             )
#      post_002 = Notification.objects.create(
#                                                 no_id = 'kakao notification 5',
#                                                 country = '호주 ',
#                                                 region = '시드니',
#                                                 position = '백엔드 주니어 개발자',
#                                                 reward = 1000000,
#                                                 content='카카오에서 백엔드 주니어 개발자를 채용합니다. 채용 요건은...',
#                                                 technique='JAVA',
#                                                 company_id = company
#                                             )

#      self.assertEqual(Notification.objects.count(),2)


#     # 페이지 새로 고침
#      response = self.client.get('/recruit/')
#      self.assertEqual(response.status_code, 200)
#      soup = BeautifulSoup(response.content, 'html.parser')

    # # main area에 공고 2개가 존재
    #  main_area = soup.find('tbody', id = 'main-area')
    #  self.self.assertIn( post_001.no_id, )
    #  self.self.assertIn( post_002.no_id, main_area.text)

    #  # '아직 채용공고가 없습니다'라는 문구가 안나타나도 됨
    #  self.self.assertNotIn('채용 공고가 없습니다', main_area.text)