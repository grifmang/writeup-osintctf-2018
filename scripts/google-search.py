def find_socials(query):
    try:
        from googlesearch import search
    except ImportError:
        print('googlesearch module not found')

    sites = ['twitter', 'linkedin', 'facebook', 'instagram', 'pinterest', 'myspace', 'tumblr']
    social_results = []

    for result in search(query, tld="com", stop=50, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36", pause=2.0):
        domain = result[8:20]
        for site in sites:
            if site in domain:
                social_results.append(result)

    for site in social_results:
        print(site)

    return social_results


if __name__ == '__main__':
    query = input('Enter search query: ') 
    find_socials(query)