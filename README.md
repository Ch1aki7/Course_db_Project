# 高校仪器预约系统 - 后端项目

基于 Flask 的高校仪器预约系统后端 API 服务。

## 技术栈

- **Web 框架**: Flask 3.0.0
- **ORM**: Flask-SQLAlchemy 3.1.1
- **数据库迁移**: Flask-Migrate 4.0.5
- **序列化**: Marshmallow / Flask-Marshmallow
- **API 文档**: Flasgger (Swagger UI)
- **数据库**: MySQL (TiDB Cloud Serverless)
- **数据库驱动**: PyMySQL

## 项目结构

```
.
├── app/                    # 应用核心代码
│   ├── __init__.py        # Application Factory
│   ├── models/            # 数据库模型
│   ├── api/               # API 蓝图
│   │   └── v1/           # API v1 版本
│   ├── services/          # 业务逻辑层
│   └── utils/             # 工具类
│       ├── response.py    # 统一响应格式
│       └── exceptions.py  # 异常处理
├── config.py              # 配置文件
├── run.py                 # 启动入口
├── requirements.txt       # 依赖包
├── env.example           # 环境变量示例
└── README.md             # 项目说明

```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

复制 `env.example` 为 `.env` 并填写配置：

```bash
# Windows
copy env.example .env

# Linux/Mac
cp env.example .env
```

编辑 `.env` 文件，配置数据库连接信息：

```env
# TiDB Cloud 数据库配置
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=your_tidb_host
DB_PORT=4000
DB_NAME=instrument_booking
```

### 3. 初始化数据库

```bash
# 初始化迁移目录
flask db init

# 创建初始迁移
flask db migrate -m "Initial migration"

# 应用迁移
flask db upgrade
```

### 4. 运行应用

```bash
python run.py
```

或使用 Flask CLI：

```bash
flask run
```

应用将在 `http://localhost:5000` 启动。

### 5. 访问 API 文档

启动应用后，访问 Swagger UI 文档：

```
http://localhost:5000/apidocs
```

## 环境变量说明

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `FLASK_ENV` | Flask 环境 (development/testing/production) | development |
| `FLASK_DEBUG` | 是否开启调试模式 | True |
| `FLASK_HOST` | 监听地址 | 0.0.0.0 |
| `FLASK_PORT` | 监听端口 | 5000 |
| `SECRET_KEY` | Flask 密钥 | dev-secret-key-change-in-production |
| `DB_USER` | 数据库用户名 | root |
| `DB_PASSWORD` | 数据库密码 | - |
| `DB_HOST` | 数据库主机 | localhost |
| `DB_PORT` | 数据库端口 | 4000 |
| `DB_NAME` | 数据库名称 | instrument_booking |
| `SSL_VERIFY_CERT` | 是否验证 SSL 证书 | True |

## 开发规范

### Application Factory 模式

项目采用 Flask Application Factory 模式，所有扩展都在 `create_app()` 函数中初始化。

### 目录说明

- **models/**: 数据库模型定义
- **api/v1/**: API 路由，按版本组织
- **services/**: 业务逻辑层，处理复杂业务逻辑
- **utils/**: 工具类，如统一响应格式、异常处理等

### 统一响应格式

使用 `app/utils/response.py` 中的工具函数：

```python
from app.utils.response import success_response, error_response

# 成功响应
return success_response(data={...}, message='操作成功')

# 错误响应
return error_response(message='操作失败', status_code=400)
```

### 异常处理

使用 `app/utils/exceptions.py` 中定义的异常类：

```python
from app.utils.exceptions import ValidationError, NotFoundError

raise ValidationError('数据验证失败', errors={...})
raise NotFoundError('资源未找到')
```

## 数据库迁移

```bash
# 创建迁移
flask db migrate -m "描述信息"

# 应用迁移
flask db upgrade

# 回滚迁移
flask db downgrade
```

## 许可证

MIT License

