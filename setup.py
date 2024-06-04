from setuptools import setup,find_packages



from typing import List

def get_req(file_path:str)->List[str]:
    req=[]
    with open(file_path) as f:
        req=f.readlines()
        req=[r.replace('/n',"") for r in req]
    return req






setup(

name="ml project",
description=" an end to end ml project",
author="anupma kumar",
packages=find_packages(),
requires=get_req('requirments.txt')    

)