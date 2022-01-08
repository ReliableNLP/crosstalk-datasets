'''

主要用来检查处理后的篇章的句子是否0，1开头


'''


import json,io,os,sys
from log import get_logger

this_dir = os.path.split(os.path.realpath(__file__))[0]
base_dir = os.path.join(os.path.dirname(this_dir))
data_dir = os.path.join(base_dir,'data_resource')
export_dir = os.path.join(data_dir,'cleanExportData')
result_dir = os.path.join(data_dir,'reduce_data')
logger = get_logger()


def check_data_by_mark(mark):
    base_data_dir = os.path.join(result_dir,mark)
    for root, dirs, files in os.walk(base_data_dir, topdown=False):
        for file in files:
            if file.endswith('.txt'):
                file_content = io.open(os.path.join(root,file)).readlines()
                for line in file_content:
                    if line.startswith('0:') or line.startswith('1:'):
                        continue
                    else:
                        raise RuntimeError(f'错误句{line}')



if __name__ == '__main__':
    check_data_by_mark('train')
    check_data_by_mark('test')
    check_data_by_mark('dev')
