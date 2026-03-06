# 专利代理师考试学习系统

## 🌐 在线访问
**GitHub Pages**: https://orphanwarrior.github.io/test-web/study.html

## 📦 快速开始

### 方法一：直接访问在线版本
打开上面的链接即可使用，支持手机、平板、电脑访问。

### 方法二：本地运行
1. 克隆仓库：
```bash
git clone https://github.com/orphanwarrior/test-web.git
cd test-web
```

2. 启动本地服务器：
```bash
python -m http.server 8000
```

3. 访问：http://localhost:8000/study.html

## 🤖 使用 Claude Code 继续开发

### 首次设置
1. 克隆仓库到本地
2. 打开 Claude Code CLI
3. 进入项目目录：
```bash
cd /path/to/test-web
```

### 继续对话
直接对 Claude 说：
- "继续开发专利学习系统"
- "添加新功能：[描述功能]"
- "修复bug：[描述问题]"
- "更新题库"

Claude 会自动读取项目文件并继续之前的工作。

## ✨ 已实现功能

### 核心功能
- ✅ 随机练习（支持10/20/30/50题选择）
- ✅ 按专题练习（30个专题）
- ✅ 错题本（自动收集、状态追踪）
- ✅ 收藏夹（支持笔记）
- ✅ 学习统计（正确率趋势、热力图）

### 题库
- ✅ 专题1：专利法基础知识与权利归属（26题）
- ✅ 专题2：专利代理制度（24题）
- ✅ 专题3：说明书（26题）

## 📱 移动端支持
已优化移动端显示，支持触摸操作。

## 🔄 更新代码到 GitHub

```bash
git add .
git commit -m "描述修改内容"
git push
```

等待1-2分钟后，GitHub Pages 会自动更新。

## 📁 项目结构

```
test-web/
├── study.html              # 主页面
├── 处理后数据/
│   ├── 专题1-题库.json
│   ├── 专题2-题库.json
│   └── 专题3-题库.json
├── 提问.md                 # 提问模板
├── 添加题目.md             # 添加题目模板
└── README.md               # 本文件
```

## 💾 数据存储

学习数据存储在浏览器 localStorage 中：
- `studyStats`: 答题统计
- `wrongQuestions`: 错题记录
- `favorites`: 收藏题目

**注意**：不同设备的数据不会自动同步。

## 🛠️ 技术栈

- 纯 HTML/CSS/JavaScript
- 无需后端服务器
- GitHub Pages 托管

---

**最后更新**: 2026-03-06
**版本**: v1.0
