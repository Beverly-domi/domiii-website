/**
 * 批量设置阿里云OSS图片文件 Cache-Control 头
 * 用法:
 *   1. npm install dotenv ali-oss
 *   2. 创建 .env 文件（参照下面的模板）
 *   3. node oss_cache.js
 *
 * .env 模板:
 *   OSS_REGION=oss-cn-hangzhou
 *   OSS_ACCESS_KEY_ID=你的AccessKeyId
 *   OSS_ACCESS_KEY_SECRET=你的AccessKeySecret
 *   OSS_BUCKET=domiii
 */

const OSS = require('ali-oss');
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

// 只处理常见图片格式
const IMAGE_EXTS = new Set([
  '.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.svg', '.tiff', '.tif', '.ico'
]);

const CACHE_CONTROL = 'max-age=2592000';
let total = 0;
let success = 0;
let skip = 0;
let fail = 0;

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function processPage(marker) {
  const result = await client.list(
    { marker, 'max-keys': 100 },
    {}
  );

  const objects = result.objects;
  if (!objects || objects.length === 0) return null;

  for (const obj of objects) {
    total++;
    const name = obj.name;
    const dot = name.lastIndexOf('.');
    if (dot === -1) { skip++; continue; }
    const ext = name.substring(dot).toLowerCase();

    if (!IMAGE_EXTS.has(ext)) {
      skip++;
      continue;
    }

    try {
      await client.putMeta(name, {
        headers: { 'Cache-Control': CACHE_CONTROL },
      });
      success++;
      console.log(`[OK] ${name}`);
    } catch (err) {
      fail++;
      console.error(`[FAIL] ${name}: ${err.message}`);
    }

    await sleep(20);
  }

  return result.nextMarker;
}

(async () => {
  console.log('开始批量设置 OSS 图片 Cache-Control...');
  console.log(`Bucket: ${BUCKET}`);
  console.log(`Cache-Control: ${CACHE_CONTROL}`);
  console.log('---');

  let marker = null;
  do {
    try {
      marker = await processPage(marker);
    } catch (err) {
      console.error(`列表请求失败: ${err.message}`);
      break;
    }
  } while (marker);

  console.log('---');
  console.log(`完成! 总计:${total}, 已设置:${success}, 跳过:${skip}, 失败:${fail}`);
})();
