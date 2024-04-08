import requests
from bs4 import BeautifulSoup
import argparse
import wikipedia



'''
Yahoo: https://search.yahoo.com/search?p={}
Google: https://google.com/search?q={}
Bing: https://www.bing.com/search?q={}

'''





def name_search(name: str) -> []:
    query = name.replace(" ","+")
    url = f"https://google.com/search?q={query}"
    response = requests.get(url)
  
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Find all search result links
        search_results = soup.find_all('a')
        # Extract the URLs from the search result links
        result_urls = [link.get('href') for link in search_results if link.get('href').startswith('/url?q=')]
        result_urls = [url.split('/url?q=')[1].split('&sa=')[0] for url in result_urls]
        filter_result_urls = []
        for index , value in enumerate(result_urls):
          if not (value.startswith('https://maps.google') or value.startswith('https://accounts.google') or value.startswith('https://support.google')):
            filter_result_urls.append(value)
        # Save the HTML content to a file for debugging
        with open("search_index.html", "w") as fp:
            fp.write(str(soup))
    
        return filter_result_urls
    else:
        print(f"Failed to fetch search    results. Status code: {response.status_code}")
        return []


headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

  
headers2 = 1

def fetch_image_urls(name:str) -> []:
    query = name.replace(" ","+")
    url = f"https://www.google.com/search?q={query}&tbm=isch"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    with open('img_search.html','w') as fp:
      fp.write(str(soup))
    image_tags = soup.find_all("img", class_="DS1iW")
    image_urls = [tag["src"] for tag in image_tags]
    return image_urls






def search_use_wikipedia(result,lang):
  wikipedia.set_lang(lang)
  res = wikipedia.summary(result)
  return res



def search_use_bing(name):
    query = name.replace(' ','+')
    search_url = f"https://www.bing.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a', href=True)
        urls = [link['href'] for link in results if 'http' in link['href']]
        return urls
    else:
        print("Error:", response.status_code)
        return []





def search_use_yahoo(name):
    query = name.replace(' ', '+')
    search_url = f"https://search.yahoo.com/search?p={query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a', href=True)
        urls = [link['href'] for link in results if 'http' in link['href']]
        return urls
    else:
        print("Error:", response.status_code)
        return []








if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Name search by name (in google search engine)')
  parser.add_argument('-n', help='name to search (optional)',default="no")
  args = parser.parse_args()
  if args.n == "no":
    print(search_use_yahoo(input("[=]Enter the name to search >> ")))
  print(search_use_yahoo(args.n))