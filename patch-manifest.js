// Puts the AdMob App ID from www/admob.config.json into AndroidManifest.xml
const fs=require('fs');
const cfg=JSON.parse(fs.readFileSync('www/admob.config.json','utf8'));
const f='android/app/src/main/AndroidManifest.xml';
let x=fs.readFileSync(f,'utf8');
if(!x.includes('com.google.android.gms.ads.APPLICATION_ID')){
  x=x.replace('</application>',`    <meta-data android:name="com.google.android.gms.ads.APPLICATION_ID" android:value="${cfg.appId}"/>\n    </application>`);
  fs.writeFileSync(f,x);
}
console.log('AdMob App ID set:',cfg.appId);
