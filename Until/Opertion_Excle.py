# encoding: utf-8

"""
# @Time    : 25/10/2019 11:43 上午
# @Author  : Function
# @FileName    : Opertion_Excle.py
# @Software: PyCharm

操作 Excle 类  提取对应行与列的数据
"""
import xlrd
from xlutils.copy import copy


from  Config.setting import *



class OperExcel:

    def __init__(self,sheet_id,file_name=None,):
        """
        构造函数 初始化类对象属性
        :param file_name: 文件名称
        :param sheet_id:  传入的sheetID
        """
        if file_name:  # 如果有新的值那么就使用下面的值
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = path_excle  # 如果不存在文件名的传入那么就使用下面默认的值
            self.sheet_id = sheet_id  # 默认加载第一个sheet里面的数据
        self.data = self.get_data()

    """
    =========---常规数据处理----==========
    """
    def get_data(self):
        """
        获取整体的Excle数据
        :return: tables
        """
        data1  = xlrd.open_workbook(self.file_name)
        tables = data1.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        """
        返回Excle中含有多少行 也就是含有多少case
        :return:
        """
        tables = self.get_data()
        return tables.nrows

    def get_cell_value(self,row,col):
        """
        获取单单元格的内容
        :param row: 行
        :param col: 列
        :return:
        """
        return self.data.cell_value(row,col)

    def write_value(self,row,col,value):
        """
        先Excle中写入数据
        :param row:
        :param col:
        :param value:
        :return:
        """
        read_data = xlrd.open_workbook(self.file_name,formatting_info=True)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(self.sheet_id)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)
    """
    =====------接口中的依赖数据处理------========
    """
    def get_row_data(self,CaseId):
        """
        拿到要被执行的整行内容
        :param CaseId:
        :return:
        """
        row_num = self.get_row_num(CaseId)
        row_data = self.get_row_value(row_num)
        return row_data

    def get_row_num(self,CaseId):
        """
        返回caseID的行号
        :param CaseId:
        :return:
        """
        Num = 0
        clos_data = self.get_cols_data()
        for col_data in clos_data:
            if CaseId in col_data:
                return Num
            Num = Num+1

    def get_row_value(self,row):
        """
        根据caseID-row拿到需要做执行整个一列的case行
        :param row:
        :return:
        """
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    def get_cols_data(self,col_id=None):
        """
        拿到正列的内容 默认拿第一列的内容
        :param col_id:
        :return:
        """
        if col_id is not None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    p = OperExcel(0)
    a = p.get_cols_data()
    print(a)
    # for i in range(len(a)):
    #     print(i)
    #     print(p.get_row_value(i))


