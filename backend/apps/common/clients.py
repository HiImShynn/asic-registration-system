from typing import Dict, Any, Optional, Union
from datetime import datetime, timedelta
import uuid
import logging
from headers import (
    QueryNameAvailabilityHeaders,
    SearchNniNameHeaders,
    GetNniHeaders,
    QueryAddressHeaders,
    BnLodgeApplicationHeaders
)
from decouple import config
from zeep import Client, Transport, Settings
from zeep.transports import Transport
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from requests.auth import HTTPBasicAuth
from requests import Session
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ASICAuthenticationError(Exception):
    """Custom exception for ASIC authentication issues"""
    pass


class ASICAPIError(Exception):
    """Custom exception for ASIC API errors"""
    pass

class ASICSOAPClient:
    """
    Complete authenticated ASIC SOAP client that:
    1. Handles authentication sessions using .env credentials
    2. Uses header classes for proper message structure  
    3. Provides methods for all ASIC operations
    4. Includes proper error handling and retry logic
    """
    def __init__(self, environment: str = 'test'):
        """
        Initialize the authenticated ASIC client
        
        Args:
            environment: "test" or "production" (currently using test credentials)
        """
        self.environment = environment
        self.username = str(config("ASIC_USERNAME", default="", cast=str))
        self.password = str(config("ASIC_PASSWORD", default="", cast=str))
        self.sender_id = str(config("ASIC_SENDER_ID", default="000040540", cast=str))
        self.sender_type = str(config("ASIC_SENDER_TYPE", default="REGA", cast=str))
        # Validate credentials are loaded
        if not all([self.username, self.password, self.sender_id, self.sender_type]):
            raise ASICAuthenticationError("Missing ASIC credentials in .env file")
            
        logger.info(f"Initializing ASIC client for user: {self.username}")
        logger.info(f"Using sender ID: {self.sender_id}")
        self.wsdl_urls = self._get_wsdl_urls()
        self.session = self._create_session()

    def _get_wsdl_urls(self) -> Dict[str, str]:
        """Get WSDL URLs from environment variables"""
        urls =  {
            "queryAddress": str(config("ASIC_QUERY_ADDRESS_WSDL", default="", cast=str)),
            "queryNameAvailability": str(config("ASIC_QUERY_NAME_AVAILABILITY_WSDL", default="", cast=str)),
            "getNni": str(config("ASIC_GET_NNI_WSDL", default="", cast=str)),
            "searchNni": str(config("ASIC_SEARCH_NNI_WSDL", default="", cast=str)),
            "bnLodgeApplication": str(config("ASIC_BN_LODGE_WSDL", default="", cast=str))
        }
        # Validate all URLs are present
        missing_urls = [key for key, url in urls.items() if not url]
        if missing_urls:
            raise ASICAuthenticationError(f"Missing WSDL URLs in .env: {missing_urls}")
                
        return urls

    def _create_session(self) -> requests.Session:
        """
        Create an authenticated requests session with ASIC credentials
        """
        session = Session()
        
        # Set up HTTP Basic Authentication
        session.auth = HTTPBasicAuth(self.username, self.password)
        
        # Configure retry strategy for network resilience
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST"]  # Updated parameter name
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        # Set headers for ASIC API
        session.headers.update({
            "Content-Type": "text/xml; charset=utf-8",
            "User-Agent": "ASIC-Python-Client/1.0",
            "Accept": "text/xml, application/soap+xml"
        })
        
        # Note: Timeout should be set per request, not on the session object.
        # Example usage: session.get(url, timeout=60)
        
        logger.info("Created authenticated session with ASIC credentials")
        return session

    def _create_soap_client(self, wsdl_url: str) -> Client:
        """
        Create a Zeep SOAP client for the given WSDL URL
        """
        try:
            # Create Zeep transport with the authenticated session
            transport = Transport(session=self.session, timeout=180)

            # Configure Zeep settings
            settings = Settings(
                strict=False,  # Be lenient with ASIC's WSDL variations
                xml_huge_tree=True,  # Handle large responses
                forbid_dtd=False,  # Allow DTD processing
                forbid_entities=False  # Allow entity processing
            )

            # Create the SOAP client
            client = Client(wsdl=wsdl_url, transport=transport, settings=settings)
            logger.info(f"Created SOAP client for WSDL: {wsdl_url}")
            return client
        except Exception as e:
            logger.error(f"Failed to create SOAP client for WSDL {wsdl_url}: {e}")
            raise ASICAPIError(f"Failed to create SOAP client: {e}")

