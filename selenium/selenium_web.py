import values
import details
from selenium import webdriver
accesstype = ""
repo_name=""
print(" 1) Do you want to import already existed repo ")
print(" 2) Do you want to Create anew one")
work=int(input("Select any one from the above :- "))

def sign_in():
        browser = webdriver.Chrome()
        browser.get("https://github.com/")

        # finding element by text
        sign_in_link = browser.find_element_by_link_text("Sign in")

        # clicking that element
        sign_in_link.click()

        # finding element on webpage and select it using class name
        username_box = browser.find_element_by_id("login_field")
        password_box = browser.find_element_by_id("password")

        # stimulating a user typing text
        username_box.send_keys(details.username)
        password_box.send_keys(details.password)
        password_box.submit()

def common_questions():
        repo_name=input("Enter the desired repo name :- ")
        accesstype=input("Do you want your Repo to be public or private :- ")

def selection_private_public_repo():
        browser = webdriver.Chrome()
        #private or public
        if accesstype=="public":
            public_key=browser.find_element_by_id("repository_visibility_public")
            public_key.click()

        elif accesstype=="private":
            private_key=browser.find_element_by_id("repository_visibility_private")
            private_key.click()

def creation_repo():
        common_questions()
        desc=input("Do you want to insert description (T/F):- ")
        if desc== "T":
            desc_data=input("Description = ")
        defaultbranchname=input("Do you want to Update default branch name (T/F):- ")
        if defaultbranchname== "T":
            name=input("Name = ")
        gitignore=input("Do you want to add git ignore file (T/F):- ")
        if gitignore== "T":
            gitignore_type=input("Select template for gitignore file (Vsc=Visualstudiocode) (Blank=none)")
        ReadmeFile=input("Do you want to add readme file (T/F):- ")
        #sign in function
        sign_in()
        #click on new_box
        browser.get("https://github.com/new")

        #input a repo name
        repo_name_field= browser.find_element_by_id("repository_name")
        repo_name_field.send_keys(repo_name)

        #adding description
        if desc== "True":
            desc_button=browser.find_element_by_id("repository_description")
            desc_button.send_keys(desc_data)
        selection_private_public_repo()
        #selecting type of gitignore file
        if gitignore== "T":
            gitignore_selector=browser.find_element_by_id("repository_gitignore_template_toggle")
            gitignore_selector.click()
            #finding element using xpath
            gitignore_type_key=browser.find_element_by_xpath("//span[.='None']")
            gitignore_type_key.click()
            if gitignore_type== "Blank":
                pass
            elif gitignore_type=="Vsc":
                gitignore_type_vsc_key=browser.find_element_by_xpath("//span[.='VisualStudio']")
                #gitignore_type_vsc_key=browser.find_element_by_id("repository_gitignore_template_VisualStudio")
                gitignore_type_vsc_key.click()

        #selecting readme file
        if ReadmeFile=="T":
            readme_select =browser.find_element_by_id("repository_auto_init")
            readme_select.click()
        #changing default branch name
        if defaultbranchname== "T":
            browser.get("https://github.com/settings/repositories")
            default_branch=browser.find_element_by_name("default_branch_name")
            default_branch.send_keys(name)
            update_button=browser.find_element_by_link_text("Update")
            update_button.click()

def import_repo():
    url=input("Your old repository’s clone URL")
    common_questions()
    sign_in()
    browser.get("https://github.com/new/import")
    clone_url=browser.find_element_by_id("vcs_url")
    clone_url.click()
    clone_url.send_keys(url)
    #input a repo name
    repo_name_field= browser.find_element_by_id("repository_name")
    repo_name_field.send_keys(repo_name)
    selection_private_public_repo()

if work==1:
    import_repo()
elif work==2:
    creation_repo()
