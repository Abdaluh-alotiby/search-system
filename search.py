from flask import Flask, render_template, request
import importlib.util
import requests
from bs4 import BeautifulSoup
import namesearch as module





app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method.lower() == 'get':
        return render_template('index.html')
    elif request.method.lower() == 'post':
        name = request.form.get('name')
        ob = request.form.get('options-base')
        # Assuming you have a form field with name="name"
        if name:
            # Call name_search function with the provided name
            if ob == 'wikipedia':
              lang = request.form.get('language')
              results = module.search_use_wikipedia(name,lang)
              return render_template('index.html',summary=True,Rmode=False,res=results)
            if ob == 'bing':
              search_results = module.search_use_bing(name)
              twitterA = []
              instagramA = []
              facebookA =[]
              youtubeA = []
              tiktokA = []
              otherA = []
              for v in search_results:
                if 'twitter.com' in v:
                  twitterA.append(v)
                  continue
                if 'facebook.com' in v:
                  facebookA.append(v)
                  continue
                if 'instagram.com' in v:
                  instagramA.append(v)
                  continue
                if 'youtube' in v or 'youtu.be' in v:
                  youtubeA.append(v)
                  continue
                if 'tiktok'in v:
                  tiktokA.append(v)
                  continue
                otherA.append(v)
              return render_template('index.html', twitter=twitterA,
                instagram=instagramA,
                youtube=youtubeA,
                facebook=facebookA,
                tiktok=tiktokA,
                other=otherA,
                Rmode=True,
                image_urls=image_urls)
            elif ob == 'google':
              search_results = module.name_search(name)
              image_urls =module.fetch_image_urls(name)
              twitterA = []
              instagramA = []
              facebookA =[]
              youtubeA = []
              tiktokA = []
              otherA = []
              for v in search_results:
                if 'twitter.com' in v:
                  twitterA.append(v)
                  continue
                if 'facebook.com' in v:
                  facebookA.append(v)
                  continue
                if 'instagram.com' in v:
                  instagramA.append(v)
                  continue
                if 'youtube' in v or 'youtu.be' in v:
                  youtubeA.append(v)
                  continue
                if 'tiktok'in v:
                  tiktokA.append(v)
                  continue
                otherA.append(v)
              return render_template('index.html', twitter=twitterA,
                instagram=instagramA,
                youtube=youtubeA,
                facebook=facebookA,
                tiktok=tiktokA,
                other=otherA,
                Rmode=True,
                image_urls=image_urls)
            else:
              return render_template('index.html',error='The type is not organise  🤨')
        else:
            return render_template('index.html',error="No name provided in the form")

if __name__ == '__main__':
    app.run(debug=True)
