获取 cleanExportData.zip   

1.将cleanExportData 解压入根目录下的data_resource（如果没有，自行创建）  
2.依次执行 split_train_dev_test.py > split_by_maxlen.py（需要设置段落最大长度和单句最大长度）   
3.在 data_resource/split_by_maxlen/p{设置的段落最大长度}_s{设置的单句最大长度}/ 文件夹下会有train.txt,dev.txt,test.txt 三个文件  

