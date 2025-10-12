#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re

def remove_asterisk_from_questions(data, question_numbers):
    """指定された問題番号の問題文から最初の「*」を削除"""
    for item in data:
        if item.get('question_number') in question_numbers:
            question_text = item.get('question_text', '')
            if question_text.startswith('* '):
                item['question_text'] = question_text[2:]  # 「* 」を削除
                print(f"問題 {item['question_number']}: 「*」を削除しました")

def main():
    # JSONファイルを読み込み
    with open('a1Text.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 問題208と166の「*」を削除
    remove_asterisk_from_questions(data, [208, 166])
    
    # 更新したデータをファイルに書き戻し
    with open('a1Text.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"問題文から「*」を削除しました。")
    print(f"総問題数: {len(data)}")

if __name__ == "__main__":
    main()
