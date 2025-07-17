from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    message = "KİMSEBASGOZ HİRAYA AŞIK ❤️❤️❤️❤️❤️❤️❤️"
    
    kimsebasgoz_ig = "@_HAYALET.BAS.KRC.KIMSEBASGOZ_"
    hira_ig = "@1.SMYFY7"
    
    kimsebasgoz_link = "https://instagram.com/_hayalet.bas.krc.kimsebasgoz_"
    hira_link = "https://instagram.com/1.smyfy7"
    
    video_url = "https://cdn.pixabay.com/vimeo/432585628/Golden_Sunset_9603.mp4?width=1280&hash=f2e5d92f0b9d5a42fa8b9d4b1b3e2f2f4d25f35e"
    music_url = "https://cdn.pixabay.com/download/audio/2022/03/20/audio_4997b5518c.mp3?filename=romantic-piano-11244.mp3"

    return f"""
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
        <video autoplay muted loop playsinline>
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

if __name__ == "__main__":
    app.run()
