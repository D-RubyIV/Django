import base64

input_string = "iVBORw0KGgoAAAANSUhEUgAAAL8AAAD8CAYAAAAmJnXEAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAANaSURBVHhe7dpBattQGEZRq0vJMCvI"
decoded_bytes = base64.b64decode(input_string)
decoded_string = decoded_bytes.decode('utf-8')

print(decoded_string)
