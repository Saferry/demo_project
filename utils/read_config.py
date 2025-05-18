# 导入 PyYAML 库
import yaml

# 定义 ReadConfig 类，用于读取 YAML 配置文件
class ReadConfig:
    def __init__(self, config_path):
        """
        初始化 ReadConfig 类。
        :param config_path: YAML 配置文件的路径
        """
        config_path = r"E:\wangzl\svn\UI_test_prj\config\web_ui_lms_uat.yaml"
        with open(config_path, "r", encoding="utf-8") as file:
            # 加载 YAML 文件内容
            self.config = yaml.safe_load(file)

    def get_base_url(self):
        """
        获取基础 URL。
        :return: 基础 URL
        """
        return self.config["base_url"]
    
    def get_user_name(self):
        """
        获取基础 username。
        :return: 用户 账号
        """
        return self.config['login']["username"]
        
    def get_pass_word(self):
        """
        获取基础 password。
        :return: 用户 密码
        """
        return self.config['login']["password"]

    def get_login_credentials(self):
        """
        获取登录凭证。
        :return: 登录用户名和密码
        """
        return self.config["login"]["username"], self.config["login"]["password"]

    def get_test_data(self, key):
        """
        获取测试数据。
        :param key: 测试数据的键
        :return: 测试数据
        """
        return self.config["test_data"].get(key, {})


if __name__ == '__main__':
    # 指定配置文件路径
    config_path = r"E:\wangzl\svn\UI_test_prj\config\web_ui_lms_uat.yaml"
    read_data = ReadConfig(config_path)
    # 获取测试数据：新用户
    data = read_data.get_test_data('new_user')
    username = read_data.get_user_name()
    print('---------')
    print(data, username)