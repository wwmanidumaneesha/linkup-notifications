import firebase_admin
from firebase_admin import credentials, messaging

# Path to your service account key
cred = credentials.Certificate("linkup-tech-68c20b7dd522.json")
firebase_admin.initialize_app(cred)

# Define the notification
notification = messaging.Message(
    notification=messaging.Notification(
        title="🔥 Test Notification",
        body="This is a test push from your local machine!",
    ),
    topic="allUsers"  # ✅ Make sure users in your Flutter app subscribed to this topic
)

# Send the message
response = messaging.send(notification)
print("✅ Message sent:", response)
