from util.operation_excel import OperationExcel
from data import data_config


class GetData:

    def __init__(self):
        self.oper_excel = OperationExcel()

    # 获取用例个数
    def get_case_lines(self):
        return self.oper_excel.get_lines()

    # 获取是否执行
    def get_is_run(self,row):
        flag = None
        col = int(data_config.global_var.get_run())
        run_model = self.oper_excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取请求方式
    def get_request_method(self,row):
        col = int(data_config.global_var.get_request_type())
        request_method = self.oper_excel.get_cell_value(row,col)
        return request_method

    def get_requset_url(self,row):
        col = int(data_config.global_var.get_url())
        requset_url = self.oper_excel.get_cell_value(row,col)
        return requset_url

    #获取请求数据
    def get_request_data(self,row):
        col = int(data_config.global_var.get_request_data())
        data = self.oper_excel.get_cell_value(row,col)
        if data == '':
            return None
        return data
    # --------------------------------------------------------------------

    # 通过获取请求关键字拿到data数据
    '''def get_data_value(self,row):
        oper_json = OperationJson('../dataconfig/request_data.json')
        request_data = oper_json.get_data(self.get_request_data(row))
        return request_data'''


    #获取预期结果
    def get_expect_data(self,row):
        col = int(data_config.global_var.get_expect())
        expect = self.oper_excel.get_cell_value(row,col)
        return expect

    #写入数据
    def write_result(self,row,value):
        col = int(data_config.global_var.get_result())
        self.oper_excel.write_value(row,col,value)

    #获取依赖数据的key
    '''def get_depend_key(self,row):
        col = int(data_config.get_data_depend())
        depend_key = self.oper_excel.get_cell_value(row,col)
        if depend_key == '':
            return None
        else:
            return depend_key'''

    #判断是否有case依赖
    '''def is_depend(self,row):
        col = int(data_config.get_case_depend())
        depend_case_id = self.oper_excel.get_cell_value(row,col)
        if depend_case_id == '':
            return None
        else:
            return depend_case_id'''

    #获取请求依赖字段
    '''def get_depend_field(self,row):
        col = int(data_config.get_field_depend())
        data = self.oper_excel.get_cell_value(row,col)
        if data == '':
            return None
        else:
            return data'''



