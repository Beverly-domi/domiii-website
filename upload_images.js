/**
 * 批量上传本地压缩图片到阿里云OSS
 * 上传 card/ childhood/ game/ shiny/ weibo/ 到 OSS 对应路径
 *
 * 用法:
 *   1. npm install dotenv ali-oss
 *   2. 复制 .env.example 为 .env，填入你的 AccessKey
 *   3. node upload_images.js
 */

const OSS = require('ali-oss');
const fs = require('fs');
const path = require('path');
require('dotenv').config();

const REGION = process.env.OSS_REGION;
const ACCESS_KEY_ID = process.env.OSS_ACCESS_KEY_ID;
const ACCESS_KEY_SECRET = process.env.OSS_ACCESS_KEY_SECRET;
const BUCKET = process.env.OSS_BUCKET;

if (!REGION || !ACCESS_KEY_ID || !ACCESS_KEY_SECRET || !BUCKET) {
  console.error('错误: 请在 .env 文件中配置 OSS_REGION, OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET, OSS_BUCKET');
  process.exit(1);
}

const client = new OSS({
  region: REGION,
  accessKeyId: ACCESS_KEY_ID,
  accessKeySecret: ACCESS_KEY_SECRET,
  bucket: BUCKET,
});

// 要上传的本地文件夹
const FOLDERS = ['card', 'childhood', 'game', 'shiny', 'weibo'];

// 常见图片扩展名
const IMAGE_EXTS = new Set([
  '.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.svg'
]);

const CACHE_CONTROL = 'max-age=2592000';

let total = 0;
let success = 0;
let fail = 0;

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function uploadFile(localPath, ossPath) {
  try {
    await client.put(ossPath, localPath, {
      headers: {
        'Cache-Control': CACHE_CONTROL,
      },
    });
    console.log(`[OK] ${ossPath}`);
    success++;
  } catch (err) {
    console.error(`[FAIL] ${ossPath}: ${err.message}`);
    fail++;
  }
}

async function scanAndUpload(folder) {
  const dir = path.join(__dirname, folder);
  if (!fs.existsSync(dir)) {
    console.log(`[SKIP] ${folder}/ 文件夹不存在`);
    return;
  }

  const files = fs.readdirSync(dir);
  for (const file of files) {
    const ext = path.extname(file).toLowerCase();
    if (!IMAGE_EXTS.has(ext)) continue;

    total++;
    const localPath = path.join(dir, file);
    const ossPath = folder + '/' + file;  // 保持 OSS 路径一致

    await uploadFile(localPath, ossPath);
    await sleep(30);  // 避免限流
  }
}

(async () => {
  console.log('开始上传压缩图片到 OSS...');
  console.log(`Bucket: ${BUCKET}`);
  console.log(`Cache-Control: ${CACHE_CONTROL}`);
  console.log('---');

  for (const folder of FOLDERS) {
    console.log(`\n处理 ${folder}/ ...`);
    await scanAndUpload(folder);
  }

  console.log('\n---');
  console.log(`完成! 总计:${total}, 成功:${success}, 失败:${fail}`);
  if (fail > 0) {
    console.log('有失败的文件，可以重新运行脚本重试');
  }
})();
