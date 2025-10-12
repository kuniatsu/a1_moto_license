#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv

def convert_json_to_csv(json_file_path, csv_file_path):
    """JSONファイルをCSVファイルに変換（question_length要素を含む）"""
    
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
        fieldnames = [
            "question_number", "question_text", "question_length",
            "option1", "option1_length",
            "option2", "option2_length", 
            "option3", "option3_length",
            "option4", "option4_length",
            "option_count", "correct_answer_numbers", "correct_answer_text", 
            "required", "keyword", "image", "short_last_option"
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for item in data:
            row = {
                "question_number": item.get("question_number"),
                "question_text": item.get("question_text"),
                "question_length": item.get("question_length", 0),
                "option1": item.get("option1", ""),
                "option1_length": item.get("option1_length", 0),
                "option2": item.get("option2", ""),
                "option2_length": item.get("option2_length", 0),
                "option3": item.get("option3", ""),
                "option3_length": item.get("option3_length", 0),
                "option4": item.get("option4", ""),
                "option4_length": item.get("option4_length", 0),
                "option_count": item.get("option_count"),
                "correct_answer_numbers": item.get("correct_answer_numbers")[0] if item.get("correct_answer_numbers") else "",
                "correct_answer_text": item.get("correct_answer_text", ""),
                "required": item.get("Required"),
                "keyword": item.get("keyword", ""),
                "image": item.get("image", False),
                "short_last_option": item.get("short_last_option", False)
            }
            
            writer.writerow(row)
    
    print(f"CSVファイル '{csv_file_path}' を作成しました。")
    print(f"総問題数: {len(data)}")
    print("含まれる要素:")
    print("- question_length要素")
    print("- 更新されたshort_last_option要素")
    print("- 各選択肢とその文字数")

if __name__ == "__main__":
    convert_json_to_csv('a1Text.json', 'a1Text.csv')
