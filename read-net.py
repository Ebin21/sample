# from pyodide.http import pyfetch

# import pandas as pd

# filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"


# async def download(url, filename):

#     response = await pyfetch(url)

#     if response.status == 200:

#         with open(filename, "wb") as f:

#             f.write(await response.bytes())

#     await download(filename, "example1.txt")

# print("done")
import urllib.request

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"

urllib.request.urlretrieve(url, "example1.txt")

print("Download completed!")
example1 = "example1.txt"
file1 = open(example1, "r")
print(file1.name)
print(file1.mode)
FileContent = file1.read()
print(FileContent)
type(FileContent)
file1.close()
