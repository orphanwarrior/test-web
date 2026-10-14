# Patent Exam Practice
专利代理师考试学习系统

I made this for my patent agent exam preparation. It is a small browser app for practicing questions, reading explanations and returning to mistakes.

**[Try the app](https://orphanwarrior.github.io/test-web/study.html)**

The interface is in Chinese. There is no sign-up; practice records stay in the current browser.

![Random practice and answer feedback](assets/screenshots/practice.jpg)

*A local demonstration session using the bundled question data.*

## Try a short session

1. Choose **随机练习** and a question count.
2. Select an answer, then click **提交答案** to see the explanation.
3. Use **错题本** or **收藏夹** to revisit questions.
4. Open **学习统计** to see local practice activity.

## What it includes

- Random practice, single-choice and multiple-choice questions.
- Three populated patent-law topics: 26, 24 and 26 questions, **76 in total**.
- Stored answer explanations, wrong-answer review and favorites.
- Learning statistics with trend and activity views.

## How it is built

The app uses HTML, CSS and JavaScript, with JSON files for questions and GitHub Pages for hosting. I used AI coding assistance during development.

There is no server-side account system. `localStorage` stores mistakes, favorites and statistics. That keeps the app easy to use, but records do not sync across devices and are lost if browser storage is cleared.

Explanations are part of the question files. Answering a question does not call a live model.

## Current limits

Only the first three patent-law topics have question data. The interface lists 30 topic names, and the other subject tabs are not populated.

Review reminders and mock examinations are placeholders. The question-history page describes an external workflow, not an integrated AI chat feature.

This is a personal study project, not an official question bank. Some content may need correction or updating.

## Run locally

```bash
git clone https://github.com/orphanwarrior/test-web.git
cd test-web
python -m http.server 8000
```

Open [localhost:8000/study.html](http://localhost:8000/study.html). Serving over HTTP lets the browser load the JSON files; Python is only the local file server.

## Files

```text
study.html                  # Interface, styles and practice logic
处理后数据/专题1-题库.json    # 26 questions
处理后数据/专题2-题库.json    # 24 questions
处理后数据/专题3-题库.json    # 26 questions
提问.md / 添加题目.md         # Content/development notes
```

My other project, [028 / TTC](https://github.com/orphanwarrior/028-ttc-showcase), explores a larger AI-assisted patent drafting workflow.
