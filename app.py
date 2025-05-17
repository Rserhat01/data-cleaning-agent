from flask import Flask, render_template, request, send_file
import pandas as pd
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # .env dosyasını yükler
app = Flask(__name__)

# API anahtarını ortam değişkeninden al (Örnek: export OPENAI_API_KEY="anahtarınız")
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_cleaning_suggestions(columns, sample_row):
    prompt = f"""
    Veri setinde aşağıdaki sütunlar ve örnek satır var:
    Sütunlar: {columns}
    Örnek veri: {sample_row}

    Eksik veriler, aykırı değerler ve olası veri temizleme önerilerini kısa ve öz liste olarak belirt.
    """
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.5
    )
    return response.choices[0].message.content.strip()

@app.route("/download")
def download_file():
    path = "output.csv"  # İşlenmiş dosya yolu
    return send_file(path, as_attachment=True)

@app.route("/", methods=["GET", "POST"])
def index():
    suggestion = None
    cleaned = None
    columns = []
    sample_row = []
    download_available = False

    if request.method == "POST":
        file = request.files.get("csv_file")
        action = request.form.get("action")
        if file:
            df = pd.read_csv(file)
            columns = df.columns.tolist()
            sample_row = df.iloc[0].tolist()

            if action == "suggest":
                suggestion = get_cleaning_suggestions(columns, sample_row)

            elif action == "clean":
                # Basit temizleme örneği: eksik sayıları ortalama ile doldur
                for col in df.select_dtypes(include=['float64', 'int64']).columns:
                    df[col].fillna(df[col].mean(), inplace=True)
                # İşlenmiş dataframe'i kaydet
                df.to_csv("output.csv", index=False)
                cleaned = df.head().to_html(classes="table table-striped")
                suggestion = "Temizleme yapıldı. Eksik sayılar ortalama ile dolduruldu."
                download_available = True

    return render_template("index.html", suggestion=suggestion, cleaned=cleaned, columns=columns, sample_row=sample_row, download_available=download_available)

if __name__ == "__main__":
    app.run(debug=True)
