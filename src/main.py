"""Server to host backend of app."""

import Path
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    """Hello World."""
    return "Hello, World!"


@app.route("/processbusinessinfo", methods=["POST"])
def process_business_info() -> str:
    """Process business info as inputted by user."""
    # Open process_business_info_input.json
    with Path.open("src/data/process_business_info_input.json", "r") as file:
        process_business_reqs = file.read()
    # Check that all attributes in process_business_info_input.json are present
    # in the request
    for key in process_business_reqs:
        if key not in request.json:
            return f"Missing key: {key}"

    # If persona_requests attribute is present, call generate_persona function
    if "persona_requests" in request.json:
        # CALL FUNCTION
        1

    # Call generate_marketing_mix function
    # CALL FUNCTION
    return 1


if __name__ == "__main__":
    app.run()
