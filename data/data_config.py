class global_var:

    id = '0'
    name = '1'
    run = '2'
    header = '3'
    cookie = '4'
    request_type = '5'
    url = '6'
    request_data = '7'
    expect = '8'
    response_data = '9'
    result = '10'

    #获取caseid
    def get_id(self):
        return global_var.id

    #获取name
    def get_name(self):
        return global_var.name

    #获取是否运行
    def get_run(self):
        return global_var.run

    def get_header(self):
        return global_var.header

    def get_cookie(self):
        return global_var.cookie

    def get_request_type(self):
        return global_var.request_type

    def get_url(self):
        return  global_var.url

    def get_request_data(self):
        return global_var.request_data

    #获取预期结果
    def get_expect(self):
        return  global_var.expect

    #获取实际返回结果
    def get_response_data(self):
        return global_var.response_data

    #获取测试结果
    def get_result(self):
        return global_var.result
