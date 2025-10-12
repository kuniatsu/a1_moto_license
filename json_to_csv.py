#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
import re

def clean_text(text):
    """テキストをクリーニングしてCSV用に適した形式にする"""
    if not text:
        return ""
    # 改行文字を削除
    text = text.replace('\n', ' ').replace('\r', ' ')
    # 複数のスペースを1つに
    text = re.sub(r'\s+', ' ', text)
    # ダブルクォートをエスケープ
    text = text.replace('"', '""')
    return text.strip()

def extract_correct_answer(options, correct_numbers):
    """正解の選択肢を抽出"""
    correct_answers = []
    for num in correct_numbers:
        if 1 <= num <= len(options):
            answer = options[num - 1]
            # [正解]マークを削除
            answer = answer.replace(' [正解]', '')
            correct_answers.append(clean_text(answer))
    return ' | '.join(correct_answers)

def main():
    # JSONファイルを読み込み
    with open('a1Text.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # CSVファイルに書き込み
    with open('a1Text.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # ヘッダー行
        writer.writerow([
            'question_number',
            'question_text',
            'option_1',
            'option_2', 
            'option_3',
            'option_4',
            'option_count',
            'correct_answer_numbers',
            'correct_answer_text',
            'required'
        ])
        
        # データ行
        for item in data:
            question_number = item.get('question_number', '')
            question_text = clean_text(item.get('question_text', ''))
            options = item.get('options', [])
            option_count = item.get('option_count', 0)
            correct_numbers = item.get('correct_answer_numbers', [])
            required = item.get('Required', False)
            
            # 選択肢を4つまで展開（足りない場合は空文字）
            option_1 = clean_text(options[0]) if len(options) > 0 else ''
            option_2 = clean_text(options[1]) if len(options) > 1 else ''
            option_3 = clean_text(options[2]) if len(options) > 2 else ''
            option_4 = clean_text(options[3]) if len(options) > 3 else ''
            
            # 正解の選択肢テキストを抽出
            correct_answer_text = extract_correct_answer(options, correct_numbers)
            
            # 正解番号を文字列に変換
            correct_numbers_str = ', '.join(map(str, correct_numbers))
            
            writer.writerow([
                question_number,
                question_text,
                option_1,
                option_2,
                option_3,
                option_4,
                option_count,
                correct_numbers_str,
                correct_answer_text,
                required
            ])
    
    print(f"CSVファイル 'a1Text.csv' を作成しました。")
    print(f"総問題数: {len(data)}")

if __name__ == "__main__":
    main()
