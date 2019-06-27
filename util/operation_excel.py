import xlrd
from xlutils import copy


class OperationExcel:

    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../case/interface.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    #获取sheets的内容
    def get_data(self):

        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    #获取单元格的行数
    def get_lines(self):

        tables = self.data
        return tables.nrows

    #获取单元格内容
    def get_cell_value(self,row,col):

        tables = self.data
        cell = tables.cell_value(row,col)
        return cell

    def write_value(self,row,col,value):
        '''
       写入到excel数据
       row,col,value
       '''
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        # 用xlwt对象的方法获得要操作的sheet
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    def get_rows_data(self,case_id):

        rownum = self.get_row_num(case_id)
        self.get_row_values(rownum)

    #根据对应的case_id找到对应的行号
    def get_row_num(self,case_id):

        num = 0
        clodata = self.get_col_values()
        for data in clodata:
            if case_id in data:
                return num
            num+=1
        return num

    #根据改行，找到该行的数据
    def get_row_values(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data
    # 根据列号，找到该列的数据
    def get_col_values(self,col):
        if col != None:
            col_data = self.data.col_values(col)
        else:
            col_data = self.data.col_values(0)
        return  col_data

if __name__ == '__main__':
    opexcel = OperationExcel()
    print(opexcel.get_cell_value(1,0))



