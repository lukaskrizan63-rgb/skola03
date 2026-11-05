import sys
import requests


def download_url_and_get_all_hrefs(url):
    hrefs = []

    response = requests.get(url)

    if response.status_code == 200:
        content = response.content.decode('utf-8', errors='ignore')

        start = 0
        while True:
            start = content.find('<a ', start)

            if start == -1:
                break

            end = content.find('>', start)

            if end == -1:
                break

            tag = content[start:end]

            href_start = tag.find('href=')

            if href_start != -1:
                quote = tag[href_start + 5]

                if quote == '"' or quote == "'":
                    href_start += 6
                    href_end = tag.find(quote, href_start)

                    if href_end != -1:
                        hrefs.append(tag[href_start:href_end])

            start = end + 1

    else:
        raise Exception(f"Chyba pri stahovani stranky: {response.status_code}")

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        download_url_and_get_all_hrefs(url)

    except Exception as e:
        print(f"Program skoncil chybou: {e}")
