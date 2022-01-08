

import json,io,os,sys
from log import get_logger
'''
将train,dev,test 按篇章最多字数，和单句最多字数转化为三个文件

'''


this_dir = os.path.split(os.path.realpath(__file__))[0]
base_dir = os.path.join(os.path.dirname(this_dir))
data_dir = os.path.join(base_dir,'data_resource')
export_dir = os.path.join(data_dir,'cleanExportData')
result_dir = os.path.join(data_dir,'reduce_data')
split_dir = os.path.join(data_dir,'split_by_maxlen')




def datasets_split(mark,para_max_len,sent_max_len):
    datasets_split_dir = os.path.join(split_dir,f'p{para_max_len}_s{sent_max_len}')
    os.makedirs(datasets_split_dir,exist_ok=True)
    datasets_ori_dir = os.path.join(result_dir,mark)
    save_file = os.path.join(datasets_split_dir,f'{mark}.txt')
    all_reduce_line = []
    this_para_nums = 0
    for root, dirs, files in os.walk(datasets_ori_dir, topdown=False):
        for file in files:
            if file.endswith('.txt'):
                one_para_contents = io.open(os.path.join(datasets_ori_dir,file),'r').readlines()
                for line_idx in range(len(one_para_contents)):
                    line = one_para_contents[line_idx]
                    # 如果该行字数多于指定单句最大长度，裁剪
                    if len(line) > sent_max_len:
                        line = line[:sent_max_len]
                    # 如果加上这句以后，当前的字数超了，就直接切到下一段
                    if this_para_nums + len(line) > para_max_len:
                        all_reduce_line.append('\n')
                        all_reduce_line.append(line)
                        this_para_nums = len(line)
                    else:
                        all_reduce_line.append(line)
                        this_para_nums += len(line)
                # 每个篇章之间隔离开来
                all_reduce_line.append('\n')
                this_para_nums = 0


                        

    io.open(save_file,'w').writelines(all_reduce_line)

    




def reduce_by_maxlen(para_max_len,sent_max_len):


    datasets_split('train',para_max_len,sent_max_len)
    datasets_split('dev',para_max_len,sent_max_len)
    datasets_split('test',para_max_len,sent_max_len)


if __name__ == '__main__':
    reduce_by_maxlen(1024,128)
