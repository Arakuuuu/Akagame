import unittest
from lib.url_detector import PhishingDetector

class TestPhishingDetector(unittest.TestCase):
    def setUp(self):
        self.detector = PhishingDetector()
        
    def test_legitimate_url(self):
        url = "https://www.example.com"
        score = self.detector.analyze_url(url)
        self.assertLess(score, 5)
        
    def test_suspicious_url(self):
        url = "http://paypal-secure.suspicious-site.com@evil.com"
        score = self.detector.analyze_url(url)
        self.assertGreater(score, 7)
        
    def test_http_penalty(self):
        url = "http://example.com"
        score = self.detector.analyze_url(url)
        self.assertGreater(score, 0)