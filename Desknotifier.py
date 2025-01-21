from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Take Rest",
            message="Rest is essential to recharge your mind and body, improving focus, health, and productivity.",
            timeout=5
        )
        time.sleep(10)  
