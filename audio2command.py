from global_params import *
import keyword_commands
import os

##======= extract keyword modules =============##
keyword_module_file_postfix = ".py"
# keyword_module_func_prefix = "keyword_"     # len('keyword_') = 8
keyword_module_dir_name = "keyword_commands"
keyword_module_dir_path = os.path.join(os.path.dirname(__file__), keyword_module_dir_name)
keyword_module_candidate = os.listdir(keyword_module_dir_path)
keyword_module_set = {kw[:-3] for kw in keyword_module_candidate if kw[-3:] == keyword_module_file_postfix and kw[:2] != "__" }
print(keyword_module_set)

##======== listen to audio ================##

##======== convert audio to text ===========##
mytext = "click this please"
int("your text msg: {}".format(mytext))

##======== convert text to commands ==========##
###### stem text ########
mytext_list = mytext.split("\n\t ")


keyword_commands.click.keyword_click()