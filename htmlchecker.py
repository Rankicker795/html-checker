"""Class to test if using a lambda can check HTML
status codes
"""
import requests


class TestResponse:
    # Set of acceptable HTML status codes
    good_html_codes = {200, 204}
    # Lambda function to check HTML status code
    htmlcheck = lambda response: False if (response.status_code 
        not in TestResponse.good_html_codes) else True

    def __init__(self):
        self.sites = ["https://theverge.com", 
            "https://css-tricks.com/thispagedoesntexist"]
    
    
    def check_sites(self):
        """Used to see if the url has a good HTML code or not"""
        for url in self.sites:
            print(f"{url} Connection Status:" 
                    f"{TestResponse.htmlcheck(requests.get(url))}")


if __name__ == "__main__":
    TestResponse().check_sites()
