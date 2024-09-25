import requests
from bs4 import BeautifulSoup


def get_image_sources(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all <img> tags
        img_tags = soup.find_all("img")

        # Extract the 'src' attribute from each <img> tag
        img_sources = [img["src"] for img in img_tags if "src" in img.attrs]

        return img_sources
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []


if __name__ == "__main__":
    # Specify the URL you want to crawl
    url = input("Enter the URL of the webpage: ")

    # Get the image sources
    image_sources = get_image_sources(url)

    # Print the image sources
    if image_sources:
        print("\nImage Sources Found:")
        for img_src in image_sources:
            print(img_src)
    else:
        print("No image sources found.")
