import os
import requests


def getLinkedInProfileFromProxyCurl(linkedin_profile_url: str):
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    api_key = os.getenv("PROXY_CURL_API_KEY")
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
        'url': linkedin_profile_url,
        'fallback_to_cache': 'on-error',
        'use_cache': 'if-present',
        'skills': 'include',
        'inferred_salary': 'include',
        'personal_email': 'include',
        'personal_contact_number': 'include',
        'twitter_profile_id': 'include',
        'facebook_profile_id': 'include',
        'github_profile_id': 'include',
        'extra': 'include',
    }
    response = requests.get(api_endpoint,
                            params=params,
                            headers=header_dic)

    return response.json()


def getLinkedInProfileFromMockup():
    api_endpoint = "https://gist.githubusercontent.com/jm-avila/b5bb1444fd1169515647ae1523110276/raw/0c21fdbfe475b4bc77062d51bbc0dd6cb4bbeadb/proxycurl_linkedin_mockup.json"
    response = requests.get(api_endpoint)
    return response.json()


def scrape_linkedin_profile(raw_data: dict):
    data = {
        key: value
        for key, value in raw_data.items()
        if value not in ([], "", "None", None) and key not in ["people_also_viewed", "certifications", "background_cover_image_url", "profile_pic_url", "similarly_named_profiles", "connections", "follower_count"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    if data.get("experiences"):
        for group_dict in data.get("experiences"):
            group_dict.pop("logo_url")
            group_dict.pop("company_linkedin_profile_url")

    if data.get("education"):
        for group_dict in data.get("education"):
            group_dict.pop("logo_url")
            group_dict.pop("school_linkedin_profile_url")

    if data.get("accomplishment_projects"):
        for group_dict in data.get("accomplishment_projects"):
            group_dict.pop("url")

    if data.get("volunteer_work"):
        for group_dict in data.get("volunteer_work"):
            group_dict.pop("logo_url")
            group_dict.pop("company_linkedin_profile_url")

    return data


def getLinkedInProfile(linkedin_profile_url: str):
    use_proxy_curl_mock_up = os.getenv("USE_PROXY_CURL_MOCK_UP")
    data = {}
    if use_proxy_curl_mock_up == "true":
        data = getLinkedInProfileFromMockup()
    else:
        data = getLinkedInProfileFromProxyCurl(
            linkedin_profile_url=linkedin_profile_url)
    return scrape_linkedin_profile(data)
