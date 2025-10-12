#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re

def clean_question_text(text):
    """問題文から「Câu X:」の部分を削除"""
    if not text:
        return text
    
    # 「Câu X:」のパターンを削除（Xは数字）
    pattern = r'^Câu\s+\d+:\s*'
    cleaned_text = re.sub(pattern, '', text)
    
    return cleaned_text

def main():
    # JSONファイルを読み込み
    with open('a1Text.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 各問題の問題文をクリーニング
    for item in data:
        if 'question_text' in item:
            item['question_text'] = clean_question_text(item['question_text'])
    
    # クリーニングしたデータをファイルに書き戻し
    with open('a1Text.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"問題文から「Câu X:」の部分を削除しました。")
    print(f"総問題数: {len(data)}")

if __name__ == "__main__":
    main()
