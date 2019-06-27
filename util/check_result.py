# from untils.log_trace import *


class  CheckResult():
    def dict_value(self,key,actual):
        try:
            if key in actual:
                return actual[key]
            else:
                for keys in actual:

                    return self.dict_value(key,actual[keys])
        except Exception as e:
            logging.error(e)
            return None

    def cmpdict(self,expect,actual,equal):
        logging.info("Begin to check result of  testcase.")
        is_dict = isinstance(expect,dict) and isinstance(actual,dict)
        if is_dict:
            if equal == "equal":
                for key in expect.keys():
                    if expect[key] == self.dict_value(key,actual):
                        logging.info("%s is equal to %s" %(expect[key],self.dict_value(key,actual)))
                        return True
                    else:
                        logging.error("%s is not equal to %s" %(expect[key],self.dict_value(key,actual)))
                        return False

            if equal == "notequal":
                for key in expect.keys():
                    if key != self.dict_value(key,actual):
                        logging.info("%s is not equal to %s" %(expect[key],self.dict_value(key,actual)))
                        return True
                    else:
                        logging.error("%s is equal to %s" %(expect[key],self.dict_value(key,actual)))
                        return False

            else:
                logging.error("Operator :%s is not support now,you can define it in file[check_result.py]" %equal)


        else:
            logging.error("Expect or actual  result is not dict,check it in  excel. ")