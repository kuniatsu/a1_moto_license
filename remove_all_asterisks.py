#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re

def remove_all_asterisks_from_questions(data):
    """すべての問題文から最初の「*」を削除"""
    removed_count = 0
    for item in data:
        question_text = item.get('question_text', '')
        if question_text.startswith('*'):
            # 「*」の後にスペースがある場合は「* 」を削除、ない場合は「*」のみを削除
            if question_text.startswith('* '):
                item['question_text'] = question_text[2:]  # 「* 」を削除
            else:
                item['question_text'] = question_text[1:]   # 「*」を削除
            print(f"問題 {item['question_number']}: 「*」を削除しました")
            removed_count += 1
    
    return removed_count

def main():
    # JSONファイルを読み込み
    with open('a1Text.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # すべての問題文から「*」を削除
    removed_count = remove_all_asterisks_from_questions(data)
    
    # 更新したデータをファイルに書き戻し
    with open('a1Text.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n問題文から「*」を削除しました。")
    print(f"削除した問題数: {removed_count}")
    print(f"総問題数: {len(data)}")

if __name__ == "__main__":
    main()
