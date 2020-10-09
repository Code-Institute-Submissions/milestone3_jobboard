# Imports needed
import os
from app import app
import unittest


# Import my env.py that's ignored by git
if os.path.exists("env.py"):
    import env


class RoutesVisitor(unittest.TestCase):
    # Ensure that route opens index page
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/index', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    # Ensure that route opens vacancies page
    def test_vacancies(self):
        tester = app.test_client(self)
        response = tester.get('/vacancies', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        
# To run the test app
if __name__ == "__main__":
    unittest.main()