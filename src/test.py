import os
import json

json_folders = ["../dist/finished", "../dist/admin"]  # 두 개의 폴더에서 검색

all_data = []

# 🔍 모든 폴더에서 JSON 파일 찾기
for folder in json_folders:
    for root, _, files in os.walk(folder):  # 하위 폴더까지 탐색
        for filename in files:
            if filename.endswith(".json"):  # JSON 파일만 선택
                file_path = os.path.join(root, filename)

                # JSON 파일 읽기
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):  # 리스트 형태만 추가
                        all_data.extend(data)

print(f"📢 총 {len(all_data)}개의 데이터를 불러왔습니다.")
