# renamer

## 介绍

python编写的批量重命名文件工具，支持遍历子目录重命名及正则表达式匹配重命名

## 使用说明

* --directory，-d：需要重命名的文件所在目录
* --target， -t：文件名中需要替换掉的字符串
* --replace， -r：替换的字符转
* --subdirectory： 是否包含子目录选项，有这个参数时会遍历子目录并重命名符合条件的文件名
* --regex：正则表达式匹配规则，使用正则匹配文件名中符合条件的字符串。有这个入参时，会忽略--target，-t的入参
