from git import Repo
import os
import urllib.request


def create_repo_folder(url):
    if os.name == 'nt':
        REPO_DIR = r'D:\test'
    else:
        REPO_DIR = '/tmp/repos'

    folder_name = os.path.join(REPO_DIR, str(url).split('/')[-1])

    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

    except OSError:
        print ('Error: Creating directory. ' + folder_name)

    return folder_name


def clone_repo_to_folder(git_url):

    repo_folder = create_repo_folder(git_url)

    if str(urllib.request.urlopen(git_url).getcode()) == '200':
        Repo.clone_from(git_url, repo_folder)
    return repo_folder
