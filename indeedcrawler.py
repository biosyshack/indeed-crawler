from indeed import IndeedClient
import time

client = IndeedClient(publisher = '')

params = {
    'q' : "internship",
    'l' : "Zurich",
    'userip' : "1.2.3.4",
    'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)",
    'radius' : 50,
    'limit' : 100,
    'co' : 'ch',
    'sort' : 'date'
}

search_response = client.search(**params)

filename = 'jobs_'+str(time.localtime()[0])+str(time.localtime()[1])+str(time.localtime()[2])+'.txt'

with open(r'export path'+filename,'w') as textfile:
    textfile.write('acquisition time: '+str(time.localtime()[3])+':'+str(time.localtime()[4])+'\n\n')
    for i in range (0,len(search_response)):
        reltime = search_response['results'][i]['formattedRelativeTime']
        jobtitle = search_response['results'][i]['jobtitle']
        company = search_response['results'][i]['company']
        url = search_response['results'][i]['url']
        textfile.write(reltime+'\t'+jobtitle+'\t company: '+company+'\n'+url+'\n\n')
textfile.close()
