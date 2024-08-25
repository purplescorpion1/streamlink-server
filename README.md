# streamlink-server
Run your m3u streams through streamlink

## What is the purpose of this?
Some streams from providers may not be stable, in a format a player can play or be able to record the stream. Running it through streamlink your player should be able to play and record the stream without any issue

## Requirements
Python with pip

## Installation
```
git clone https://github.com/purplescorpion1/streamlink-server.git
```
```
cd streamlink-server
```
```
pip install flask
```
## Instructions - Read Fully!!

Make sure [streamlink](https://streamlink.github.io/install.html) is installed and available at path

Open stream_link_server.py <br>
Change the port number at the bottom to the port you want the script to run <br>
<br>
Open your m3u file in notepad++ <br>
Before all the stream links add (changing ip and port to your actual ip and port values)
```
http://ip:port/stream?url=
```
eg it will look like <br>
```
http://192.168.1.123:6090/stream?url=http://cfd-v4-service-channel-stitcher-use1-1.prd.pluto.tv/stitch/hls/channel/5ad8d1e9e738977e2c310925/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=4c9b8520-6224-11ef-9154-83018d21c856&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=16d72f2e-ab58-4ea1-9554-e127c7674652&userId=&serverSideAds=true
```

You can use notepad++ to automatically add it in, using find and replace, to save you manually adding it all to every stream url in your m3u <br>
eg in the example above you would say <br>
Find http://cfd and replace with http://192.168.1.123:6090/stream?url=http://cfd <br>
<br>
Open encodeurls.py <br>
<br>
Change <br>
```
base_url = 'http://192.168.1.123:6090/stream?url='
```
so the IP and port matches what you are running it on <br>
<br>
Change
```
input_file = 'input.m3u'
```
to the name of your m3u file <br>
eg
```
input_file = 'mym3ufile.m3u'
```

In a terminal/cmd window run <br>
```
python encodeurls.py
```
it will output output_encoded.m3u <br>
<br>
Your stream link should now look like this
```
http://192.168.1.123:6090/stream?url=http%3A%2F%2Fcfd-v4-service-channel-stitcher-use1-1.prd.pluto.tv%2Fstitch%2Fhls%2Fchannel%2F663a3eb8b18d700008db8c1a%2Fmaster.m3u8%3FadvertisingId%3D%26appName%3Dweb%26appVersion%3Dunknown%26appStoreUrl%3D%26architecture%3D%26buildVersion%3D%26clientTime%3D0%26deviceDNT%3D0%26deviceId%3D4ca15182-6224-11ef-9154-83018d21c856%26deviceMake%3DChrome%26deviceModel%3Dweb%26deviceType%3Dweb%26deviceVersion%3Dunknown%26includeExtendedEvents%3Dfalse%26sid%3Deb27f56c-62af-4331-b9dc-775d5c2ac337%26userId%3D%26serverSideAds%3Dtrue
```
In a terminal/cmd window run
```
python stream_link_server.py
```
Open output_encoded.m3u with your chosen player and it will stream the urls through streamlink to your player <br>
You can rename output_encoded.m3u to any name you wish
