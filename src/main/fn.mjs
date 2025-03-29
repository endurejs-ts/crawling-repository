import fs from 'fs';
import path from 'path';

const jsonDir = "../../dist";
const outputFile = path.join(jsonDir, "comhref.json");

const jsonFiles = Array.from({ length: 29 }, (_, i) => path.join(jsonDir, `href${i + 1}.json`));
let combinedData = [];

jsonFiles.forEach((f) => {
    const data = JSON.parse(fs.readFileSync(f, "utf-8"));

    if (Array.isArray(data)) {
        combinedData = combinedData.concat(data);
    }

    else {
        combinedData.push(data);
    }
});

fs.writeFileSync(outputFile, JSON.stringify(combinedData, null, 4), "utf-8");