import { existsSync, readFileSync, writeFileSync } from "fs";
import { join } from "path";

// JSON 파일이 위치한 경로
function fucingMakingFunction(led, cn) {
    const jsonDir = `../dist/noadmin/${cn}/bottom/data`;
    const outputFile = join("../dist/finished/", `${cn}f.json`);

    const jsonFiles = Array.from({ length: led }, (_, i) => join(jsonDir, `data${i + 1}.json`));
    let combinedData = [];

    jsonFiles.forEach((file) => {
        if (existsSync(file)) {  // 파일 존재 여부 확인
            try {
                const data = JSON.parse(readFileSync(file, "utf-8"));
                if (Array.isArray(data)) {
                    combinedData = combinedData.concat(data);
                } else {
                    combinedData.push(data);
                }
            } catch (error) {
                console.warn(`⚠️ JSON 파일 ${file} 읽기 오류 발생`);
            }
        }
    });

    // 합쳐진 데이터를 comhref.json에 저장
    writeFileSync(outputFile, JSON.stringify(combinedData, null, 4), "utf-8");
    console.log(`✅ 모든 JSON 파일이 ${outputFile}으로 합쳐졌습니다.`);
}

fucingMakingFunction(23, 44);
