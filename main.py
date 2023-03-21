import os
import openai
from flask import Flask, render_template, request

app = Flask(__name__)

openai.api_key = "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"


def generate_caption(image_url):
  prompt = f"Generate a caption for the following image: {image_url}"
  response = openai.Completion.create(engine="text-davinci-002",
                                      prompt=prompt,
                                      max_tokens=20,
                                      n=1,
                                      stop=None,
                                      temperature=0.5)
  return response.choices[0].text.strip()


@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    image_url = request.form["image_url"]
    caption = generate_caption(image_url)
    return render_template("results.html",
                           image_url=image_url,
                           caption=caption)
  return render_template("index.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
