 import requests
import os
from urllib.parse import urlparse
import hashlib

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB limit

def get_file_hash(content):
    return hashlib.sha256(content).hexdigest()

def save_image(content, filename, folder="Fetched_Images"):
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    with open(filepath, 'wb') as f:
        f.write(content)
    return filepath

def fetch_images(urls):
    downloaded_hashes = set()
    
    for url in urls:
        url = url.strip()
        if not url:
            continue
        
        print(f"\nFetching: {url}")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # Check headers
            content_type = response.headers.get("Content-Type", "")
            content_length = int(response.headers.get("Content-Length", 0))

            if not content_type.startswith("image/"):
                print("✗ Skipped: URL does not point to an image")
                continue
            
            if content_length > MAX_FILE_SIZE:
                print(f"✗ Skipped: Image too large ({content_length} bytes)")
                continue

            content_hash = get_file_hash(response.content)
            if content_hash in downloaded_hashes:
                print("✗ Skipped: Duplicate image detected")
                continue
            
            # Determine filename
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                filename = "downloaded_image.jpg"

            filepath = save_image(response.content, filename)
            downloaded_hashes.add(content_hash)
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Saved to: {filepath}")
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")
        except Exception as e:
            print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    urls_input = input("Enter image URLs (comma or newline separated):\n")
    urls = [u.strip() for u in urls_input.replace("\n", ",").split(",") if u.strip()]
    
    fetch_images(urls)
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
