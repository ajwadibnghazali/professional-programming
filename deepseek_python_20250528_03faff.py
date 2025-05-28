import pandas as pd
import re
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import time
import random
from urllib.parse import urlparse
from fake_useragent import UserAgent

# Initialize user agent generator
ua = UserAgent()

def extract_contact_info(url):
    """Extract email and phone from a webpage with better pattern matching"""
    try:
        headers = {'User-Agent': ua.random}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Extract emails with better regex pattern
        emails = re.findall(
            r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b", 
            response.text
        )
        
        # Extract phone numbers (Malaysian format)
        phones = re.findall(
            r"\b(?:\+?60|0)[ -]?\d{1,2}[ -]?\d{3,4}[ -]?\d{3,4}\b", 
            response.text
        )
        
        # Clean results
        email = emails[0