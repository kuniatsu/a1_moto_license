#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re

def parse_html_to_json():
    """
    HTMLファイルから問題文と回答を抽出してJSONファイルに出力する
    
    対象1: 問題文 (card-header内のCâu X: で始まるテキスト)
    対象2: 回答 (card-body内のoption-item-resultクラス)
    正解: correct-option-reviewクラスが付いている回答に[正解]を追加
    """
    # HTMLファイルを読み込み
    with open('index2.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 問題と回答のリスト
    questions_data = []
    
    # 問題文のパターン（Câu X: で始まる）
    question_pattern = r'<strong>Câu (\d+):</strong>\s*([^<]+)'
    questions = re.findall(question_pattern, html_content)
    
    for question_num, question_text in questions:
        question_number = int(question_num)
        question_text = question_text.strip()
        
        # この問題の回答オプションを検索
        # 問題文の直後から次の問題文までを検索範囲とする
        start_pattern = f'<strong>Câu {question_number}:</strong>'
        next_pattern = f'<strong>Câu {question_number + 1}:</strong>'
        
        start_pos = html_content.find(start_pattern)
        if start_pos == -1:
            continue
            
        # 次の問題の位置を探す
        next_pos = html_content.find(next_pattern)
        if next_pos == -1:
            # 最後の問題の場合、ファイルの終わりまで
            next_pos = len(html_content)
        
        # この問題の範囲を抽出
        question_section = html_content[start_pos:next_pos]
        
        # 回答オプションを検索
        options = []
        
        # まず正解のオプション番号を取得
        correct_pattern = r'<div class="option-item-result[^"]*correct-option-review[^"]*"[^>]*>.*?<span class="option-number">(\d+)\.</span>'
        correct_matches = re.findall(correct_pattern, question_section, re.DOTALL)
        correct_options = set(correct_matches)
        
        # すべてのオプションを検索
        option_pattern = r'<div class="option-item-result[^"]*"[^>]*>.*?<label[^>]*>.*?<span class="option-number">(\d+)\.</span>\s*([^<]+)</label>'
        option_matches = re.findall(option_pattern, question_section, re.DOTALL)
        
        for option_num, option_text in option_matches:
            option_text = option_text.strip()
            
            # 正解かどうかを判定
            is_correct = option_num in correct_options
            
            # 正解の場合は[正解]を追加
            if is_correct:
                option_text += ' [正解]'
            
            options.append(option_text)
        
        # データを追加
        question_data = {
            'question_number': question_number,
            'question_text': f'Câu {question_number}: {question_text}',
            'options': options,
            'option_count': len(options),
            'correct_answer_numbers': [int(num) for num in correct_options]
        }
        
        questions_data.append(question_data)
    
    # 問題番号でソート
    questions_data.sort(key=lambda x: x['question_number'])
    
    # JSONファイルに出力
    with open('a1Text2.json', 'w', encoding='utf-8') as f:
        json.dump(questions_data, f, ensure_ascii=False, indent=2)
    
    print(f"抽出完了: {len(questions_data)}問の問題をa1Text2.jsonに出力しました。")
    
    # 最初の3問を表示して確認
    for i, q in enumerate(questions_data[:3]):
        print(f"\n問題 {q['question_number']}:")
        print(f"問題文: {q['question_text']}")
        print(f"選択肢数: {q['option_count']}")
        print(f"正解番号: {q['correct_answer_numbers']}")
        print("回答:")
        for j, option in enumerate(q['options'], 1):
            print(f"  {j}. {option}")

if __name__ == "__main__":
    parse_html_to_json()
