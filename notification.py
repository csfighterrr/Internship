from pywebpush import webpush, WebPushException
from typing import Dict
import json

class WebPushNotification:
    def __init__(self, vapid_private_key: str, vapid_claims: Dict):
        """
        Initialize Web Push notification service
        vapid_claims should contain 'sub' key with mailto: or https: URL
        """
        self.vapid_private_key = vapid_private_key
        self.vapid_claims = vapid_claims

    def send_notification(
        self,
        subscription_info: Dict,
        message: str,
        title: str = None
    ) -> bool:
        """
        Send web push notification to a subscriber
        subscription_info: Dict containing endpoint, keys (p256dh, auth)
        """
        try:
            data = {
                "message": message,
                "title": title or "Notification"
            }
            
            webpush(
                subscription_info=subscription_info,
                data=json.dumps(data),
                vapid_private_key=self.vapid_private_key,
                vapid_claims=self.vapid_claims
            )
            return True
        except WebPushException as e:
            print(f"Web Push failed: {e}")
            return False

    @staticmethod
    def generate_subscription_info(endpoint: str, p256dh: str, auth: str) -> Dict:
        """Generate subscription info dictionary from components"""
        return {
            "endpoint": endpoint,
            "keys": {
                "p256dh": p256dh,
                "auth": auth
            }
        }





