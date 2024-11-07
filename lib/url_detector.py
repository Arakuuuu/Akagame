import re
import urllib.parse
from collections import Counter

class PhishingDetector:
    def __init__(self):
        self.suspicious_patterns = [
            r'paypal.*\.com',
            r'bank.*\.com',
            r'secure.*\.com',
            r'account.*\.com',
        ]
        
    def analyze_url(self, url):
        """Analyze URL for potential phishing indicators."""
        risk_score = 0
        parsed = urllib.parse.urlparse(url)
        
        # Check domain length
        if len(parsed.netloc) > 30:
            risk_score += 2
            
        # Check for suspicious patterns
        for pattern in self.suspicious_patterns:
            if re.search(pattern, url.lower()):
                risk_score += 1
                
        # Check for special characters
        special_chars = Counter(['@', '-', '_', '%', '='])
        for char, count in special_chars.items():
            if url.count(char) > 2:
                risk_score += 1
                
        # Check for HTTP vs HTTPS
        if parsed.scheme != 'https':
            risk_score += 2
            
        return min(risk_score, 10)  # Cap score at 10