# base page: http://www.cardiped.net/browseDogs.php?start=0&p_f=0&sortBy=name&alpha=a
# for web scraping
import requests, bs4
import httplib2

# were are we saving data?
saveFilejson = '/Users/jillnaiman1/spring2019online/week11/corg/corgiData_countries.json'

#-----------------------------------------------------------


# webparsing numbers
startSmall=0
startLarge=0

names = []
sires = []
dams = []
sexes = []
years = []
siblings = []
countries = []

# find number of doggos listed
w = 'http://www.cardiped.net/browseDogs.php?start='+\
    str(int(startSmall))+\
    '&p_f='+\
    str(int(startLarge))+\
    '&sortBy=name&alpha=a'
# parse
page = requests.get(w)
soup = bs4.BeautifulSoup(page.text, 'html.parser')
soup = str(soup)

# figuring out from webpage how many doggos
x = soup.split('Displaying')[1]
x = x.split('</b>')[0]
x = x.split('of ')[1]
numberOfDoggos = int(x)

while startSmall < numberOfDoggos:
    w = 'http://www.cardiped.net/browseDogs.php?start='+\
        str(int(startSmall))+\
        '&p_f='+\
        str(int(startLarge))+\
        '&sortBy=name&alpha=a'
    print(w)
    
    # parse
    page = requests.get(w)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    soup = str(soup)

    # split by details
    splitSoup = soup.split('<a href="details.php?id=')
    # ignore top
    splitSoup = splitSoup[1:]
    # take out last bit from last one
    x = splitSoup[-1]
    y = x.split('</table>')
    splitSoup[-1] = y[0]

    
    # loop and append
    for s in splitSoup:
        #print(s)
        #print('---')

        # navigate to details page
        myid = s.split('">')[0]
        w_details = 'http://www.cardiped.net/details.php?id=' + str(myid)
        page_details = requests.get(w_details)
        soup_details = bs4.BeautifulSoup(page_details.text, 'html.parser')
        soup_details = str(soup_details)
        # name
        name = ((soup_details.split('Registered Name:')[1]).split('<td>')[1]).split('</td>')[0]
        # Dad
        sire = ((soup_details.split('Sire:')[1]).split('<td>')[1]).split('</td>')[0]
        #   listed?
        if len(sire) > 0:
            sire = (sire.split('>')[1]).split('<')[0]
        else:
            sire = ''
        # Mom
        dam = ((soup_details.split('Dam:')[1]).split('<td>')[1]).split('</td>')[0]
        if len(dam) > 0:
            dam = (dam.split('>')[1]).split('<')[0]
        else:
            dam = ''
        # Sex
        sex = ((soup_details.split('Sex:')[1]).split('<td>')[1]).split('</td>')[0]
        # Birthday
        dob = ((soup_details.split('Date of Birth:')[1]).split('<td>')[1]).split('</td>')[0]
        # listed?
        if len(dob.split()) > 0:
            #  just grab year
            year = dob.split()[-1]
        else:
            year = ''
        # nationality
        country = ((soup_details.split('Country of Birth:')[1]).split('<td>')[1]).split('</td>')[0]
        # siblings
        # do we have them listed?
        if len(soup_details.split('Siblings:')) > 1:
            sibs =  ((soup_details.split('Siblings:')[1])).split('</td>')[0]
            sibs = sibs.split('">')[1:]
            # loop and update
            for i in range(len(sibs)):
                sibs[i] = sibs[i].split('<')[0]
        else:
            sibs = []
                
        names.append(name)
        sires.append(sire)
        dams.append(dam)
        sexes.append(sex)
        years.append(year)
        siblings.append(sibs)
        countries.append(country)

        
            
    startSmall += 20
    if startSmall%100 == 0:
        startLarge += 100




# now, save this dataset
def replaceWeird(st):
    sto = st.replace("'","")
    sto = st.replace('"','')
    sto = st.replace("'",'')
    return sto

# loop through things and replace any weirdos
for i in range(len(names)):
    names[i] = replaceWeird(names[i])
    dams[i] = replaceWeird(dams[i])
    sires[i] = replaceWeird(sires[i])
    sexes[i] = replaceWeird(sexes[i])
    years[i] = replaceWeird(years[i])
    countries[i] = replaceWeird(countries[i])
    for j in range(len(siblings[i])):
        siblings[i][j] = replaceWeird(siblings[i][j])



# save to json
import json

v = []
for i in range(len(names)):
    v.append( {"name":names[i], "dam":dams[i], "sire":sires[i], "sex":sexes[i],
               "year":years[i], "countries":countries[i], "siblings":siblings[i] } )

# dump to file
f = open(saveFilejson,'w')
f.write(json.dumps(v,indent=2))
f.close()
    
