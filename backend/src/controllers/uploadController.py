
from flask import render_template, redirect, url_for, request, abort
from models.Usuario import Usuario
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

@app.route("/upload", methods=["GET", "POST"])
def upload_file():

    if request.method == "POST":
        if not "file" in request.files:
            return "No file part in the form."
        f = request.files["file"]
        if f.filename == "":
            return "No file selected."
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            # return redirect(url_for("get_file", filename=filename))
            rest = {
                'path': UPLOAD_FOLDER+"/"+filename
            }
            return jsonify(rest)
            # return UPLOAD_FOLDER+"/"+filename
        return "File not allowed."

    return """
    <!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Upload File</title>
</head>
<body>
    <h1>Upload File</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
</body>
</html>"""

@app.route("/uploads/<filename>")
def get_file(filename):
    print(UPLOAD_FOLDER)
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route("/upload_reconocedor", methods=["GET", "POST"])
def upload_file2():
    if request.method == "POST":
        if not "file" in request.files:
            return "No file part in the form."
        f = request.files["file"]
        if f.filename == "":
            return "No file selected."
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        if reconocedor.reconocer(str(UPLOAD_FOLDER+"/"+filename)) is None:
            return "False"
        else:
            return "True"
        return "File not allowed."

    return ""