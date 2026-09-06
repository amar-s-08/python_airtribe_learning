import json 
from pathlib import Path

# Base_Dir = "/Users/amars/Documents/Python Airtribe/task-project/tasks/data"
Base_Dir : Path = Path(__file__).resolve().parent.parent / "data"
#__file__ is the current file path
#resolve() is to get the absolute path
#parent.parent is to go up two levels


def read_json(file_name: str) -> list:
    # r -> stands for reading the data from the file
    # U should not do
    # with open(file_path,"r"):
    #     return json.load(file)
    # because it will not close the file automatically
    # and it will cause a memory leak
    # and it will not be a good practice
    # and it will not be a good practice to open and close the file manually
    file_path = Base_Dir / file_name
    with open(file_path,"r") as file:
        return json.load(file)

def write_json(file_name: str, data: list):
    file_path = Base_Dir / file_name
    with open(file_path,"w") as file:
        json.dump(data, file, indent=2)
    # w -> stands for writing the data to the file
    # indent -> stands for the number of spaces to indent the data
    # U should not do
    # with open(file_path,"w"):
    #     json.dump(data, file, indent=4)
