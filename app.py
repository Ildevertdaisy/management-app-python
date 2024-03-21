

from flask import Flask, render_template, request, jsonify
import os


app = Flask(__name__)

# Définir le dossier où les fichiers téléchargés seront stockés
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Assurez-vous que le dossier existe
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/partager", methods=["GET"])
def upload():
    return render_template("upload.html")


@app.route("/upload/files", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return "Aucun fichier part"
    
    file = request.files["file"]
    if file.filename == '':
        return 'Aucun fichier sélectionné'
    
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'Fichier téléchargé avec succès'


@app.route("/files", methods=["GET"])
def list_files():
    files = os.listdir(app.config["UPLOAD_FOLDER"])
    data = {
        "files": files
    }
    return jsonify(data)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)