from flask import Flask

app = Flask(__name__)

print("Goodbye world")
print(app.config)

if __name__ == "__name__":
    app.run()