from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import requests
import pyautogui

#print('get_post(keyword,web,need_poste_number)')
#print('login(user , passw)')
#print('save_liste(nom_file,list_date ,a_or_write_or_read)')
print('main(web,keyword,link_f,message ,user,passw,email,number_phone,time_sleep,time_sleep_h,link_teweet)')
#print('function for het ip \n ips = get_ip()')
#print('create browser with ip \n crate_browser_for_ip(ip) ')
print('crate_browser_for_ip(ip)')
print('https://proxy.webshare.io')

def save(nom_file ,a_or_write_or_read,text):
    #open file .txt
    file = open(nom_file+'.txt',a_or_write_or_read)
    #add life
    file.write(text+str('\n'))
    #close file 
    file.close()
    
    

# function=================================save()
def save_liste(nom_file,list_date ,a_or_write_or_read):
    #open files .txt
    number = open(nom_file+'.txt',a_or_write_or_read)
    #add items to file
    for numb in list_date:
        #add item 
        number.write(numb +('\n'))
    #close file
    number.close()


#function for change information from file text to liste in progrmation (for lin in index)  
def change_from_file_to_liste(name_file):
    #for open file it's .txt
    items = open(name_file+'.txt','r')
    #create liste for add items
    liste_items = []
    #add items to liste
    for item in items:
        liste_items.append(item)
    #retuen liste
    return liste_items







#path = './browserweb/chromedriver.exe'
web = webdriver.Chrome()







web.get('https://twitter.com')






'''--------------------------------- that for create browser with ip ----------------------------------'''
def enter_proxy_auth(proxy_username, proxy_password):
    pyautogui.FAILSAFE= False
    time.sleep(5)
    # for add user name
    pyautogui.typewrite(proxy_username)
    pyautogui.press('tab')
    # for add pass word
    pyautogui.typewrite(proxy_password)
    #for enter
    pyautogui.press('enter')

def get_ip():
    import requests
    ips = []
    #connect with api 
    date = requests.get("https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25&filters=eyJvcmRlckJ5IjoibGFzdF92ZXJpZmljYXRpb24ifQ%253D%253D", headers={"Authorization": "3g2mnxohwvqcao9qsk5zuzkn3iztovnp5tsijuxj"}).json()['results']
    #that boucl for get ip adress and port
    for n in range(0,25):
        
        ip =[]
        #i need user name
        ip.append(date[n]['username'])
        #i need password
        ip.append(date[n]['password'])
        ip.append(date[n]['valid'])
        #i need password
        ip.append(date[n]['proxy_address'])
        #i need port 
        ip.append(date[n]['port'])
        ips.append(ip)
        ip =[]
    return ips



def crate_browser_for_ip(ip):
	from selenium import webdriver
	#get ip
	PROXY_STR = ip
	time.sleep(2)
	options = webdriver.ChromeOptions()
	time.sleep(2)
	#options = webdriver.FirefoxOptions()
	
	options.add_argument('--proxy-server=%s' % PROXY_STR)
	time.sleep(2)
	
	path = './browserweb/chromedriver.exe'
	# create browser
	web = webdriver.Chrome(path,options=options)
	
	time.sleep(2)
	#for connect with ip whatismyipaddress
	web.get("https://whatismyipaddress.com/")
	#for connect and add username and password
	enter_proxy_auth('fzcgsmaj', 'x43jgrie7jye')
	
	return web





#this function for if twitter is need email
def add_email(web,email,number_phone,time_sleep):
    #that for chek we need email or number phone
    v = web.find_element(by = By.XPATH ,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[1]').text
    print('add ' + v)
    

    if v =='Email address' or 'email' in v or 'Adresse' in v:
        #import time
        time.sleep(time_sleep)
        #click for input
        web.find_element(by = By.CSS_SELECTOR , value='#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input').click()
        #import time
        time.sleep(time_sleep)
        #this for send email
        web.find_element(by = By.CSS_SELECTOR , value='#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input').send_keys(email)
        #import time
        time.sleep(time_sleep)
        #click for button
        web.find_element(by = By.CSS_SELECTOR , value='#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div > div').click()
        
    if v == 'Numéro de téléphone' or 'number' in v or 'Phone' in v:
        #import time
        time.sleep(time_sleep)
        #for click input
        web.find_element(by = By.CSS_SELECTOR , value='#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input').click()
        # import time
        time.sleep(time_sleep)
        #this for send email
        web.find_element(by = By.CSS_SELECTOR , value='#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input').send_keys(number_phone)
        # import time
        time.sleep(time_sleep)
        #click for button
        web.find_element(by = By.CSS_SELECTOR , value='#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div > div').click()
        

    web.refresh()
        





def login(web,user , passw ,email,number_phone,time_sleep):
        web.get('https://twitter.com/i/flow/login')
        time.sleep(time_sleep)
        #add user to ipnut
        web.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(user)

        time.sleep(time_sleep)
        #click for add user 
        web.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
        #add password to input
        time.sleep(time_sleep)
        web.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(passw)

        time.sleep(time_sleep)
        #click button sub
        web.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()

        time.sleep(time_sleep)
        
        #this  for check if twitter  it need number
        

        try:
            #that fucntion for add email or number phone
            add_email(web,email,number_phone,time_sleep)
        except:
            print('')
        













        


# function for get last past for keyword and comment in post
'''__________________________________new function get new post with add new testks__________________'''



def chek(web,keyword,link):
    keyworks = keyword.split(' ')
    def chek_kewors(web,keyworks,text):
        value = 0
        keyword_text = text.split(' ')
        #for keywork in keyworks:
        #    if keywork in text or keywork.upper() in text:
        #        value += 1
        for ky in keyword_text:
            for keyword in keyworks:
                if keyword == ky:
                    value += 1
        return value     
    number_window = web.window_handles
    time.sleep(2)
    web.switch_to.window(number_window[0])
    time.sleep(2)
    web.execute_script("window.open('"+link+"')")
    time.sleep(2)
    number_window = web.window_handles
    time.sleep(2)
    web.switch_to.window(number_window[1])
    time.sleep(15)
    #get all span
    snap = web.find_elements(by  = By.TAG_NAME ,value = 'span')
    value = 0
    return_list_chek_kewors = 0
    for sn in snap:
        for ky in keyworks:
            if  ky in sn.text or ky.upper() in sn.text :
                return_list_chek_kewors = chek_kewors(web,keyworks,sn.text)
                
                if return_list_chek_kewors !=0:
                    print(sn.text)
                    print(return_list_chek_kewors)
                    value = return_list_chek_kewors
                break     
    web.close()
    time.sleep(5)
    web.switch_to.window(number_window[0])
    return value







#that get link
def get_best_link(liste_):
    chek = 1
    best_link_index = [] #liste for best link
    big_number= 0
    iindex = 0 #index
    iindex_save = 0
    for n_1 in liste_:
        for n_2 in liste_:
            if n_1[1] > n_2[1]:
                if n_1[1] >  big_number:
                    big_number = n_1[1]
                    iindex_save = iindex        
            else:
                if n_2[1]  > big_number:
                    big_number = n_2[1]
                    iindex_save = iindex

    print(big_number)
    for n_1 in liste_:
        
        if n_1[1] == big_number:
            break
        iindex += 1
    return liste_[iindex]






def get_best_links(liste_ ,number_for_link):
    last_list=liste_
    index_list = []
    for n in range(0,number_for_link):
        index = get_best_link(liste_)
        index_list.append(index)
        liste_.remove(liste_[index])
    liste_ = last_list
    return index_list
        
    
    


def get_new_post(web,keyword,message,time_sleep):
    #start get link
    web.get('https://twitter.com/search?q='+keyword+'&src=typed_query')
    #import time
    time.sleep(time_sleep)
    
    web.find_element(by = By.XPATH , value ='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a').click()
    print('get_links')
    time.sleep(5)
    # get links
    links = web.find_elements(by = By.TAG_NAME ,value='a')
    # import time
    time.sleep(time_sleep)
    # liste for links
    list_link_value = [] #that list for add list to new list last has link and valeu
    # best link 
    list_link_and_value =[]
    
    continue_ = 0
    
    post= 'noerr'
    
    c = 0 # that canteu for teste
    
    for link in links:    
        if c == 4:
            break
        try:
            if 'status' in link.get_attribute('href'):
                print(link.get_attribute('href'))
                #import time
                time.sleep(5)
                #ckek that function for chik post if good form algoritm it chik text for post
                c += 1
                #import links
                valeu = chek(web,keyword, link.get_attribute('href'))
                
                if  valeu != 0:
                    
                    list_link_and_value = [] #in list i'm add link and value if good i'm see value from number keyword in text
                    
                    list_link_and_value.append(link.get_attribute('href'))
                    list_link_and_value.append(valeu)
                    for ls in list_link_value:
                        try:
                            for ls2 in ls:
                                if link.get_attribute('href') in ls2:
                                    list_link_and_value = []
                                    continue_ = 1
                                    print('continue')
                                    continue
                        except:
                            print('')
                        if link.get_attribute('href') in ls:
                            list_link_and_value = []
                            continue_ = 1
                            print('continue')
                            continue
                    if continue_ == 1:
                        continue
                    list_link_value.append(list_link_and_value)
                    list_link_and_value = []
        
                
        except:
            print('err 134 get links')
    
    print('go to poste')
    index = get_best_link(list_link_value)[1]
    print('--------------\n')
 

    best_link = get_best_link(list_link_value)[0]
    time.sleep(5)
    print('go to poste')
    web.get(best_link)
    time.sleep(5)
    user_for_post = web.find_element(by = By.XPATH , value ='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div/div/a/div/span').text
    time.sleep(5)
    last_message = message
    message = 'Hello' + user_for_post +' '+ last_message
    time.sleep(5)
    try:
        web.find_element(by = By.XPATH , value ='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div/div[3]/div[6]/div/div[3]/div/div/div').click()
    except:
        print('  ')
        post  ='err  in post'
    time.sleep(time_sleep)
    #rhis is a functon for commenti
    try:
        commeti(web,message,time_sleep)
    except:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        print('i have err in comment\n')
        print('in that link \n'+str(best_link))
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    time.sleep(time_sleep)


    
    
    #print(index)
    print('--------------\n')
    return post


    
    
            
            
            
            
        
    
        

def commeti(web,message,time_sleep):
    #message = 'you can get free ebook for health and health food from this link \n https://sites.google.com/view/downloadyourfreeebookhealthyea/home'
    def click_buttunre(web):
        s =  web.find_elements(by=By.TAG_NAME, value='span')
        for n in  range(0, len(s) ):
            if(s[n].text =='Reply'):
                s[n].click



    def post(web,message,time_sleep):
        
        
        #send message text to input
        
        web.find_element(by=By.CSS_SELECTOR, value='.public-DraftStyleDefault-block').send_keys(message)
        time.sleep(time_sleep)
        #web.find_element(by=By.CSS_SELECTOR, value='.public-DraftStyleDefault-block').click()
        try:
            web.find_element(by=By.CSS_SELECTOR, value='div.r-x572qd:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)').click()
        except:
            click_buttunre(web)
            
        time.sleep(time_sleep)
                
        #click for post
        web.find_element(by=By.CSS_SELECTOR, value='div.r-42olwf:nth-child(2) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)').click()
        

    post(web,message,time_sleep)#i need change message


    
    




    
def wp(web,keyword,link_f,link_teweet,time_sleep):
    

    def outo_folow(web,link_f,time_sleep):
        web.get(link_f)
        time.sleep(time_sleep)
        for n in range(1,5+1):
            #click for folow
            web.find_element(by = By.XPATH,value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div['+str(n)+']/div/div/div/div/div[2]/div/div[2]/div').click()

            try:
                unfollow = web.find_element(by = By.XPATH , value ='/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span/span').text
                if unfollow == 'Unfollow':
                    time.sleep(time_sleep)
                    web.find_element(by = By.XPATH , value ='/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span/span').click()
            except:
                print('  ')
                    
            time.sleep(40)
    


    def auto_like(web,time_sleep):
        web.get('https://twitter.com/home')
        time.sleep(time_sleep)
        #get all link
        links = web.find_elements(by = By.TAG_NAME ,value ='a')
        time.sleep(time_sleep)
        #get link from links
        for lin in links:
            if 'status' in lin.get_attribute('href'):
                link = lin.get_attribute('href')
                break
        #go to link
        web.get(link)
        time.sleep(40)
        # click for like
        web.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div/div[3]/div[7]/div/div[3]/div/div/div').click()


    def retwiit(web,keyword,time_sleep):
        web.get('https://twitter.com/search?q='+keyword+'&src=typed_query')
        time.sleep(time_sleep)
        post= 'noerr'
        #click for button latest
        #web.find_element(by = By.XPATH , value ='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a').click()
        web.find_element(by = By.XPATH ,value = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[4]/a/div/div').click()
        # function for get time and chek and click
        
        time.sleep(time_sleep)
        links = web.find_elements(by = By.TAG_NAME , value = 'a')
        time.sleep(time_sleep)
        chik  = 1
        link_liste = []
        
        for link in links:
            if link.get_attribute('href') in link_liste:
                    continue
            if 'status' in link.get_attribute('href'):
                if 'photo' in link.get_attribute('href') or 'like' in link.get_attribute('href') or 'retweet' in link.get_attribute('href'):
                    continue
                else:
                    print('')
                    

                print(link.get_attribute('href'))
                link_liste.append(link.get_attribute('href'))
        def click(web,link,time_sleep):
            
            web.get(link)
            time.sleep(time_sleep)
            try:
                web.find_element(by = By.XPATH , value = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/span/span').click()
            except:
                try:
                    web.find_element(by = By.XPATH , value = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div/div[3]/div[6]/div/div[2]/div/div/div').click()
                except:
                    web.find_element(by = By.XPATH , value = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div/div[3]/div[7]/div/div[2]/div').click()
                
                #web.find_element(by = By.XPATH , value = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div/div[3]/div[7]/div/div[2]/div/div/div').click()
            time.sleep(time_sleep)
            web.find_element(by = By.XPATH , value = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div/div[2]/div').click()

        time.sleep(time_sleep)
        print('\n all links '+str(len(link_liste)) +'\n')
        i_m_post = []
        for link in link_liste:
            if link in i_m_post:
                continue
            try:
                click(web,link,time_sleep)
                i_m_post.append(link)
                time.sleep(80) # i can change time 
                print('reteweet is a good')
            except:
                print('no reteweet \n' + link)
                time.sleep(50)
    try:
        outo_folow(web,link_f,time_sleep)
    except:
        print('err 327')
    
    time.sleep(180)
    for n in range(0,10):
        try:
            auto_like(web,time_sleep)
        except:
            print('"-___- no like"')
            
        time.sleep(179)
    time.sleep(200)
    retwiit(web,keyword,time_sleep)
    



  


def scrolle(web):
    web.get('https://twitter.com/home')
    time.sleep(5)
    driver=web
    
    for n in range(0,4):
        for m in range(0,20):
            driver.find_element(by = By.TAG_NAME, value=  'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(20)
        driver.find_element(by = By.TAG_NAME, value=  'body').send_keys(Keys.HOME)
        time.sleep(2)
        web.refresh()
        time.sleep(2)
        

    







#this is a function for start all function
def start(web,keyword,link_f,message,user,pass_w,email,time_sleep,time_sleep_h,link_teweet):
    con = 0

    for n in range(0,200):
        try:
            #the function fro post and get new post
            post = get_new_post(web,keyword,message,time_sleep)
            #counteur
            con = con  + 1
            print('post all is a' +str(con))                                            
        except:
            print('we have err in function post test number 2')
            try:
                #import function get new post
                post = get_new_post(web,keyword,message,time_sleep)
            except:
                print('err in porst 572')
            
            
        
        print(post)
        time.sleep(10)
        scrolle(web)
        time.sleep(300)
        wp(web,keyword,link_f,link_teweet,time_sleep)
        time.sleep(300)
        web.get('https://www.redbubble.com/i/t-shirt/Vecto-Rafiki-Simba-Lion-Cartoon-by-aminebnrh/48476565.WFLAH?ref=explore-for-you-recently-viewed')
        

        #time
        time.sleep(8000)
        print('sleep 1 4170')
        
        
        web.get('https://twitter.com/home')
        print('sleep 2 4170')



 


#login

def main(web,keyword,link_f,message ,user,passw,email,number_phone,time_sleep,time_sleep_h,link_teweet):
    print('strat twitter')
    web.get('https://twitter.com')
    
    time.sleep(30)

    start(web,keyword,link_f,message,user,passw,email,time_sleep,time_sleep_h,link_teweet)
    time.sleep(time_sleep)





'''   
print('new fuction  main \n main(web,keyword,link_f,message ,time_sleep,time_sleep_h,link_teweet) ')
def main(web,keyword,link_f,message ,time_sleep,time_sleep_h,link_teweet):

    #login(user , pass_w,email,time_sleep)
    #login(web,user , passw ,email,number_phone,time_sleep)
    time.sleep(10)
    print('strat twitter')
    web.get('https://twitter.com')
    
    time.sleep(30)

    start(web,keyword,link_f,message,user,passw,email,time_sleep,time_sleep_h,link_teweet)
    time.sleep(time_sleep)
    

'''
    





