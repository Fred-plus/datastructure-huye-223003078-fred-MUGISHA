# Program to manage emergency undo response and processing response
from collections import deque

emergency_type = deque(["police emergence","medical emergence","traffic emergence","fire emergence"])

def undoEmergence():
    if emergency_type:
        emergency_type.pop()
    else:
        print("No Response Found")

def processingEmergence():
    if emergency_type:
        emergency_type.popleft()
    else:
        print("No Processing Found")

undoEmergence()
processingEmergence()

print(emergency_type)
