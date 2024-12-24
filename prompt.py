# 读取所有的 prompt
prompts = {
    "生成简单算法代码": [
        {
            "prompt": "生成一个二叉树的Python实现，包括插入、查找和遍历功能。",
            "save_path": "二叉树"
        },
        {
            "prompt": "请写一个Python函数，使用递归实现快速排序算法。",
            "save_path": "快速排序"
        },
        {
            "prompt": "用Python实现一个深度优先搜索（DFS）算法，遍历给定图的所有节点。",
            "save_path": "深度优先搜索"
        },
        {
            "prompt": "生成一个Python实现的广度优先搜索（BFS）算法，寻找从起点到终点的最短路径。",
            "save_path": "广度优先搜索"
        },
        {
            "prompt": "请写一个Python函数，判断一个字符串是否是回文字符串。",
            "save_path": "回文字符串"
        },
        {
            "prompt": "生成一个Python实现的归并排序算法。",
            "save_path": "归并排序"
        },
        {
            "prompt": "请写一个Python程序，计算给定列表的所有子集。",
            "save_path": "子集"
        },
        {
            "prompt": "实现一个二分查找算法，输入一个排序数组和目标值，返回目标值的索引。",
            "save_path": "二分查找"
        },
        {
            "prompt": "用Python实现一个贪心算法，解决背包问题。",
            "save_path": "贪心算法"
        },
        {
            "prompt": "请写一个Python程序，检测一个数组是否有重复元素，并返回布尔值。",
            "save_path": "重复元素"
        },
    ],
    "生成针对框架的代码": [
        {
            "prompt": "生成一个Django视图函数，实现用户登录功能。",
            "save_path": "Django视图函数"
        },
        {
            "prompt": "请写一个Django模型，表示一个博客文章，包括标题、内容和发布时间。",
            "save_path": "Django模型"
        },
        {
            "prompt": "生成一个Django表单类，用于注册新用户，包含字段验证。",
            "save_path": "Django表单类"
        },
        {
            "prompt": "请写一个Django的URL配置，将多个视图与URL进行映射。",
            "save_path": "Django URL配置"
        },
        {
            "prompt": "生成一个Django视图，支持文件上传功能，返回上传的文件路径。",
            "save_path": "Django视图"
        },
        {
            "prompt": "生成一个Flask表单，接受用户的用户名和密码进行登录验证。",
            "save_path": "Flask表单"
        },
        {
            "prompt": "用Flask实现一个简单的博客应用，包含文章列表和详细页面。",
            "save_path": "Flask博客应用"
        },
        {
            "prompt": "请写一个Flask中间件，用于记录请求的日志。",
            "save_path": "Flask中间件"
        },
        {
            "prompt": "用Flask实现一个JWT认证系统，保护API接口。",
            "save_path": "Flask JWT认证系统"
        },
        {
            "prompt": "生成一个Flask应用，支持文件上传并保存到服务器。",
            "save_path": "Flask应用"
        },
        {
            "prompt": "用PyTorch实现一个简单的前馈神经网络，用于二分类任务。",
            "save_path": "PyTorch前馈神经网络"
        },
        {
            "prompt": "请写一个PyTorch优化器，使用Adam优化器训练模型。",
            "save_path": "PyTorch优化器"
        },
        {
            "prompt": "生成一个PyTorch实现的自注意力机制（self-attention）。",
            "save_path": "PyTorch自注意力机制"
        },
        {
            "prompt": "用PyTorch实现一个简单的生成对抗网络（GAN）。",
            "save_path": "PyTorch GAN"
        },
        {
            "prompt": "请写一个PyTorch模型，使用迁移学习进行图像分类。",
            "save_path": "PyTorch迁移学习"
        },
        {
            "prompt": "生成一个PyTorch实现的多层感知机（MLP）模型，进行回归任务。",
            "save_path": "PyTorch MLP"
        },
    ],
    "生成复杂需求的代码": [
        {
            "prompt": "请实现一个完整的Django用户认证系统，包含注册、登录、注销、密码重置等功能。",
            "save_path": "Django用户认证系统"
        },
        {
            "prompt": "生成一个Django博客应用，支持文章创建、编辑、删除、评论功能，并能对文章进行分类。",
            "save_path": "Django博客应用"
        },
        {
            "prompt": "写一个Flask应用，支持用户注册、发送电子邮件验证、激活账户功能。",
            "save_path": "Flask应用"
        },
        {
            "prompt": "实现一个基于PyTorch的图像分类模型，包含数据预处理、训练过程、评估和保存模型的功能。",
            "save_path": "PyTorch图像分类模型"
        },
        {
            "prompt": "生成一个完整的Django REST API，提供用户注册、文章管理、评论功能，支持JSON格式请求和响应。",
            "save_path": "Django REST API"
        },
        {
            "prompt": "写一个深度学习模型，使用PyTorch实现一个图像分割任务，包含数据处理、训练和评估过程。",
            "save_path": "深度学习模型"
        },
        {
            "prompt": "生成一个Flask和MongoDB结合的聊天应用，支持实时消息发送和接收。",
            "save_path": "Flask和MongoDB结合的聊天应用"
        },
        {
            "prompt": "实现一个多线程的Python程序，模拟一个小型银行的存取款系统，支持并发用户操作。",
            "save_path": "多线程的Python程序"
        },
        {
            "prompt": "为以下Flask应用的API接口生成测试用例，测试POST请求的正确性和异常处理。",
            "save_path": "Flask API接口测试用例"
        },
        {
            "prompt": "为以下PyTorch训练代码生成测试用例，验证模型训练过程中的损失计算是否正确。",
            "save_path": "PyTorch训练代码测试用例"
        },
        {
            "prompt": "为以下Flask应用的文件上传功能生成测试用例，验证文件上传是否成功。",
            "save_path": "Flask文件上传测试用例"
        },
    ],
    "生成已有项目代码的测试用例": [
        {
            "prompt": """以下是一个用 Flask 实现的用户管理系统的代码：

<code>

请为上述代码生成一组测试用例，测试以下功能：
1. 创建用户时的成功和失败场景（如用户已存在的情况）。
2. 获取所有用户时的正确性。
3. 根据用户 ID 获取单个用户的正确性和用户不存在时的错误处理。
4. 删除用户时的成功和失败场景。

要求：
- 测试用例使用 Python 的 unittest 框架。
- 测试代码应可直接运行，覆盖代码的主要功能。
- 包括必要的设置和清理操作。
""",
            "project_path": "./test_project/RestfullAPI",
            "save_path": "Flask API接口测试用例"
        },
        {
            "prompt": """以下是一个多线程文件处理工具的代码，用于统计文件的行数：

<code>

请为上述代码生成一组测试用例，测试以下功能：
1. 单个文件的行数统计是否正确。
2. 多个文件的行数统计是否正确。
3. 在多线程环境下是否能够正确统计所有文件的行数。
4. 针对不存在文件或空目录的处理。

要求：
- 测试用例使用 Python 的 unittest 框架。
- 测试代码应可直接运行，覆盖代码的主要功能。
- 包括必要的设置和清理操作。
- 如果需要创建测试文件，请在测试用例中提供创建和删除这些文件的逻辑。
""",
            "project_path": "./test_project/multiThreadDownload",
            "save_path": "多线程文件处理工具测试用例"
        },
        {
            "prompt": """以下是一个简单聊天机器人的代码：

<code>

请为上述代码生成一组测试用例，测试以下功能：
1. 针对已知输入（如 "hello"、"how are you"、"bye"）返回正确响应。
2. 针对未知输入返回默认响应。
3. 机器人是否区分大小写（如 "Hello" 和 "hello" 返回相同响应）。

要求：
- 测试用例使用 Python 的 unittest 框架。
- 测试代码应可直接运行，覆盖代码的主要功能。
- 包括必要的设置代码。
""",
            "project_path": "./test_project/chatBot",
            "save_path": "聊天机器人代码测试用例"
        },
    ]
}