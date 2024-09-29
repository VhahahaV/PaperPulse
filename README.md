# 📚 PaperPulse

Welcome to **PaperPulse**! 🎉  
A streamlined automated paper query and analysis system designed for researchers. 🧑‍🔬✨

## 🚀 功能特性

- **🔍 自动论文抓取**: 定期从指定网站抓取相关论文。
- **🏷️ 关键词过滤**: 只抓取符合您指定关键词的论文。
- **💡 多语言模型支持**: 热插拔不同的大语言模型（如 GPT、Claude）以满足不同需求。
- **⚡ 实时推送**: 通过 WebSocket 技术，实时将分析结果推送给前端。
- **👥 用户管理**: 提供不同角色的用户管理功能（管理员、普通用户）。

## 🗂️ 项目架构

### 🏗️ 主要应用

- **analysis**: 处理论文分析逻辑。
- **user**: 管理用户注册、登录和权限。
- **paper**: 管理论文的抓取与存储。
- **scheduler**: 处理定时任务。
- **websocket**: 实现实时通信。
- **notification**: 管理通知发送与接收。

## 🛠️ 技术栈

- **🐍 Django**: Web 框架
- **🔗 Django REST Framework**: API 构建
- **📄 drf-yasg**: 用于生成 Swagger 文档
- **🐉 Redis**: 消息队列与缓存机制
- **🌐 WebSocket**: 实时推送
- **⚙️ PostgreSQL/MySQL**: 数据库（根据需要选择）

## 📥 安装与配置

### 1. 克隆项目

```bash
git clone <your-repo-url>
cd PaperPulse
2. 创建虚拟环境并安装依赖
# 创建虚拟环境
conda create -n paperpulse python=3.10
conda activate paperpulse

# 安装依赖
pip install -r requirements.txt
3. 数据库迁移
# 创建数据库迁移
python manage.py makemigrations
python manage.py migrate
4. 创建超级用户
python manage.py createsuperuser
5. 运行开发服务器
python manage.py runserver
访问 👉 http://127.0.0.1:8000/ 以查看您的应用，或通过 👉 http://127.0.0.1:8000/admin/ 访问管理后台。
```

📝 使用指南
🚀 用户通过注册页面注册账户，登录后配置需要抓取的论文网站及相关关键词。
📆 系统将在指定的时间周期内自动抓取指定网页上的论文。
📊 分析结果将通过 WebSocket 实时发送给用户。
📄 API 文档
使用 drf-yasg 生成 API 文档，访问以下地址：

👉 http://127.0.0.1:8000/swagger/

🤝 贡献
欢迎任何人对项目进行贡献！请按照以下步骤：

Fork 本项目 👇
创建您的新分支 (git checkout -b feature/YourFeature) 🌱
提交您的更改 (git commit -m 'Add some feature') 💬
推送到分支 (git push origin feature/YourFeature) 🚀
创建新的 Pull Request 🔄
📜 许可证
本项目使用 MIT 许可证。有关更多信息，请查看 LICENSE 文件。

感谢您查看 PaperPulse！🎉

如有任何问题，请随时联系我。😊

