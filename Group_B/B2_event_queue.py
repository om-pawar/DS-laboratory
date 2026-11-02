# Experiment B2: Real-Time Event Processing System
# Group B: Stacks, Queues, and Linked List

from collections import deque

class EventProcessor:
    def __init__(self):
        self.queue = deque()

    def add_event(self, event_name):
        """Adds a new event to the rear of the queue."""
        self.queue.append(event_name)
        print(f"[+] Event Queued    : {event_name}")

    def process_next_event(self):
        """Processes and removes the oldest event from the front of the queue."""
        if self.queue:
            event = self.queue.popleft()
            print(f"[✓] Event Processed : {event}")
        else:
            print("[!] No pending events in the queue.")


if __name__ == "__main__":
    print("--- Real-Time Event Processing System ---")
    processor = EventProcessor()
    processor.add_event("User_Login")
    processor.add_event("File_Upload")
    processor.add_event("Payment_Checkout")

    processor.process_next_event()
    processor.process_next_event()
    processor.process_next_event()
    processor.process_next_event()
