from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <body>
            <h2>ASTRA UI</h2>
            <textarea id="codeInput"></textarea><br><br>
            <button id="analyzeBtn" onclick="analyze()">Analyze</button>
            <pre id="output"></pre>

            <script>
                function analyze() {
                    fetch("/analyze", {
                        method: "POST",
                        headers: {"Content-Type": "application/json"},
                        body: JSON.stringify({
                            code: document.getElementById("codeInput").value
                        })
                    })
                    .then(res => res.json())
                    .then(data => {
                        document.getElementById("output").innerText = data.result;
                    });
                }
            </script>
        </body>
    </html>
    """

@app.route("/analyze", methods=["POST"])
def analyze():
    code = request.json.get("code", "")
    if "prin(" in code:
        return jsonify(result="print(x)")
    return jsonify(result="No error")

if __name__ == "__main__":
    app.run(port=8501)
