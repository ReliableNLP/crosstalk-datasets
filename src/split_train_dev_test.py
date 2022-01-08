


import json,io,os,sys
from log import get_logger
'''
将对口相声按8:1:1切成train,dev.test

'''
this_dir = os.path.split(os.path.realpath(__file__))[0]
base_dir = os.path.join(os.path.dirname(this_dir))
data_dir = os.path.join(base_dir,'data_resource')
export_dir = os.path.join(data_dir,'cleanExportData')
result_dir = os.path.join(data_dir,'reduce_data')
logger = get_logger()


def save_datasets(meta_list,mark):
    save_dir = os.path.join(result_dir,mark)
    if os.path.exists(save_dir):
        logger.error('已存在同名数据集，请检查')
    os.makedirs(save_dir)
    all_sent_len = 0
    all_char_len = 0
    all_file_len = 0

    for idx in range(len(meta_list)):
        idx_meta = meta_list[idx]
        meta_roles = idx_meta['roles']
        real_file_path = idx_meta['filePath']
        abs_file_path = os.path.join(export_dir,real_file_path)
        content = io.open(abs_file_path,'r').read()
        reduce_role_content = content.replace(meta_roles[0],'0:').replace(meta_roles[1],'1:')
        all_line = reduce_role_content.split('\n')
        filter_flag = False
        for line in all_line:
            if len(line) > 0 and  not (line.startswith('0:') or line.startswith('1:')):
                logger.error(f'出现错误文本{idx_meta["title"]},已丢弃')
                filter_flag = True
                break
        
        if filter_flag:
            continue

        save_file_path = os.path.join(save_dir,f'{idx}.txt')
        save_config_path = os.path.join(save_dir,f'{idx}.cfg')
        io.open(save_file_path,'w').write(reduce_role_content)
        io.open(save_config_path,'w').write(json.dumps(idx_meta,ensure_ascii=False,indent=4))
        all_char_len += idx_meta['charSize']
        all_sent_len += idx_meta['sentenceSize']
        all_file_len += 1
    logger.info(f'{mark}数据集处理完成,共有{all_file_len}篇文本，{all_sent_len}句子，{all_char_len}字')

def read_export_datas():
    meta_data = io.open(os.path.join(export_dir,'meta.json'),'r').read()
    meta_json = json.loads(meta_data)
    logger.info('因为本项工作仅面向对口相声，故切分数据集时只使用对口相声')
    dk_meta = []

    for meta_entity in meta_json:
        if meta_entity['type'] == '对口相声':
            dk_meta.append(meta_entity)
    logger.info(f'导出数据集共有{len(dk_meta)}篇对口，共有{sum([i.get("sentenceSize") for i in dk_meta])}句子，共有{sum([i.get("charSize") for i in dk_meta])}字')
    logger.info(f'按8:1:1切分为train,dev,test集合，并过滤其中的非对口文本，所有角色都修改为0，1')
    train_meta = []
    dev_meta = []
    test_meta = []
    for entity in dk_meta:
        
        if len(train_meta) < int(len(dk_meta) * 0.8):
            train_meta.append(entity)
            continue
        if len(test_meta) < int(len(dk_meta) * 0.1):
            test_meta.append(entity)
            continue
        dev_meta.append(entity)
    
    
    save_datasets(train_meta,'train')
    save_datasets(dev_meta,'dev')
    save_datasets(test_meta,'test')


    logger.info('=' * 20 + 'FINISH' + '=' * 20)


if __name__ == '__main__':
    read_export_datas()
