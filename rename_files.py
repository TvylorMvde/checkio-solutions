import os

# path = r'X:/Downloads/SB_audio'

# cd = 1

# # SB rename files

# for directory in os.listdir(path):
#     for count, filename in enumerate(os.listdir(os.path.join(path,directory)), start=1):
#         dir_path = os.path.join(path, directory)
#         if count < 10:
#             count = "0" + str(count)
#         new_name = 'BR5_CD{}_0{}.srt'.format(str(cd), str(count))
#         os.rename(os.path.join(dir_path, filename),
#                   os.path.join(dir_path, new_name))
#     cd += 1
        
            
        

# WB rename files
# ---------------------------------------------------------------------------------------------

# for directory in enumerate(os.walk(path), start=1):

#     if count < 10:
#         count = "0" + str(count)
#     new_name = 'BR5_WB_0{}.mp3'.format(str(count))
#     os.rename(os.path.join(path, filename), os.path.join(path, new_name))


# rename tags <strong>, <em> and hard space: "&nbsp;"
# ---------------------------------------------------------------------------------------------

path = r'X:/Downloads/test'

for directory in os.listdir(path):
    for filename in os.listdir(os.path.join(path, directory)):
        file_path = os.path.join(os.path.join(path, directory), filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().replace("<strong>", "<b>").replace(
                "</strong>", "</b>").replace("<em>", "<i>").replace("</em>", "</i>").replace("&nbsp;", " ")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)







