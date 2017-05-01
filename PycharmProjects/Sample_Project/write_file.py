f = open('output.txt', 'w')

for name, url in urls.iteritems():
    web = urllib.urlopen(url)
    # FloorPlanData houses the JSON information we want
    pattern = re.compile('var FloorPlanData = (.*?);')

    soup = BeautifulSoup(web.read(), "lxml")
    scripts = soup.find_all('script')
    json_data = None
    for script in scripts: # cycle through the script tags in the page source
       if(pattern.match(str(script.string))):
           data = pattern.match(script.string)
           json_data = json.loads(data.groups()[0])

    fields = ['PlanName', 'MinimumRent', 'MaximumRent', 'SquareFeet']

    name_string = "\n" + name
    print name_string # print apartment complex name (e.g. "RiverView")
    f.write(name_string + "\n")

    for plan in json_data:
        if approve_plan(plan):
            print ""
            f.write("\n")
            for field in fields:
                field_string = field + ': ' + str(plan[field])
                print field_string
                f.write(field_string + "\n")