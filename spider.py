from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from git import Repo
import re
import time
import os
import shutil

driver = webdriver.Chrome()

# log in
str_user = "netario"
str_pwd = "*******"
repo_path = 'C:/Workspace/'
repo_link = 'https://github.com/netario/leetcode-solutions/blob/master/'

driver.get("https://leetcode.com/accounts/login/")
driver.find_element_by_id("id_login").send_keys(str_user)
driver.find_element_by_id("id_password").send_keys(str_pwd + Keys.RETURN)
files_set = []


# scratch text
def scratch(link):
    ret = ""

    # get problem info
    driver.get(link)
    title = driver.find_element_by_xpath("//div[contains(@class, 'question-title')]//h3").text
    [problem_id, problem_name] = title.split(". ", 1)
    filename = problem_id + '_' + problem_name.lower().replace(" ", "_")
    print filename

    # get submission page
    if link[-1] != '/':
        link += "/"
    link = link.replace('/description/', '/submissions/')
    driver.get(link)
    time.sleep(0.5)

    # get submission history
    table = driver.find_element_by_class_name('tab-content')
    table_rows = table.find_elements_by_tag_name('tr')
    print "row:", len(table_rows)
    table_cols = table_rows[0].find_elements_by_tag_name('th')
    print "col:", len(table_cols)

    # find accepted record
    for row in table_rows:
        if row == table_rows[0]:
            continue
        rec_timestamp = row.find_elements_by_tag_name('td')[0].text
        rec_state = row.find_elements_by_tag_name('td')[1].text
        rec_runtime = row.find_elements_by_tag_name('td')[2].text
        rec_lang = row.find_elements_by_tag_name('td')[3].text
        if rec_state == 'Accepted':
            ret += "[" + rec_lang + "] leetcode " + problem_id + " : \n"\
                    + " |SubmitTime " + rec_timestamp\
                    + " |RunTime " + rec_runtime
            url = row.find_element_by_class_name('text-success').get_attribute('href')
            driver.get(url)
            stat = driver.find_element_by_class_name("callout").text
            ret += " "+ re.search(r'beats{1}.*%', stat).group()

            # fetch solution
            contents = driver.find_element_by_xpath("//div[contains(@class, 'ace_layer ace_text-layer')]").text
            ret += " |Lines " + str(contents.count('\n') + 1) + '\n'

            # store solution
            if not os.path.exists("./solutions"):
                os.makedirs("./solutions")
            fullname = filename + ".cpp"
            f = open("./solutions/" + fullname, 'w+')
            f.write(contents)
            f.close()

            # copy file
            old_path = "./solutions/" + fullname
            new_path = repo_path + filename + ".cpp"
            shutil.copy(old_path, new_path)
            files_set.append(fullname)
            ret += repo_link + fullname + "\n"
            print ret
            break
    return ret


def git():
    repo = Repo(repo_path)
    assert not repo.bare

    repo.index.add(files_set)
    repo.index.commit(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), )
    repo.remotes.origin.push()

f = open('input.txt')
text = f.read() + '\n'
pattern = re.compile('http{1}.*\n{0}')
arr = re.findall(pattern, text)
output_content = ""
for link in arr:
    while True:
        try:
            output_content += scratch(link)
            break
        except Exception as err:
            print(err)
git()
print "--------------------------------------------------------------"
print output_content
