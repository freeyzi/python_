import requests

cookie = {
    "_zap":"5a3ea060-9a2d-48dd-b9d4-9ac973ce4ffb",
    "q_c1":"4540ae28f88f4fe394e6124814ec7e2e|1524593144000|1524593144000",
    "r_cap_id":"OGE3NGM2MDU3Y2I3NDI2ZDk5ZDJmZGRiM2I2MjliYjA=|1524593144|4ad3bb076f7f28955140569c4ab49adaa29590bc",
    "cap_id":"N2VhNGM5MzE3NjQ2NDRhYWI4YzBkZTU1MjJmZTc2ZGM=|1524593144|d44027b7a2dcea8164892ff8e4a02e3599ebaa1b",
    "l_cap_id":"Y2E5OWFjNmUyNTk4NGE2MDkyMWNlNjUyMzk4MTY1NDg=|1524593144|9cfa8ab3b96dfee373318d3583faeb514e49df0d",
    "aliyungf_tc":"AQAAALw3VwhMUgwA7Y0mGxFu0w6cRM96",
    "_xsrf":"656da94e-0e84-4c42-8a2c-86a201bbbf1d",
    "d_c0":"AIBg-UFPiA2PTsoF8hgAsPS0ci-XVvNscbM=|1525265881",
    "capsion_ticket":"2|1:0|10:1525265895|14:capsion_ticket|44:NDBlNTE0MzhkN2U1NDllNTliMTk2NmFlNmRhZmJhMWU=|9c30a273a7870924e4d3ab10085a3597ad3b88621286205deb9b5431b68e4e67",
    "z_c0":"2|1:0|10:1525265937|4:z_c0|92:Mi4xbW90WkJ3QUFBQUFBZ0dENVFVLUlEU1lBQUFCZ0FsVk5FUVRYV3dEOWJQRmVzQkJOX2J2cGFxWTB6UExRNVhfTGJn|ea249be25e4d02a1617754c50104080d501224e5d3fdc6c1184cf47fe32f397d",
    "unlock_ticket":"AHCmHWNr_wwmAAAAYAJVTRm96Vq_OeklKHLqVijhdMZjPf7UzrkrmQ=="
}
headers = {
    "Host":"www.zhihu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}

r = requests.get("https://www.zhihu.com",headers=headers,cookies=cookie)
print(r.text)