import requests
import json
import setup

PAGEID='187118781444931'
def user_likes_page(user_id,page_id):
    url='https://graph.facebook.com/%d/likes/%d/' %(user_id,page_id)
    parameters={'access_token':setup.TOKEN}
    r=requests.get(url,params=parameters)
    result=json.loads(r.text)
    if result['data']:
        print('True')
    else:
        print('False')

def get_user_info(user_id):
    url='https://graph.facebook.com/v2.4/%s' %user_id
    parameters={'access_token':setup.TOKEN}
    r=requests.get(url,params=parameters)
    result=json.loads(r.text)
    if result['name']:
        print('True')
        print(result)
    else:
        print('False')

def get_user_feed(user_id):
    page_data=list()

    url='https://graph.facebook.com/v2.0/%s/home' %user_id
    parameters={'access_token':setup.TOKEN}
    r=requests.get(url,params=parameters)
    #print(r)
    result=json.loads(r.text)
    if result['data']:
        id=dict()
        for i in result['data']:
            if i['type']=='photo':
                d=i['id']
                id.update(id=i['id'])
                id.update(type=i['type'])
                id.update(id=i['id'])
                id.update(fro=i['from']['name'])

                page_data.append(id)

            #print('-'*150)
        return page_data

    else:
        print(result)
        return

def post_like(obj_id):
    url='https://graph.facebook.com/v2.0/%d/likes' %obj_id

    r = requests.post(url)#, data=
    if r=='true':
        print('Succesfully Liked')
    else:
        print('Did not like Post')

def get_post_id(id):
    full_id=str(id)
    return full_id[full_id.index('_')+1:]

def get_a_photo_comment(user_id):
    url='https://graph.facebook.com/v2.0/%s/home' %user_id
    parameters={'access_token':setup.TOKEN}
    r=requests.get(url,params=parameters)
    #print(r)
    result=json.loads(r.text)

#get_user_feed('me')
#user_likes_page(535202226582363,187118781444931)

class FBot:
    token=''
    url=''

    def __init__(self,token,host,api_v):
        self.token=token;
        self.url=str.strip('https://'+host+'/'+api_v+'/')
        print(self.url)
        pass
    def get_request(self,url):
        parameters={'access_token':self.token}
        r=requests.get(url,parameters)
        return r
    def post_request(self,url):
        parameters={'access_token':self.token}
        r=requests.post(url)#,parameters)
        return r
    def get_post_id(self,id):
        full_id=str(id)
        return full_id[full_id.index('_')+1:]

    def get_user_info(self,user_id):
        url=self.url+'%s' %user_id
        result=json.loads(self.get_request(url).text)
        if result['name']:
            print(result)
        else:
            print('False')

    def like_post(self,obj_id):
        url=self.url+'%s/likes'%obj_id
        result=json.loads(self.post_request(url).text)
        if result=='true':
            print('Success Like')
        else:
            print('Could not like Post')

    def get_feed(self,user_id):
        page_data=list()
        url=self.url+'%s/home'%user_id
        result=json.loads(self.get_request(url).text)
        if result['data']:


            for i in result['data']:
                if i['type']=='photo':
                    id=dict()
                    #print(i)

                    id['id']=i['id']
                    id['type']=i['type']
                    id['fro']=i['from']['name']
                    page_data.append(id)
                    del (id)

                else:
                    print(i['from']['name']+' didn\'t post a Photo')

            #print('-'*150)
            return page_data
        else:
            print(result)
            return





#b=FBot(setup.TOKEN,setup.HOST,setup.API_V)

my_bot=FBot(setup.TOKEN,setup.HOST,setup.API_V)
