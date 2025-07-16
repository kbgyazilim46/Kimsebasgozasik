from flask import Flask
import textwrap

app = Flask(__name__)

@app.route("/")
def home():
    message = "KİMSEBASGOZ HİRAYA AŞIK ❤️❤️❤️❤️❤️❤️❤️"
    
    kimsebasgoz_ig = "@_HAYALET.BAS.KRC.KIMSEBASGOZ_"
    hira_ig = "@1.SMYFY7"
    
    kimsebasgoz_link = "https://instagram.com/_hayalet.bas.krc.kimsebasgoz_"
    hira_link = "https://instagram.com/1.smyfy7"
    
    video_url = "https://raw.githubusercontent.com/kbgyazilim46/Kimsebasgozasik/main/sitevideosu.mp4"
    music_url = "https://raw.githubusercontent.com/kbgyazilim46/Kimsebasgozasik/main/sitemuzigi.mp3"

    html_content = f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>KİMSEBASGOZ ❤️ HİRA</title>
        <style>
            html, body {{
                margin: 0;
                padding: 0;
                height: 100%;
                overflow: hidden;
                font-family: Arial, sans-serif;
                background: black;
            }}
            video {{
                position: fixed;
                top: 0;
                left: 0;
                min-width: 100%;
                min-height: 100%;
                object-fit: cover;
                z-index: -1;
            }}
            .content {{
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                color: white;
                text-align: center;
                text-shadow: 2px 2px 8px #000;
            }}
            h1 {{
                font-size: 3em;
            }}
            p {{
                font-size: 1.5em;
            }}
            .ig {{
                color: #ff80ab;
                text-decoration: none;
            }}
            .ig:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <video autoplay muted loop>
            <source src="{video_url}" type="video/mp4">
            Tarayıcınız video formatını desteklemiyor.
        </video>

        <audio autoplay loop>
            <source src="{music_url}" type="audio/mpeg">
            Tarayıcınız ses formatını desteklemiyor.
        </audio>

        <div class="content">
            <h1>{message}</h1>
            <p><strong>KİMSEBASGOZ IG:</strong>
                <a class="ig" href="{kimsebasgoz_link}" target="_blank">{kimsebasgoz_ig}</a></p>
            <p><strong>HİRA IG:</strong>
                <a class="ig" href="{hira_link}" target="_blank">{hira_ig}</a></p>
        </div>
    </body>
    </html>
    """

    return textwrap.dedent(html_content)

if __name__ == "__main__":
    app.run()
