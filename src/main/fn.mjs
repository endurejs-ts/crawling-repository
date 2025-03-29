import fs from 'fs';
import path from 'path';

// 원본 JSON 파일 경로
const jsonDir = "../../dist";
const inputFile = path.join(jsonDir, "comhref.json");

// 출력 파일 개수 (최대 11개)
const maxFiles = 30;

// JSON 파일 읽기
const data = JSON.parse(fs.readFileSync(inputFile, "utf-8"));

// 리스트 데이터를 나눌 개수 계산
const chunkSize = Math.ceil(data.length / maxFiles);

// JSON 파일 나누어 저장
for (let i = 1; i <= maxFiles; i++) {
    const start = (i - 1) * chunkSize;
    const end = start + chunkSize;
    const chunk = data.slice(start, end);
    
    if (chunk.length === 0) break;  // 데이터가 없으면 중단

    const outputFile = path.join(jsonDir, `href${i}.json`);
    fs.writeFileSync(outputFile, JSON.stringify(chunk, null, 4), "utf-8");

    console.log(`✅ ${outputFile} 저장 완료 (${chunk.length}개)`);
}

console.log("🎉 JSON 파일이 성공적으로 나뉘었습니다!");
