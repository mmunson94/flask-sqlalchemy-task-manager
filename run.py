import os
from taskmanager import app

if __name__ == "__main__":
    print(os.environ.get("IP"))
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG") == "True"
    )
