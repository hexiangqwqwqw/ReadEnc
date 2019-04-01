# -*- coding:utf-8 -*-
from osgeo import ogr


def ReadENC_File(encfile):
    ogr.RegisterAll()                                       #注册所有驱动
    fp = ogr.Open(encfile, 0)                               #打开ENC文件
    print('文件类型为{}'.format(fp.GetDriver().GetName()))       #输出驱动类型
    layercount = fp.GetLayerCount()                         #获取ENC文件图层总数
    print('图层总数:{}'.format(layercount))                      #输出图层总数
    for num in range(layercount):                           #建立图层循环，循环体内执行输出图层内要素
        layer = fp.GetLayerByIndex(num)
        if layer == None :
            print('fail')
        layer.ResetReading()
        defn = layer.GetLayerDefn()
        fieldcount = defn.GetFieldCount()
        print('第{}图层属性表结构信息:'.format(num))
        for item in range(fieldcount):
            field = defn.GetFieldDefn(item)
            print(field.GetNameRef() + ':' + field.GetFieldTypeName(field.GetType()) + '(' + str(field.GetWidth()) + '.' + str(field.GetPrecision()) + ')')
        print('FeatureCount:{}'.format(layer.GetFeatureCount()))
        while True :
            feature = layer.GetNextFeature()
            if feature == None :
                break
            else:
                print('当前处理第{}个属性值'.format(feature.GetFID()))
                for ifield in range(fieldcount):
                    fielddefn = defn.GetFieldDefn(ifield)
                    otype = fielddefn.GetTypeName()
                    if otype == 'String' :
                        print(feature.GetFieldAsString(ifield).encode('utf-8', 'ignore').decode('utf-8'))#忽略utf8不能读取的部分
                    elif otype == 'Real' :
                        print(feature.GetFieldAsDouble(ifield))
                    elif otype == 'Integer':
                        print(feature.GetFieldAsInteger(ifield))
                    else:
                        print(feature.GetFieldAsString(ifield).encode('utf-8', 'ignore').decode('utf-8'))
    
    
encfile = input('请输入文件路径（请使用\\\分隔）')
ReadENC_File(encfile)
